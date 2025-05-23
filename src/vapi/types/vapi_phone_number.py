# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .phone_number_hook_call_ringing import PhoneNumberHookCallRinging
from .server import Server
from .sip_authentication import SipAuthentication
from .vapi_phone_number_fallback_destination import VapiPhoneNumberFallbackDestination
from .vapi_phone_number_status import VapiPhoneNumberStatus


class VapiPhoneNumber(UncheckedBaseModel):
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[VapiPhoneNumberFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = pydantic.Field(default=None)
    """
    This is the fallback destination an inbound call will be transferred to if:
    1. `assistantId` is not set
    2. `squadId` is not set
    3. and, `assistant-request` message to the `serverUrl` fails
    
    If this is not set and above conditions are met, the inbound call is hung up with an error message.
    """

    hooks: typing.Optional[typing.List[PhoneNumberHookCallRinging]] = pydantic.Field(default=None)
    """
    This is the hooks that will be used for incoming calls to this phone number.
    """

    provider: typing.Literal["vapi"] = "vapi"
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

    status: typing.Optional[VapiPhoneNumberStatus] = pydantic.Field(default=None)
    """
    This is the status of the phone number.
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    These are the digits of the phone number you purchased from Vapi.
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
    
    If neither `assistantId`, `squadId` nor `workflowId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    """

    workflow_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="workflowId")] = pydantic.Field(
        default=None
    )
    """
    This is the workflow that will be used for incoming calls to this phone number.
    
    If neither `assistantId`, `squadId`, nor `workflowId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    """

    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = pydantic.Field(
        default=None
    )
    """
    This is the squad that will be used for incoming calls to this phone number.
    
    If neither `assistantId`, `squadId`, nor `workflowId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    """

    server: typing.Optional[Server] = pydantic.Field(default=None)
    """
    This is where Vapi will send webhooks. You can find all webhooks available along with their shape in ServerMessage schema.
    
    The order of precedence is:
    
    1. assistant.server
    2. phoneNumber.server
    3. org.server
    """

    number_desired_area_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="numberDesiredAreaCode")
    ] = pydantic.Field(default=None)
    """
    This is the area code of the phone number to purchase.
    """

    sip_uri: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="sipUri")] = pydantic.Field(
        default=None
    )
    """
    This is the SIP URI of the phone number. You can SIP INVITE this. The assistant attached to this number will answer.
    
    This is case-insensitive.
    """

    authentication: typing.Optional[SipAuthentication] = pydantic.Field(default=None)
    """
    This enables authentication for incoming SIP INVITE requests to the `sipUri`.
    
    If not set, any username/password to the 401 challenge of the SIP INVITE will be accepted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
