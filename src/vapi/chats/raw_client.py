# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.unchecked_base_model import construct_type
from ..types.assistant_overrides import AssistantOverrides
from ..types.chat import Chat
from ..types.chat_paginated_response import ChatPaginatedResponse
from ..types.create_assistant_dto import CreateAssistantDto
from .types.chats_create_response import ChatsCreateResponse
from .types.chats_create_response_response import ChatsCreateResponseResponse
from .types.chats_list_request_sort_order import ChatsListRequestSortOrder
from .types.create_chat_dto_input import CreateChatDtoInput
from .types.open_ai_responses_request_input import OpenAiResponsesRequestInput

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawChatsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        assistant_id: typing.Optional[str] = None,
        workflow_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[ChatsListRequestSortOrder] = None,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatPaginatedResponse]:
        """
        Parameters
        ----------
        assistant_id : typing.Optional[str]
            This is the unique identifier for the assistant that will be used for the chat.

        workflow_id : typing.Optional[str]
            This is the unique identifier for the workflow that will be used for the chat.

        session_id : typing.Optional[str]
            This is the unique identifier for the session that will be used for the chat.

        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[ChatsListRequestSortOrder]
            This is the sort order for pagination. Defaults to 'DESC'.

        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatPaginatedResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "chat",
            method="GET",
            params={
                "assistantId": assistant_id,
                "workflowId": workflow_id,
                "sessionId": session_id,
                "page": page,
                "sortOrder": sort_order,
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatPaginatedResponse,
                    construct_type(
                        type_=ChatPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        input: CreateChatDtoInput,
        assistant_id: typing.Optional[str] = OMIT,
        assistant: typing.Optional[CreateAssistantDto] = OMIT,
        assistant_overrides: typing.Optional[AssistantOverrides] = OMIT,
        name: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        previous_chat_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatsCreateResponse]:
        """
        Creates a new chat. Requires at least one of: assistantId/assistant, sessionId, or previousChatId. Note: sessionId and previousChatId are mutually exclusive.

        Parameters
        ----------
        input : CreateChatDtoInput
            This is the input text for the chat.
            Can be a string or an array of chat messages.
            This field is REQUIRED for chat creation.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant : typing.Optional[CreateAssistantDto]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant_overrides : typing.Optional[AssistantOverrides]
            These are the variable values that will be used to replace template variables in the assistant messages.
            Only variable substitution is supported in chat contexts - other assistant properties cannot be overridden.

        name : typing.Optional[str]
            This is the name of the chat. This is just for your own reference.

        session_id : typing.Optional[str]
            This is the ID of the session that will be used for the chat.
            Mutually exclusive with previousChatId.

        stream : typing.Optional[bool]
            This is a flag that determines whether the response should be streamed.
            When true, the response will be sent as chunks of text.

        previous_chat_id : typing.Optional[str]
            This is the ID of the chat that will be used as context for the new chat.
            The messages from the previous chat will be used as context.
            Mutually exclusive with sessionId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatsCreateResponse]
            Chat response - either non-streaming chat or streaming
        """
        _response = self._client_wrapper.httpx_client.request(
            "chat",
            method="POST",
            json={
                "assistantId": assistant_id,
                "assistant": convert_and_respect_annotation_metadata(
                    object_=assistant, annotation=CreateAssistantDto, direction="write"
                ),
                "assistantOverrides": convert_and_respect_annotation_metadata(
                    object_=assistant_overrides, annotation=AssistantOverrides, direction="write"
                ),
                "name": name,
                "sessionId": session_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CreateChatDtoInput, direction="write"
                ),
                "stream": stream,
                "previousChatId": previous_chat_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatsCreateResponse,
                    construct_type(
                        type_=ChatsCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Chat]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Chat]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"chat/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Chat,
                    construct_type(
                        type_=Chat,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Chat]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Chat]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"chat/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Chat,
                    construct_type(
                        type_=Chat,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_response(
        self,
        *,
        input: OpenAiResponsesRequestInput,
        assistant_id: typing.Optional[str] = OMIT,
        assistant: typing.Optional[CreateAssistantDto] = OMIT,
        assistant_overrides: typing.Optional[AssistantOverrides] = OMIT,
        name: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        previous_chat_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatsCreateResponseResponse]:
        """
        Parameters
        ----------
        input : OpenAiResponsesRequestInput
            This is the input text for the chat.
            Can be a string or an array of chat messages.
            This field is REQUIRED for chat creation.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant : typing.Optional[CreateAssistantDto]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant_overrides : typing.Optional[AssistantOverrides]
            These are the variable values that will be used to replace template variables in the assistant messages.
            Only variable substitution is supported in chat contexts - other assistant properties cannot be overridden.

        name : typing.Optional[str]
            This is the name of the chat. This is just for your own reference.

        session_id : typing.Optional[str]
            This is the ID of the session that will be used for the chat.
            Mutually exclusive with previousChatId.

        stream : typing.Optional[bool]
            Whether to stream the response or not.

        previous_chat_id : typing.Optional[str]
            This is the ID of the chat that will be used as context for the new chat.
            The messages from the previous chat will be used as context.
            Mutually exclusive with sessionId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatsCreateResponseResponse]
            OpenAI Responses API format - either non-streaming or streaming
        """
        _response = self._client_wrapper.httpx_client.request(
            "chat/responses",
            method="POST",
            json={
                "assistantId": assistant_id,
                "assistant": convert_and_respect_annotation_metadata(
                    object_=assistant, annotation=CreateAssistantDto, direction="write"
                ),
                "assistantOverrides": convert_and_respect_annotation_metadata(
                    object_=assistant_overrides, annotation=AssistantOverrides, direction="write"
                ),
                "name": name,
                "sessionId": session_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=OpenAiResponsesRequestInput, direction="write"
                ),
                "stream": stream,
                "previousChatId": previous_chat_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatsCreateResponseResponse,
                    construct_type(
                        type_=ChatsCreateResponseResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawChatsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        assistant_id: typing.Optional[str] = None,
        workflow_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[ChatsListRequestSortOrder] = None,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatPaginatedResponse]:
        """
        Parameters
        ----------
        assistant_id : typing.Optional[str]
            This is the unique identifier for the assistant that will be used for the chat.

        workflow_id : typing.Optional[str]
            This is the unique identifier for the workflow that will be used for the chat.

        session_id : typing.Optional[str]
            This is the unique identifier for the session that will be used for the chat.

        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[ChatsListRequestSortOrder]
            This is the sort order for pagination. Defaults to 'DESC'.

        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatPaginatedResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "chat",
            method="GET",
            params={
                "assistantId": assistant_id,
                "workflowId": workflow_id,
                "sessionId": session_id,
                "page": page,
                "sortOrder": sort_order,
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatPaginatedResponse,
                    construct_type(
                        type_=ChatPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        input: CreateChatDtoInput,
        assistant_id: typing.Optional[str] = OMIT,
        assistant: typing.Optional[CreateAssistantDto] = OMIT,
        assistant_overrides: typing.Optional[AssistantOverrides] = OMIT,
        name: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        previous_chat_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatsCreateResponse]:
        """
        Creates a new chat. Requires at least one of: assistantId/assistant, sessionId, or previousChatId. Note: sessionId and previousChatId are mutually exclusive.

        Parameters
        ----------
        input : CreateChatDtoInput
            This is the input text for the chat.
            Can be a string or an array of chat messages.
            This field is REQUIRED for chat creation.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant : typing.Optional[CreateAssistantDto]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant_overrides : typing.Optional[AssistantOverrides]
            These are the variable values that will be used to replace template variables in the assistant messages.
            Only variable substitution is supported in chat contexts - other assistant properties cannot be overridden.

        name : typing.Optional[str]
            This is the name of the chat. This is just for your own reference.

        session_id : typing.Optional[str]
            This is the ID of the session that will be used for the chat.
            Mutually exclusive with previousChatId.

        stream : typing.Optional[bool]
            This is a flag that determines whether the response should be streamed.
            When true, the response will be sent as chunks of text.

        previous_chat_id : typing.Optional[str]
            This is the ID of the chat that will be used as context for the new chat.
            The messages from the previous chat will be used as context.
            Mutually exclusive with sessionId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatsCreateResponse]
            Chat response - either non-streaming chat or streaming
        """
        _response = await self._client_wrapper.httpx_client.request(
            "chat",
            method="POST",
            json={
                "assistantId": assistant_id,
                "assistant": convert_and_respect_annotation_metadata(
                    object_=assistant, annotation=CreateAssistantDto, direction="write"
                ),
                "assistantOverrides": convert_and_respect_annotation_metadata(
                    object_=assistant_overrides, annotation=AssistantOverrides, direction="write"
                ),
                "name": name,
                "sessionId": session_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=CreateChatDtoInput, direction="write"
                ),
                "stream": stream,
                "previousChatId": previous_chat_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatsCreateResponse,
                    construct_type(
                        type_=ChatsCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[Chat]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Chat]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chat/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Chat,
                    construct_type(
                        type_=Chat,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Chat]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Chat]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chat/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Chat,
                    construct_type(
                        type_=Chat,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_response(
        self,
        *,
        input: OpenAiResponsesRequestInput,
        assistant_id: typing.Optional[str] = OMIT,
        assistant: typing.Optional[CreateAssistantDto] = OMIT,
        assistant_overrides: typing.Optional[AssistantOverrides] = OMIT,
        name: typing.Optional[str] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        previous_chat_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatsCreateResponseResponse]:
        """
        Parameters
        ----------
        input : OpenAiResponsesRequestInput
            This is the input text for the chat.
            Can be a string or an array of chat messages.
            This field is REQUIRED for chat creation.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant : typing.Optional[CreateAssistantDto]
            This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.

        assistant_overrides : typing.Optional[AssistantOverrides]
            These are the variable values that will be used to replace template variables in the assistant messages.
            Only variable substitution is supported in chat contexts - other assistant properties cannot be overridden.

        name : typing.Optional[str]
            This is the name of the chat. This is just for your own reference.

        session_id : typing.Optional[str]
            This is the ID of the session that will be used for the chat.
            Mutually exclusive with previousChatId.

        stream : typing.Optional[bool]
            Whether to stream the response or not.

        previous_chat_id : typing.Optional[str]
            This is the ID of the chat that will be used as context for the new chat.
            The messages from the previous chat will be used as context.
            Mutually exclusive with sessionId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatsCreateResponseResponse]
            OpenAI Responses API format - either non-streaming or streaming
        """
        _response = await self._client_wrapper.httpx_client.request(
            "chat/responses",
            method="POST",
            json={
                "assistantId": assistant_id,
                "assistant": convert_and_respect_annotation_metadata(
                    object_=assistant, annotation=CreateAssistantDto, direction="write"
                ),
                "assistantOverrides": convert_and_respect_annotation_metadata(
                    object_=assistant_overrides, annotation=AssistantOverrides, direction="write"
                ),
                "name": name,
                "sessionId": session_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=OpenAiResponsesRequestInput, direction="write"
                ),
                "stream": stream,
                "previousChatId": previous_chat_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatsCreateResponseResponse,
                    construct_type(
                        type_=ChatsCreateResponseResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
