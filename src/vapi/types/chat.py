# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .assistant_overrides import AssistantOverrides
from .chat_costs_item import ChatCostsItem
from .chat_input import ChatInput
from .chat_messages_item import ChatMessagesItem
from .chat_output_item import ChatOutputItem
from .create_assistant_dto import CreateAssistantDto


class Chat(UncheckedBaseModel):
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.
    """

    assistant_overrides: typing_extensions.Annotated[
        typing.Optional[AssistantOverrides], FieldMetadata(alias="assistantOverrides")
    ] = pydantic.Field(default=None)
    """
    These are the variable values that will be used to replace template variables in the assistant messages.
    Only variable substitution is supported in chat contexts - other assistant properties cannot be overridden.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the chat. This is just for your own reference.
    """

    session_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="sessionId")] = pydantic.Field(
        default=None
    )
    """
    This is the ID of the session that will be used for the chat.
    Mutually exclusive with previousChatId.
    """

    input: typing.Optional[ChatInput] = pydantic.Field(default=None)
    """
    This is the input text for the chat.
    Can be a string or an array of chat messages.
    """

    stream: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This is a flag that determines whether the response should be streamed.
    When true, the response will be sent as chunks of text.
    """

    previous_chat_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="previousChatId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ID of the chat that will be used as context for the new chat.
    The messages from the previous chat will be used as context.
    Mutually exclusive with sessionId.
    """

    id: str = pydantic.Field()
    """
    This is the unique identifier for the chat.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this chat belongs to.
    """

    messages: typing.Optional[typing.List[ChatMessagesItem]] = pydantic.Field(default=None)
    """
    This is an array of messages used as context for the chat.
    Used to provide message history for multi-turn conversations.
    """

    output: typing.Optional[typing.List[ChatOutputItem]] = pydantic.Field(default=None)
    """
    This is the output messages generated by the system in response to the input.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the chat was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the chat was last updated.
    """

    costs: typing.Optional[typing.List[ChatCostsItem]] = pydantic.Field(default=None)
    """
    These are the costs of individual components of the chat in USD.
    """

    cost: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the cost of the chat in USD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
