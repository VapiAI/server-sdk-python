# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .artifact import Artifact
from .call import Call
from .chat import Chat
from .create_assistant_dto import CreateAssistantDto
from .create_customer_dto import CreateCustomerDto
from .server_message_tool_calls_phone_number import ServerMessageToolCallsPhoneNumber
from .server_message_tool_calls_tool_with_tool_call_list_item import ServerMessageToolCallsToolWithToolCallListItem
from .tool_call import ToolCall


class ServerMessageToolCalls(UncheckedBaseModel):
    phone_number: typing_extensions.Annotated[
        typing.Optional[ServerMessageToolCallsPhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number that the message is associated with.
    """

    type: typing.Optional[typing.Literal["tool-calls"]] = pydantic.Field(default=None)
    """
    This is the type of the message. "tool-calls" is sent to call a tool.
    """

    tool_with_tool_call_list: typing_extensions.Annotated[
        typing.List[ServerMessageToolCallsToolWithToolCallListItem], FieldMetadata(alias="toolWithToolCallList")
    ] = pydantic.Field()
    """
    This is the list of tools calls that the model is requesting along with the original tool configuration.
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the timestamp of the message.
    """

    artifact: typing.Optional[Artifact] = pydantic.Field(default=None)
    """
    This is a live version of the `call.artifact`.
    
    This matches what is stored on `call.artifact` after the call.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that the message is associated with.
    """

    customer: typing.Optional[CreateCustomerDto] = pydantic.Field(default=None)
    """
    This is the customer that the message is associated with.
    """

    call: typing.Optional[Call] = pydantic.Field(default=None)
    """
    This is the call that the message is associated with.
    """

    chat: typing.Optional[Chat] = pydantic.Field(default=None)
    """
    This is the chat object.
    """

    tool_call_list: typing_extensions.Annotated[typing.List[ToolCall], FieldMetadata(alias="toolCallList")] = (
        pydantic.Field()
    )
    """
    This is the list of tool calls that the model is requesting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
