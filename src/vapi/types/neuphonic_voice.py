# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .chunk_plan import ChunkPlan
from .fallback_plan import FallbackPlan
from .neuphonic_voice_model import NeuphonicVoiceModel


class NeuphonicVoice(UncheckedBaseModel):
    caching_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="cachingEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    This is the flag to toggle voice caching for the assistant.
    """

    provider: typing.Literal["neuphonic"] = pydantic.Field(default="neuphonic")
    """
    This is the voice provider that will be used.
    """

    voice_id: typing_extensions.Annotated[str, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    This is the provider-specific ID that will be used.
    """

    model: typing.Optional[NeuphonicVoiceModel] = pydantic.Field(default=None)
    """
    This is the model that will be used. Defaults to 'neu_fast' if not specified.
    """

    language: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    This is the language (ISO 639-1) that is enforced for the model.
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
