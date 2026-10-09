"""Exercise tool variants declared by the live API's oneOf response/request schemas."""
import json

import httpx
import pytest

from vapi import AsyncVapi, Vapi
from vapi.tools.types.create_tools_request import CreateToolsRequest_Code
from vapi.tools.types.update_tools_request_body import UpdateToolsRequestBody_Code


CODE = "return { ok: true };"
BASE = {
    "id": "tool-test",
    "orgId": "org-test",
    "createdAt": "2026-10-07T00:00:00Z",
    "updatedAt": "2026-10-07T00:00:00Z",
}


def handler(operation, kind):
    def respond(request):
        expected = {
            "list": ("GET", "/tool"),
            "create": ("POST", "/tool"),
            "get": ("GET", "/tool/tool-test"),
            "update": ("PATCH", "/tool/tool-test"),
            "delete": ("DELETE", "/tool/tool-test"),
        }
        assert (request.method, request.url.path) == expected[operation]
        if operation in {"create", "update"}:
            assert json.loads(request.content) == {"type": "code", "code": CODE, "async": True}
        if kind == "code":
            payload = {**BASE, "type": "code", "code": CODE, "async": True}
        else:
            payload = {**BASE, "type": "ghl", "metadata": {"workflowId": "workflow-test", "locationId": "location-test"}}
        if operation == "list":
            payload = [payload]
        return httpx.Response(201 if operation == "create" else 200, json=payload)
    return respond


def args(operation):
    if operation == "create":
        return (), {"request": CreateToolsRequest_Code(code=CODE, async_=True)}
    if operation == "update":
        return ("tool-test",), {"request": UpdateToolsRequestBody_Code(code=CODE, async_=True)}
    return (() if operation == "list" else ("tool-test",)), {}


def assert_result(result, operation, kind):
    if operation == "list":
        assert len(result) == 1
        result = result[0]
    assert result.type == kind
    assert result.id == "tool-test"
    assert result.org_id == "org-test"
    if kind == "code":
        assert type(result).__name__.endswith("_Code")
        assert result.code == CODE
        assert result.async_ is True
    else:
        assert type(result).__name__.endswith("_Ghl")
        assert result.metadata.workflow_id == "workflow-test"
        assert result.metadata.location_id == "location-test"


CASES = [(op, "code") for op in ["create", "update"]] + [
    (op, "ghl") for op in ["list", "create", "get", "update", "delete"]
]


@pytest.mark.parametrize("operation,kind", CASES)
def test_sync_tool_variant(operation, kind):
    with httpx.Client(transport=httpx.MockTransport(handler(operation, kind))) as http:
        client = Vapi(token="test", httpx_client=http)
        positional, keywords = args(operation)
        result = getattr(client.tools, operation)(*positional, **keywords)
        assert_result(result, operation, kind)


@pytest.mark.asyncio
@pytest.mark.parametrize("operation,kind", CASES)
async def test_async_tool_variant(operation, kind):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler(operation, kind))) as http:
        client = AsyncVapi(token="test", httpx_client=http)
        positional, keywords = args(operation)
        result = await getattr(client.tools, operation)(*positional, **keywords)
        assert_result(result, operation, kind)
