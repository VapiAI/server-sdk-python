# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .update_azure_credential_dto_region import UpdateAzureCredentialDtoRegion
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateAzureCredentialDto(UniversalBaseModel):
    provider: typing.Literal["azure"] = "azure"
    service: typing.Literal["speech"] = pydantic.Field(default="speech")
    """
    This is the service being used in Azure.
    """

    region: typing.Optional[UpdateAzureCredentialDtoRegion] = pydantic.Field(default=None)
    """
    This is the region of the Azure resource.
    """

    api_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="apiKey")] = pydantic.Field(
        default=None
    )
    """
    This is not returned in the API.
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
