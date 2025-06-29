# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .fallback_transcriber_plan import FallbackTranscriberPlan


class AssemblyAiTranscriber(UncheckedBaseModel):
    provider: typing.Literal["assembly-ai"] = pydantic.Field(default="assembly-ai")
    """
    This is the transcription provider that will be used.
    """

    language: typing.Optional[typing.Literal["en"]] = pydantic.Field(default=None)
    """
    This is the language that will be set for the transcription.
    """

    confidence_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="confidenceThreshold")
    ] = pydantic.Field(default=None)
    """
    Transcripts below this confidence threshold will be discarded.
    
    @default 0.4
    """

    enable_universal_streaming_api: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableUniversalStreamingApi")
    ] = pydantic.Field(default=None)
    """
    Uses Assembly AI's new Universal Streaming API. See: https://www.assemblyai.com/docs/speech-to-text/universal-streaming
    
    @default false
    """

    format_turns: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="formatTurns")] = (
        pydantic.Field(default=None)
    )
    """
    This enables formatting of transcripts. Only used when `enableUniversalStreamingApi` is true.
    
    @default false
    """

    end_of_turn_confidence_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="endOfTurnConfidenceThreshold")
    ] = pydantic.Field(default=None)
    """
    The confidence threshold to use when determining if the end of a turn has been reached. Only used when `enableUniversalStreamingApi` is true.
    
    @default 0.7
    """

    min_end_of_turn_silence_when_confident: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minEndOfTurnSilenceWhenConfident")
    ] = pydantic.Field(default=None)
    """
    The minimum amount of silence in milliseconds required to detect end of turn when confident. Only used when `enableUniversalStreamingApi` is true.
    
    @default 160
    """

    word_finalization_max_wait_time: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="wordFinalizationMaxWaitTime")
    ] = pydantic.Field(default=None)
    """
    The maximum wait time for word finalization. Only used when `enableUniversalStreamingApi` is true.
    
    @default 160
    """

    max_turn_silence: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="maxTurnSilence")] = (
        pydantic.Field(default=None)
    )
    """
    The maximum amount of silence in milliseconds allowed in a turn before end of turn is triggered. Only used when `enableUniversalStreamingApi` is true.
    
    @default 400
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
