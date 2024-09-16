# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .open_ai_message import OpenAiMessage
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .client_inbound_message_control_control import ClientInboundMessageControlControl
import typing_extensions
from ..core.serialization import FieldMetadata


class ClientInboundMessageMessage_AddMessage(UniversalBaseModel):
    """
    These are the messages that can be sent from client-side SDKs to control the call.
    """

    type: typing.Literal["add-message"] = "add-message"
    message: OpenAiMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ClientInboundMessageMessage_Control(UniversalBaseModel):
    """
    These are the messages that can be sent from client-side SDKs to control the call.
    """

    type: typing.Literal["control"] = "control"
    control: ClientInboundMessageControlControl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ClientInboundMessageMessage_Say(UniversalBaseModel):
    """
    These are the messages that can be sent from client-side SDKs to control the call.
    """

    type: typing.Literal["say"] = "say"
    content: typing.Optional[str] = None
    end_call_after_spoken: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="endCallAfterSpoken")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ClientInboundMessageMessage = typing.Union[
    ClientInboundMessageMessage_AddMessage, ClientInboundMessageMessage_Control, ClientInboundMessageMessage_Say
]