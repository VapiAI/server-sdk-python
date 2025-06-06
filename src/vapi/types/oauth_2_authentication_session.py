# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel


class Oauth2AuthenticationSession(UncheckedBaseModel):
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

    refresh_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="refreshToken")] = (
        pydantic.Field(default=None)
    )
    """
    This is the OAuth2 refresh token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
