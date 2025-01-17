# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .cartesia_voice_model import CartesiaVoiceModel
from .cartesia_voice_language import CartesiaVoiceLanguage
import typing_extensions
from .chunk_plan import ChunkPlan
from ..core.serialization import FieldMetadata
from .fallback_plan import FallbackPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CartesiaVoice(UniversalBaseModel):
    provider: typing.Literal["cartesia"] = pydantic.Field(default="cartesia")
    """
    This is the voice provider that will be used.
    """

    model: typing.Optional[CartesiaVoiceModel] = pydantic.Field(default=None)
    """
    This is the model that will be used. This is optional and will default to the correct model for the voiceId.
    """

    language: typing.Optional[CartesiaVoiceLanguage] = pydantic.Field(default=None)
    """
    This is the language that will be used. This is optional and will default to the correct language for the voiceId.
    """

    chunk_plan: typing_extensions.Annotated[typing.Optional[ChunkPlan], FieldMetadata(alias="chunkPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for chunking the model output before it is sent to the voice provider.
    """

    voice_id: typing_extensions.Annotated[str, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    This is the provider-specific ID that will be used.
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
