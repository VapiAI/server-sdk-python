# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .deepgram_voice_voice_id import DeepgramVoiceVoiceId
from .chunk_plan import ChunkPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DeepgramVoice(UniversalBaseModel):
    filler_injection_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fillerInjectionEnabled")
    ] = pydantic.Field(default=None)
    """
    This determines whether fillers are injected into the model output before inputting it into the voice provider.
    
    Default `false` because you can achieve better results with prompting the model.
    """

    provider: typing.Literal["deepgram"] = pydantic.Field(default="deepgram")
    """
    This is the voice provider that will be used.
    """

    voice_id: typing_extensions.Annotated[DeepgramVoiceVoiceId, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    This is the provider-specific ID that will be used.
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
