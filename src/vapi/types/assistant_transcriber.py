# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .deepgram_transcriber_model import DeepgramTranscriberModel
from .deepgram_transcriber_language import DeepgramTranscriberLanguage
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .gladia_transcriber_model import GladiaTranscriberModel
from .gladia_transcriber_language_behaviour import GladiaTranscriberLanguageBehaviour
from .gladia_transcriber_language import GladiaTranscriberLanguage
from .talkscriber_transcriber_language import TalkscriberTranscriberLanguage


class AssistantTranscriber_Deepgram(UniversalBaseModel):
    """
    These are the options for the assistant's transcriber.
    """

    provider: typing.Literal["deepgram"] = "deepgram"
    model: typing.Optional[DeepgramTranscriberModel] = None
    language: typing.Optional[DeepgramTranscriberLanguage] = None
    smart_format: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="smartFormat")] = None
    language_detection_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="languageDetectionEnabled")
    ] = None
    keywords: typing.Optional[typing.List[str]] = None
    endpointing: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssistantTranscriber_Gladia(UniversalBaseModel):
    """
    These are the options for the assistant's transcriber.
    """

    provider: typing.Literal["gladia"] = "gladia"
    model: typing.Optional[GladiaTranscriberModel] = None
    language_behaviour: typing_extensions.Annotated[
        typing.Optional[GladiaTranscriberLanguageBehaviour], FieldMetadata(alias="languageBehaviour")
    ] = None
    language: typing.Optional[GladiaTranscriberLanguage] = None
    transcription_hint: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="transcriptionHint")] = (
        None
    )
    prosody: typing.Optional[bool] = None
    audio_enhancer: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="audioEnhancer")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssistantTranscriber_Talkscriber(UniversalBaseModel):
    """
    These are the options for the assistant's transcriber.
    """

    provider: typing.Literal["talkscriber"] = "talkscriber"
    model: typing.Optional[typing.Literal["whisper"]] = None
    language: typing.Optional[TalkscriberTranscriberLanguage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssistantTranscriber = typing.Union[
    AssistantTranscriber_Deepgram, AssistantTranscriber_Gladia, AssistantTranscriber_Talkscriber
]