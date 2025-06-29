# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .supabase_bucket_plan import SupabaseBucketPlan


class CreateSupabaseCredentialDto(UncheckedBaseModel):
    provider: typing.Literal["supabase"] = "supabase"
    fallback_index: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="fallbackIndex")] = (
        pydantic.Field(default=None)
    )
    """
    This is the order in which this storage provider is tried during upload retries. Lower numbers are tried first in increasing order.
    """

    bucket_plan: typing_extensions.Annotated[typing.Optional[SupabaseBucketPlan], FieldMetadata(alias="bucketPlan")] = (
        None
    )
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of credential. This is just for your reference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
