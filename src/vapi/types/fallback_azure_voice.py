# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from .fallback_azure_voice_id import FallbackAzureVoiceId
from ..core.serialization import FieldMetadata
from .chunk_plan import ChunkPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackAzureVoice(UncheckedBaseModel):
    provider: typing.Literal["azure"] = pydantic.Field(default="azure")
    """
    This is the voice provider that will be used.
    """

    voice_id: typing_extensions.Annotated[FallbackAzureVoiceId, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    This is the provider-specific ID that will be used.
    """

    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the speed multiplier that will be used.
    """

    chunk_plan: typing_extensions.Annotated[typing.Optional[ChunkPlan], FieldMetadata(alias="chunkPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for chunking the model output before it is sent to the voice provider.
    """

    one_of: typing_extensions.Annotated[typing.Optional[typing.Optional[typing.Any]], FieldMetadata(alias="oneOf")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
