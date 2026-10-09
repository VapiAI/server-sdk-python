"""Verify both replacement states documented by the official API schema."""
import httpx
import pytest

from vapi import AsyncVapi, Vapi


def handler(status):
    def respond(request):
        assert request.method == "GET"
        assert request.url.path == "/assistant/assistant-test"
        notice = {
            "slot": "model",
            "provider": "openai",
            "model": "gpt-4-1106-preview",
            "deprecationDate": "2026-09-01",
            "retirementDate": "2026-10-01",
            "replacementStatus": status,
        }
        if status == "available":
            notice["replacementModel"] = "gpt-5"
        return httpx.Response(200, json={
            "id": "assistant-test",
            "orgId": "org-test",
            "createdAt": "2026-10-07T00:00:00Z",
            "updatedAt": "2026-10-07T00:00:00Z",
            "modelDeprecations": [notice],
        })
    return respond


def assert_notice(result, status):
    assert len(result.model_deprecations) == 1
    notice = result.model_deprecations[0]
    assert notice.replacement_status == status
    assert notice.replacement_model == ("gpt-5" if status == "available" else None)


@pytest.mark.parametrize("status", ["available", "manual-action-required"])
def test_sync_model_deprecation_notice(status):
    with httpx.Client(transport=httpx.MockTransport(handler(status))) as http:
        result = Vapi(token="test", httpx_client=http).assistants.get("assistant-test")
        assert_notice(result, status)


@pytest.mark.asyncio
@pytest.mark.parametrize("status", ["available", "manual-action-required"])
async def test_async_model_deprecation_notice(status):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler(status))) as http:
        result = await AsyncVapi(token="test", httpx_client=http).assistants.get("assistant-test")
        assert_notice(result, status)
