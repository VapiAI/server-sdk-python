# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .create_azure_credential_dto_service import CreateAzureCredentialDtoService
import pydantic
from .create_azure_credential_dto_region import CreateAzureCredentialDtoRegion
import typing_extensions
from ..core.serialization import FieldMetadata
from .azure_blob_storage_bucket_plan import AzureBlobStorageBucketPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateAzureCredentialDto(UncheckedBaseModel):
    provider: typing.Literal["azure"] = "azure"
    service: CreateAzureCredentialDtoService = pydantic.Field()
    """
    This is the service being used in Azure.
    """

    region: typing.Optional[CreateAzureCredentialDtoRegion] = pydantic.Field(default=None)
    """
    This is the region of the Azure resource.
    """

    api_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="apiKey")] = pydantic.Field(
        default=None
    )
    """
    This is not returned in the API.
    """

    bucket_plan: typing_extensions.Annotated[
        typing.Optional[AzureBlobStorageBucketPlan], FieldMetadata(alias="bucketPlan")
    ] = pydantic.Field(default=None)
    """
    This is the bucket plan that can be provided to store call artifacts in Azure Blob Storage.
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
