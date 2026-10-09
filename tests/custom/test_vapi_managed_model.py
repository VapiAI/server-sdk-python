"""Verify the supported tagged request types send version-only Vapi models."""
import json

import httpx
import pytest

from vapi import AsyncVapi, Vapi
from vapi.types.create_assistant_dto_model import CreateAssistantDtoModel_Vapi
from vapi.assistants.types.update_assistant_dto_model import UpdateAssistantDtoModel_Vapi


def handler(operation):
    def respond(request):
        assert request.method == ("POST" if operation == "create" else "PATCH")
        assert request.url.path == ("/assistant" if operation == "create" else "/assistant/assistant-test")
        body = json.loads(request.content)
        assert body["model"] == {"provider": "vapi", "version": "latest"}
        return httpx.Response(200, json={"id": "assistant-test", "model": body["model"]})
    return respond


@pytest.mark.parametrize("operation", ["create", "update"])
def test_sync_version_only_vapi_model(operation):
    with httpx.Client(transport=httpx.MockTransport(handler(operation))) as http:
        client = Vapi(token="test", httpx_client=http)
        if operation == "create":
            result = client.assistants.create(model=CreateAssistantDtoModel_Vapi(version="latest"))
        else:
            result = client.assistants.update("assistant-test", model=UpdateAssistantDtoModel_Vapi(version="latest"))
        assert result.model.provider == "vapi"
        assert result.model.version == "latest"


@pytest.mark.asyncio
@pytest.mark.parametrize("operation", ["create", "update"])
async def test_async_version_only_vapi_model(operation):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler(operation))) as http:
        client = AsyncVapi(token="test", httpx_client=http)
        if operation == "create":
            result = await client.assistants.create(model=CreateAssistantDtoModel_Vapi(version="latest"))
        else:
            result = await client.assistants.update("assistant-test", model=UpdateAssistantDtoModel_Vapi(version="latest"))
        assert result.model.provider == "vapi"
        assert result.model.version == "latest"
