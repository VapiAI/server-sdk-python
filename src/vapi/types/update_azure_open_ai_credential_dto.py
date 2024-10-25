# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .update_azure_open_ai_credential_dto_region import UpdateAzureOpenAiCredentialDtoRegion
from .update_azure_open_ai_credential_dto_models_item import UpdateAzureOpenAiCredentialDtoModelsItem
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateAzureOpenAiCredentialDto(UniversalBaseModel):
    provider: typing.Literal["azure-openai"] = "azure-openai"
    region: UpdateAzureOpenAiCredentialDtoRegion
    models: typing.List[UpdateAzureOpenAiCredentialDtoModelsItem]
    open_ai_key: typing_extensions.Annotated[str, FieldMetadata(alias="openAIKey")] = pydantic.Field()
    """
    This is not returned in the API.
    """

    open_ai_endpoint: typing_extensions.Annotated[str, FieldMetadata(alias="openAIEndpoint")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
