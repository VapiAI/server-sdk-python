# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .cartesia_experimental_controls import CartesiaExperimentalControls
from .cartesia_voice_language import CartesiaVoiceLanguage
from .cartesia_voice_model import CartesiaVoiceModel
from .chunk_plan import ChunkPlan
from .fallback_plan import FallbackPlan


class CartesiaVoice(UncheckedBaseModel):
    caching_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="cachingEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    This is the flag to toggle voice caching for the assistant.
    """

    provider: typing.Literal["cartesia"] = pydantic.Field(default="cartesia")
    """
    This is the voice provider that will be used.
    """

    voice_id: typing_extensions.Annotated[str, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    The ID of the particular voice you want to use.
    """

    model: typing.Optional[CartesiaVoiceModel] = pydantic.Field(default=None)
    """
    This is the model that will be used. This is optional and will default to the correct model for the voiceId.
    """

    language: typing.Optional[CartesiaVoiceLanguage] = pydantic.Field(default=None)
    """
    This is the language that will be used. This is optional and will default to the correct language for the voiceId.
    """

    experimental_controls: typing_extensions.Annotated[
        typing.Optional[CartesiaExperimentalControls], FieldMetadata(alias="experimentalControls")
    ] = pydantic.Field(default=None)
    """
    Experimental controls for Cartesia voice generation
    """

    chunk_plan: typing_extensions.Annotated[typing.Optional[ChunkPlan], FieldMetadata(alias="chunkPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for chunking the model output before it is sent to the voice provider.
    """

    fallback_plan: typing_extensions.Annotated[typing.Optional[FallbackPlan], FieldMetadata(alias="fallbackPlan")] = (
        pydantic.Field(default=None)
    )
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
