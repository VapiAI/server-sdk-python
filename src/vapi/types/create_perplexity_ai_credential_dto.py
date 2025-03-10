# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreatePerplexityAiCredentialDto(UncheckedBaseModel):
    provider: typing.Literal["perplexity-ai"] = "perplexity-ai"
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey")] = pydantic.Field()
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
