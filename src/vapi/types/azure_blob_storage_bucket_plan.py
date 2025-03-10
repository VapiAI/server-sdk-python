# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AzureBlobStorageBucketPlan(UncheckedBaseModel):
    connection_string: typing_extensions.Annotated[str, FieldMetadata(alias="connectionString")] = pydantic.Field()
    """
    This is the blob storage connection string for the Azure resource.
    """

    container_name: typing_extensions.Annotated[str, FieldMetadata(alias="containerName")] = pydantic.Field()
    """
    This is the container name for the Azure blob storage.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the path where call artifacts will be stored.
    
    Usage:
    - To store call artifacts in a specific folder, set this to the full path. Eg. "/folder-name1/folder-name2".
    - To store call artifacts in the root of the bucket, leave this blank.
    
    @default "/"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
