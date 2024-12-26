# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from .gcp_key import GcpKey
from ..core.serialization import FieldMetadata
import pydantic
from .bucket_plan import BucketPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateGcpCredentialDto(UniversalBaseModel):
    provider: typing.Literal["gcp"] = "gcp"
    gcp_key: typing_extensions.Annotated[GcpKey, FieldMetadata(alias="gcpKey")] = pydantic.Field()
    """
    This is the GCP key. This is the JSON that can be generated in the Google Cloud Console at https://console.cloud.google.com/iam-admin/serviceaccounts/details/<service-account-id>/keys.
    
    The schema is identical to the JSON that GCP outputs.
    """

    bucket_plan: typing_extensions.Annotated[typing.Optional[BucketPlan], FieldMetadata(alias="bucketPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the bucket plan that can be provided to store call artifacts in GCP.
    """

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
