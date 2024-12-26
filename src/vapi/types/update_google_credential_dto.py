# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateGoogleCredentialDto(UniversalBaseModel):
    provider: typing.Literal["google"] = pydantic.Field(default="google")
    """
    This is the key for Gemini in Google AI Studio. Get it from here: https://aistudio.google.com/app/apikey
    """

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
