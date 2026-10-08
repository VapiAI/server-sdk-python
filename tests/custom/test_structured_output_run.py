import httpx
import pytest

from vapi import AsyncVapi, Vapi
from vapi.types.structured_output_rerun_response import StructuredOutputRerunResponse


PAYLOADS = [
    pytest.param({"workflowId": "workflow-test", "message": "Rerun started"}, False, id="rerun-with-workflow"),
    pytest.param({"message": "Rerun started"}, False, id="rerun-without-workflow"),
    pytest.param({}, True, id="empty-preview"),
    pytest.param({"output-test": {"name": "Score", "result": 42}, "skipped": {}}, True, id="preview-result"),
]


def assert_response(result, payload, preview):
    if preview:
        assert not isinstance(result, StructuredOutputRerunResponse)
        assert hasattr(result, "skipped")
        if "skipped" in payload:
            assert result.skipped == {}
            assert getattr(result, "output-test")["result"] == 42
    else:
        assert isinstance(result, StructuredOutputRerunResponse)
        assert result.workflow_id == payload.get("workflowId")
        assert result.message == payload["message"]


def response_handler(payload):
    def handler(request):
        assert request.method == "POST"
        assert request.url.path == "/structured-output/run"
        return httpx.Response(200, json=payload)

    return handler


@pytest.mark.parametrize("payload,preview", PAYLOADS)
def test_sync_structured_output_run_response(payload, preview):
    with httpx.Client(transport=httpx.MockTransport(response_handler(payload))) as http:
        client = Vapi(token="test", httpx_client=http)
        result = client.structured_outputs.structured_output_controller_run(
            call_ids=["call-test"], structured_output_id="output-test", preview_enabled=preview
        )
        assert_response(result, payload, preview)


@pytest.mark.parametrize("payload,preview", PAYLOADS)
async def test_async_structured_output_run_response(payload, preview):
    async with httpx.AsyncClient(transport=httpx.MockTransport(response_handler(payload))) as http:
        client = AsyncVapi(token="test", httpx_client=http)
        result = await client.structured_outputs.structured_output_controller_run(
            call_ids=["call-test"], structured_output_id="output-test", preview_enabled=preview
        )
        assert_response(result, payload, preview)
