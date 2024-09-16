# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateDeepgramCredentialDto(UniversalBaseModel):
    provider: typing.Literal["deepgram"] = "deepgram"
    api_key: typing_extensions.Annotated[str, FieldMetadata(alias="apiKey")] = pydantic.Field()
    """
    This is not returned in the API.
    """

    api_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="apiUrl")] = pydantic.Field(
        default=None
    )
    """
    This can be used to point to an onprem Deepgram instance. Defaults to api.deepgram.com.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow