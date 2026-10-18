import datetime as dt
import os
import time

import httpx
import pytest

from vapi import AsyncVapi, Vapi


@pytest.fixture
def pacific_timezone():
    if not hasattr(time, "tzset"):
        pytest.skip("runtime timezone switching requires time.tzset")
    previous = os.environ.get("TZ")
    os.environ["TZ"] = "America/Los_Angeles"
    time.tzset()
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop("TZ", None)
        else:
            os.environ["TZ"] = previous
        time.tzset()


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    "field,wire_field",
    [
        ("created_at_ge", "createdAtGe"),
        ("created_at_le", "createdAtLe"),
        ("updated_at_ge", "updatedAtGe"),
        ("updated_at_le", "updatedAtLe"),
    ],
)
@pytest.mark.parametrize(
    "value,expected",
    [
        (dt.datetime(2026, 1, 15, 12), "2026-01-15T12:00:00-08:00"),
        (dt.datetime(2026, 7, 15, 12), "2026-07-15T12:00:00-07:00"),
        (dt.datetime(2026, 11, 1, 1, 30, fold=0), "2026-11-01T01:30:00-07:00"),
        (dt.datetime(2026, 11, 1, 1, 30, fold=1), "2026-11-01T01:30:00-08:00"),
        (dt.datetime(2026, 1, 15, 12, tzinfo=dt.timezone.utc), "2026-01-15T12:00:00Z"),
        (
            dt.datetime(2026, 1, 15, 12, tzinfo=dt.timezone(dt.timedelta(hours=5, minutes=30))),
            "2026-01-15T12:00:00+05:30",
        ),
        (dt.datetime(2026, 1, 15, 12, 0, 0, 123456), "2026-01-15T12:00:00.123456-08:00"),
    ],
)
async def test_call_filters_use_date_specific_local_offset(
    pacific_timezone, asynchronous, field, wire_field, value, expected
):
    requests = []

    def respond(request):
        requests.append(request)
        return httpx.Response(200, json=[])

    if asynchronous:
        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http:
            client = AsyncVapi(token="test", httpx_client=http)
            result = await client.calls.list(**{field: value})
    else:
        with httpx.Client(transport=httpx.MockTransport(respond)) as http:
            client = Vapi(token="test", httpx_client=http)
            result = client.calls.list(**{field: value})
    assert result == []
    assert len(requests) == 1
    assert requests[0].url.params[wire_field] == expected
