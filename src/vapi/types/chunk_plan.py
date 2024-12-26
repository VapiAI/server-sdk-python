# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from .punctuation_boundary import PunctuationBoundary
from .format_plan import FormatPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ChunkPlan(UniversalBaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This determines whether the model output is chunked before being sent to the voice provider. Default `true`.
    
    Usage:
    - To rely on the voice provider's audio generation logic, set this to `false`.
    - If seeing issues with quality, set this to `true`.
    
    If disabled, Vapi-provided audio control tokens like <flush /> will not work.
    
    @default true
    """

    min_characters: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="minCharacters")] = (
        pydantic.Field(default=None)
    )
    """
    This is the minimum number of characters in a chunk.
    
    Usage:
    - To increase quality, set this to a higher value.
    - To decrease latency, set this to a lower value.
    
    @default 30
    """

    punctuation_boundaries: typing_extensions.Annotated[
        typing.Optional[typing.List[PunctuationBoundary]], FieldMetadata(alias="punctuationBoundaries")
    ] = pydantic.Field(default=None)
    """
    These are the punctuations that are considered valid boundaries for a chunk to be created.
    
    Usage:
    - To increase quality, constrain to fewer boundaries.
    - To decrease latency, enable all.
    
    Default is automatically set to balance the trade-off between quality and latency based on the provider.
    """

    format_plan: typing_extensions.Annotated[typing.Optional[FormatPlan], FieldMetadata(alias="formatPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for formatting the chunk before it is sent to the voice provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
