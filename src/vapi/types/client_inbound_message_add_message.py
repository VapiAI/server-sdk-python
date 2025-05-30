# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .open_ai_message import OpenAiMessage


class ClientInboundMessageAddMessage(UncheckedBaseModel):
    type: typing.Literal["add-message"] = pydantic.Field(default="add-message")
    """
    This is the type of the message. Send "add-message" message to add a message to the conversation history.
    """

    message: OpenAiMessage = pydantic.Field()
    """
    This is the message to add to the conversation.
    """

    trigger_response_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="triggerResponseEnabled")
    ] = pydantic.Field(default=None)
    """
    This is the flag to trigger a response, or to insert the message into the conversation history silently. Defaults to `true`.
    
    Usage:
    - Use `true` to trigger a response.
    - Use `false` to insert the message into the conversation history silently.
    
    @default true
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
