# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .fallback_cartesia_voice_model import FallbackCartesiaVoiceModel
from .fallback_cartesia_voice_language import FallbackCartesiaVoiceLanguage
from .cartesia_experimental_controls import CartesiaExperimentalControls
from .chunk_plan import ChunkPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackCartesiaVoice(UncheckedBaseModel):
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

    model: typing.Optional[FallbackCartesiaVoiceModel] = pydantic.Field(default=None)
    """
    This is the model that will be used. This is optional and will default to the correct model for the voiceId.
    """

    language: typing.Optional[FallbackCartesiaVoiceLanguage] = pydantic.Field(default=None)
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
