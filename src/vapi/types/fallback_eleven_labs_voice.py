# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .chunk_plan import ChunkPlan
from .fallback_eleven_labs_voice_id import FallbackElevenLabsVoiceId
from .fallback_eleven_labs_voice_model import FallbackElevenLabsVoiceModel


class FallbackElevenLabsVoice(UncheckedBaseModel):
    caching_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="cachingEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    This is the flag to toggle voice caching for the assistant.
    """

    provider: typing.Literal["11labs"] = pydantic.Field(default="11labs")
    """
    This is the voice provider that will be used.
    """

    voice_id: typing_extensions.Annotated[FallbackElevenLabsVoiceId, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    This is the provider-specific ID that will be used. Ensure the Voice is present in your 11Labs Voice Library.
    """

    stability: typing.Optional[float] = pydantic.Field(default=None)
    """
    Defines the stability for voice settings.
    """

    similarity_boost: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="similarityBoost")] = (
        pydantic.Field(default=None)
    )
    """
    Defines the similarity boost for voice settings.
    """

    style: typing.Optional[float] = pydantic.Field(default=None)
    """
    Defines the style for voice settings.
    """

    use_speaker_boost: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="useSpeakerBoost")] = (
        pydantic.Field(default=None)
    )
    """
    Defines the use speaker boost for voice settings.
    """

    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    Defines the speed for voice settings.
    """

    optimize_streaming_latency: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="optimizeStreamingLatency")
    ] = pydantic.Field(default=None)
    """
    Defines the optimize streaming latency for voice settings. Defaults to 3.
    """

    enable_ssml_parsing: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableSsmlParsing")
    ] = pydantic.Field(default=None)
    """
    This enables the use of https://elevenlabs.io/docs/speech-synthesis/prompting#pronunciation. Defaults to false to save latency.
    
    @default false
    """

    auto_mode: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="autoMode")] = pydantic.Field(
        default=None
    )
    """
    Defines the auto mode for voice settings. Defaults to false.
    """

    model: typing.Optional[FallbackElevenLabsVoiceModel] = pydantic.Field(default=None)
    """
    This is the model that will be used. Defaults to 'eleven_turbo_v2' if not specified.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the language (ISO 639-1) that is enforced for the model. Currently only Turbo v2.5 supports language enforcement. For other models, an error will be returned if language code is provided.
    """

    chunk_plan: typing_extensions.Annotated[typing.Optional[ChunkPlan], FieldMetadata(alias="chunkPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for chunking the model output before it is sent to the voice provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
