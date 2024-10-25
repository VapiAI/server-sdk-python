# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .create_twilio_phone_number_dto_fallback_destination import CreateTwilioPhoneNumberDtoFallbackDestination
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateTwilioPhoneNumberDto(UniversalBaseModel):
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[CreateTwilioPhoneNumberDtoFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = pydantic.Field(default=None)
    """
    This is the fallback destination an inbound call will be transferred to if:
    
    1. `assistantId` is not set
    2. `squadId` is not set
    3. and, `assistant-request` message to the `serverUrl` fails
    
    If this is not set and above conditions are met, the inbound call is hung up with an error message.
    """

    provider: typing.Literal["twilio"] = "twilio"
    number: str = pydantic.Field()
    """
    These are the digits of the phone number you own on your Twilio.
    """

    twilio_account_sid: typing_extensions.Annotated[str, FieldMetadata(alias="twilioAccountSid")] = pydantic.Field()
    """
    This is the Twilio Account SID for the phone number.
    """

    twilio_auth_token: typing_extensions.Annotated[str, FieldMetadata(alias="twilioAuthToken")] = pydantic.Field()
    """
    This is the Twilio Auth Token for the phone number.
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
