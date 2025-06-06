# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .call import Call
from .client_message_voice_input_phone_number import ClientMessageVoiceInputPhoneNumber
from .create_assistant_dto import CreateAssistantDto
from .create_customer_dto import CreateCustomerDto


class ClientMessageVoiceInput(UncheckedBaseModel):
    phone_number: typing_extensions.Annotated[
        typing.Optional[ClientMessageVoiceInputPhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number that the message is associated with.
    """

    type: typing.Literal["voice-input"] = pydantic.Field(default="voice-input")
    """
    This is the type of the message. "voice-input" is sent when a generation is requested from voice provider.
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the timestamp of the message.
    """

    call: typing.Optional[Call] = pydantic.Field(default=None)
    """
    This is the call that the message is associated with.
    """

    customer: typing.Optional[CreateCustomerDto] = pydantic.Field(default=None)
    """
    This is the customer that the message is associated with.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that the message is associated with.
    """

    input: str = pydantic.Field()
    """
    This is the voice input content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
