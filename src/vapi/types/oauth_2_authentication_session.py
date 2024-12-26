# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Oauth2AuthenticationSession(UniversalBaseModel):
    access_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="accessToken")] = (
        pydantic.Field(default=None)
    )
    """
    This is the OAuth2 access token.
    """

    expires_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the OAuth2 access token expiration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
