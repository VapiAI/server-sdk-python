# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .byo_phone_number_fallback_destination import ByoPhoneNumberFallbackDestination
from ..core.serialization import FieldMetadata
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ByoPhoneNumber(UniversalBaseModel):
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[ByoPhoneNumberFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = pydantic.Field(default=None)
    """
    This is the fallback destination an inbound call will be transferred to if:
    
    1. `assistantId` is not set
    2. `squadId` is not set
    3. and, `assistant-request` message to the `serverUrl` fails
    
    If this is not set and above conditions are met, the inbound call is hung up with an error message.
    """

    number_e_164_check_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="numberE164CheckEnabled")
    ] = pydantic.Field(default=None)
    """
    This is the flag to toggle the E164 check for the `number` field. This is an advanced property which should be used if you know your use case requires it.
    
    Use cases:
    
    - `false`: To allow non-E164 numbers like `+001234567890`, `1234`, or `abc`. This is useful for dialing out to non-E164 numbers on your SIP trunks.
    - `true` (default): To allow only E164 numbers like `+14155551234`. This is standard for PSTN calls.
    
    If `false`, the `number` is still required to only contain alphanumeric characters (regex: `/^\+?[a-zA-Z0-9]+$/`).
    
    @default true (E164 check is enabled)
    """

    id: str = pydantic.Field()
    """
    This is the unique identifier for the phone number.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this phone number belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the phone number was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the phone number was last updated.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the phone number. This is just for your own reference.
    """

    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the assistant that will be used for incoming calls to this phone number.
    
    If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    """

    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = pydantic.Field(
        default=None
    )
    """
    This is the squad that will be used for incoming calls to this phone number.
    
    If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    """

    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = pydantic.Field(
        default=None
    )
    """
    This is the server URL where messages will be sent for calls on this number. This includes the `assistant-request` message.
    
    You can see the shape of the messages sent in `ServerMessage`.
    
    This overrides the `org.serverUrl`. Order of precedence: tool.server.url > assistant.serverUrl > phoneNumber.serverUrl > org.serverUrl.
    """

    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = (
        pydantic.Field(default=None)
    )
    """
    This is the secret Vapi will send with every message to your server. It's sent as a header called x-vapi-secret.
    
    Same precedence logic as serverUrl.
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the number of the customer.
    """

    credential_id: typing_extensions.Annotated[str, FieldMetadata(alias="credentialId")] = pydantic.Field()
    """
    This is the credential of your own SIP trunk or Carrier (type `byo-sip-trunk`) which can be used to make calls to this phone number.
    
    You can add the SIP trunk or Carrier credential in the Provider Credentials page on the Dashboard to get the credentialId.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow