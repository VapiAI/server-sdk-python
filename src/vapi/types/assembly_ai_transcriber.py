# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from .fallback_transcriber_plan import FallbackTranscriberPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AssemblyAiTranscriber(UncheckedBaseModel):
    provider: typing.Literal["assembly-ai"] = pydantic.Field(default="assembly-ai")
    """
    This is the transcription provider that will be used.
    """

    language: typing.Optional[typing.Literal["en"]] = pydantic.Field(default=None)
    """
    This is the language that will be set for the transcription.
    """

    realtime_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="realtimeUrl")] = (
        pydantic.Field(default=None)
    )
    """
    The WebSocket URL that the transcriber connects to.
    """

    word_boost: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="wordBoost")] = (
        pydantic.Field(default=None)
    )
    """
    Add up to 2500 characters of custom vocabulary.
    """

    end_utterance_silence_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="endUtteranceSilenceThreshold")
    ] = pydantic.Field(default=None)
    """
    The duration of the end utterance silence threshold in milliseconds.
    """

    disable_partial_transcripts: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="disablePartialTranscripts")
    ] = pydantic.Field(default=None)
    """
    Disable partial transcripts.
    Set to `true` to not receive partial transcripts. Defaults to `false`.
    """

    fallback_plan: typing_extensions.Annotated[
        typing.Optional[FallbackTranscriberPlan], FieldMetadata(alias="fallbackPlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan for voice provider fallbacks in the event that the primary voice provider fails.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
