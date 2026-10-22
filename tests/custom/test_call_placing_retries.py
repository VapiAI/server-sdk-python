"""A request that places phone calls must not be replayed after an ambiguous failure.

The API takes no idempotency key for these POSTs, so a retry after a 5xx, 408, 409 or a
dropped connection can dial the same customer a second time.
"""

import httpx
import pytest

import vapi.core.http_client as http_client
from vapi import AsyncVapi, Vapi
from vapi.core.api_error import ApiError

AMBIGUOUS_STATUSES = [500, 502, 503, 504, 408, 409]

CALL = {
    "id": "call-1",
    "orgId": "org",
    "createdAt": "2026-10-22T00:00:00Z",
    "updatedAt": "2026-10-22T00:00:00Z",
    "type": "outboundPhoneCall",
    "status": "queued",
}

CALL_PLACING = [
    pytest.param(
        "/call",
        lambda c: c.calls.create(assistant_id="asst-1", phone_number_id="pn-1", customer={"number": "+14155550199"}),
        id="calls.create",
    ),
    pytest.param(
        "/campaign",
        lambda c: c.campaigns.campaign_controller_create(name="Q2", customers=[{"number": "+14155550199"}]),
        id="campaigns.create",
    ),
    pytest.param(
        "/v2/campaign",
        lambda c: c.campaigns.campaign_controller_create_v_2(name="Q2", customers=[{"number": "+14155550199"}]),
        id="campaigns.create_v2",
    ),
]


@pytest.fixture(autouse=True)
def no_backoff(monkeypatch):
    monkeypatch.setattr(http_client, "_retry_timeout", lambda response, retries: 0)
    monkeypatch.setattr(http_client, "_retry_timeout_from_retries", lambda retries: 0)


def recorder(replies):
    """Return (requests, handler); the handler answers with each reply in turn, then repeats the last."""
    seen = []

    def handler(request):
        seen.append((request.method, request.url.path))
        reply = replies[min(len(seen), len(replies)) - 1]
        if isinstance(reply, Exception):
            raise reply
        return reply

    return seen, handler


def client_for(handler):
    return Vapi(
        token="test", base_url="https://api.test", httpx_client=httpx.Client(transport=httpx.MockTransport(handler))
    )


@pytest.mark.parametrize("status", AMBIGUOUS_STATUSES)
@pytest.mark.parametrize("path,place", CALL_PLACING)
def test_call_placing_post_is_sent_once_after_ambiguous_status(path, place, status):
    seen, handler = recorder([httpx.Response(status, json={"message": "upstream timed out"})])
    with pytest.raises(ApiError) as err:
        place(client_for(handler))
    assert err.value.status_code == status
    assert seen == [("POST", path)]


@pytest.mark.parametrize("path,place", CALL_PLACING)
def test_call_placing_post_is_sent_once_after_dropped_connection(path, place):
    seen, handler = recorder([httpx.RemoteProtocolError("Server disconnected without sending a response.")])
    with pytest.raises(httpx.RemoteProtocolError):
        place(client_for(handler))
    assert seen == [("POST", path)]


def test_call_create_is_still_retried_on_429():
    seen, handler = recorder([httpx.Response(429, json={"message": "rate limited"}), httpx.Response(201, json=CALL)])
    call = client_for(handler).calls.create(assistant_id="asst-1", customer={"number": "+14155550199"})
    assert call.id == "call-1"
    assert seen == [("POST", "/call"), ("POST", "/call")]


def test_call_create_is_still_retried_when_the_connection_never_opened():
    seen, handler = recorder([httpx.ConnectError("connection refused"), httpx.Response(201, json=CALL)])
    call = client_for(handler).calls.create(assistant_id="asst-1", customer={"number": "+14155550199"})
    assert call.id == "call-1"
    assert len(seen) == 2


def test_other_requests_keep_their_retries():
    seen, handler = recorder([httpx.Response(503, json={}), httpx.Response(200, json=[])])
    client_for(handler).calls.list()
    assert seen == [("GET", "/call"), ("GET", "/call")]

    seen, handler = recorder([httpx.Response(503, json={}), httpx.Response(201, json={"id": "a-1"})])
    client_for(handler).assistants.create(name="support")
    assert seen == [("POST", "/assistant"), ("POST", "/assistant")]


async def test_async_call_create_is_sent_once_after_502():
    seen, handler = recorder([httpx.Response(502, json={"message": "Bad Gateway"})])
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        client = AsyncVapi(token="test", base_url="https://api.test", httpx_client=http)
        with pytest.raises(ApiError):
            await client.calls.create(assistant_id="asst-1", customer={"number": "+14155550199"})
    assert seen == [("POST", "/call")]


async def test_async_call_create_is_sent_once_after_dropped_connection():
    seen, handler = recorder([httpx.RemoteProtocolError("Server disconnected without sending a response.")])
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
        client = AsyncVapi(token="test", base_url="https://api.test", httpx_client=http)
        with pytest.raises(httpx.RemoteProtocolError):
            await client.calls.create(assistant_id="asst-1", customer={"number": "+14155550199"})
    assert seen == [("POST", "/call")]
