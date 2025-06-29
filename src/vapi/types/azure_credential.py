# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .azure_blob_storage_bucket_plan import AzureBlobStorageBucketPlan
from .azure_credential_region import AzureCredentialRegion
from .azure_credential_service import AzureCredentialService


class AzureCredential(UncheckedBaseModel):
    provider: typing.Literal["azure"] = "azure"
    service: AzureCredentialService = pydantic.Field()
    """
    This is the service being used in Azure.
    """

    region: typing.Optional[AzureCredentialRegion] = pydantic.Field(default=None)
    """
    This is the region of the Azure resource.
    """

    api_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="apiKey")] = pydantic.Field(
        default=None
    )
    """
    This is not returned in the API.
    """

    fallback_index: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="fallbackIndex")] = (
        pydantic.Field(default=None)
    )
    """
    This is the order in which this storage provider is tried during upload retries. Lower numbers are tried first in increasing order.
    """

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

    bucket_plan: typing_extensions.Annotated[
        typing.Optional[AzureBlobStorageBucketPlan], FieldMetadata(alias="bucketPlan")
    ] = pydantic.Field(default=None)
    """
    This is the bucket plan that can be provided to store call artifacts in Azure Blob Storage.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
