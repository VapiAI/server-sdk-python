# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel


class ClientInboundMessageSay(UncheckedBaseModel):
    type: typing.Optional[typing.Literal["say"]] = pydantic.Field(default=None)
    """
    This is the type of the message. Send "say" message to make the assistant say something.
    """

    interrupt_assistant_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="interruptAssistantEnabled")
    ] = pydantic.Field(default=None)
    """
    This is the flag for whether the message should replace existing assistant speech.
    
    @default false
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the content to say.
    """

    end_call_after_spoken: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="endCallAfterSpoken")
    ] = pydantic.Field(default=None)
    """
    This is the flag to end call after content is spoken.
    """

    interruptions_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="interruptionsEnabled")
    ] = pydantic.Field(default=None)
    """
    This is the flag for whether the message is interruptible by the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
