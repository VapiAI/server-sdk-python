# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import typing
from .import_vonage_phone_number_dto_fallback_destination import ImportVonagePhoneNumberDtoFallbackDestination
from ..core.serialization import FieldMetadata
import pydantic
from .server import Server
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ImportVonagePhoneNumberDto(UncheckedBaseModel):
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[ImportVonagePhoneNumberDtoFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = pydantic.Field(default=None)
    """
    This is the fallback destination an inbound call will be transferred to if:
    1. `assistantId` is not set
    2. `squadId` is not set
    3. and, `assistant-request` message to the `serverUrl` fails
    
    If this is not set and above conditions are met, the inbound call is hung up with an error message.
    """

    vonage_phone_number: typing_extensions.Annotated[str, FieldMetadata(alias="vonagePhoneNumber")] = pydantic.Field()
    """
    These are the digits of the phone number you own on your Vonage.
    """

    credential_id: typing_extensions.Annotated[str, FieldMetadata(alias="credentialId")] = pydantic.Field()
    """
    This is the credential you added in dashboard.vapi.ai/keys. This is used to configure the number to send inbound calls to Vapi, make outbound calls and do live call updates like transfers and hangups.
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

    server: typing.Optional[Server] = pydantic.Field(default=None)
    """
    This is where Vapi will send webhooks. You can find all webhooks available along with their shape in ServerMessage schema.
    
    The order of precedence is:
    
    1. assistant.server
    2. phoneNumber.server
    3. org.server
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
