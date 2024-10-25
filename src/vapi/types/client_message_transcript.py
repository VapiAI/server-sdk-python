# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .client_message_transcript_role import ClientMessageTranscriptRole
import typing_extensions
from .client_message_transcript_transcript_type import ClientMessageTranscriptTranscriptType
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientMessageTranscript(UniversalBaseModel):
    type: typing.Literal["transcript"] = pydantic.Field(default="transcript")
    """
    This is the type of the message. "transcript" is sent as transcriber outputs partial or final transcript.
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
