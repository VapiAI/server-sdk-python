# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .call import Call
from .client_message_transcript_phone_number import ClientMessageTranscriptPhoneNumber
from .client_message_transcript_role import ClientMessageTranscriptRole
from .client_message_transcript_transcript_type import ClientMessageTranscriptTranscriptType
from .client_message_transcript_type import ClientMessageTranscriptType
from .create_assistant_dto import CreateAssistantDto
from .create_customer_dto import CreateCustomerDto


class ClientMessageTranscript(UncheckedBaseModel):
    phone_number: typing_extensions.Annotated[
        typing.Optional[ClientMessageTranscriptPhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number that the message is associated with.
    """

    type: ClientMessageTranscriptType = pydantic.Field()
    """
    This is the type of the message. "transcript" is sent as transcriber outputs partial or final transcript.
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

    role: ClientMessageTranscriptRole = pydantic.Field()
    """
    This is the role for which the transcript is for.
    """

    transcript_type: typing_extensions.Annotated[
        ClientMessageTranscriptTranscriptType, FieldMetadata(alias="transcriptType")
    ] = pydantic.Field()
    """
    This is the type of the transcript.
    """

    transcript: str = pydantic.Field()
    """
    This is the transcript content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
