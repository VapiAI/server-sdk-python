# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
from .gcp_key import GcpKey
from .bucket_plan import BucketPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GcpCredential(UncheckedBaseModel):
    provider: typing.Literal["gcp"] = "gcp"
    id: str = pydantic.Field()
    """
    This is the unique identifier for the credential.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this credential belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the credential was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the assistant was last updated.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of credential. This is just for your reference.
    """

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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
