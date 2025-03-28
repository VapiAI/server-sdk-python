# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .fallback_gladia_transcriber_model import FallbackGladiaTranscriberModel
import typing_extensions
from .fallback_gladia_transcriber_language_behaviour import FallbackGladiaTranscriberLanguageBehaviour
from ..core.serialization import FieldMetadata
from .fallback_gladia_transcriber_language import FallbackGladiaTranscriberLanguage
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackGladiaTranscriber(UncheckedBaseModel):
    provider: typing.Literal["gladia"] = pydantic.Field(default="gladia")
    """
    This is the transcription provider that will be used.
    """

    model: typing.Optional[FallbackGladiaTranscriberModel] = None
    language_behaviour: typing_extensions.Annotated[
        typing.Optional[FallbackGladiaTranscriberLanguageBehaviour], FieldMetadata(alias="languageBehaviour")
    ] = None
    language: typing.Optional[FallbackGladiaTranscriberLanguage] = pydantic.Field(default=None)
    """
    Defines the language to use for the transcription. Required when languageBehaviour is 'manual'.
    """

    transcription_hint: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="transcriptionHint")] = (
        pydantic.Field(default=None)
    )
    """
    Provides a custom vocabulary to the model to improve accuracy of transcribing context specific words, technical terms, names, etc. If empty, this argument is ignored.
    ⚠️ Warning ⚠️: Please be aware that the transcription_hint field has a character limit of 600. If you provide a transcription_hint longer than 600 characters, it will be automatically truncated to meet this limit.
    """

    prosody: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If prosody is true, you will get a transcription that can contain prosodies i.e. (laugh) (giggles) (malefic laugh) (toss) (music)… Default value is false.
    """

    audio_enhancer: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="audioEnhancer")] = (
        pydantic.Field(default=None)
    )
    """
    If true, audio will be pre-processed to improve accuracy but latency will increase. Default value is false.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
