# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing_extensions
import typing
from .server_message_hang_phone_number import ServerMessageHangPhoneNumber
from ..core.serialization import FieldMetadata
import pydantic
from .artifact import Artifact
from .create_assistant_dto import CreateAssistantDto
from .create_customer_dto import CreateCustomerDto
from .call import Call
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ServerMessageHang(UniversalBaseModel):
    phone_number: typing_extensions.Annotated[
        typing.Optional[ServerMessageHangPhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number associated with the call.
    
    This matches one of the following:
    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    type: typing.Literal["hang"] = pydantic.Field(default="hang")
    """
    This is the type of the message. "hang" is sent when the assistant is hanging due to a delay. The delay can be caused by many factors, such as:
    - the model is too slow to respond
    - the voice is too slow to respond
    - the tool call is still waiting for a response from your server
    - etc.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the ISO-8601 formatted timestamp of when the message was sent.
    """

    artifact: typing.Optional[Artifact] = pydantic.Field(default=None)
    """
    This is a live version of the `call.artifact`.
    
    This matches what is stored on `call.artifact` after the call.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that is currently active. This is provided for convenience.
    
    This matches one of the following:
    - `call.assistant`,
    - `call.assistantId`,
    - `call.squad[n].assistant`,
    - `call.squad[n].assistantId`,
    - `call.squadId->[n].assistant`,
    - `call.squadId->[n].assistantId`.
    """

    customer: typing.Optional[CreateCustomerDto] = pydantic.Field(default=None)
    """
    This is the customer associated with the call.
    
    This matches one of the following:
    - `call.customer`,
    - `call.customerId`.
    """

    call: typing.Optional[Call] = pydantic.Field(default=None)
    """
    This is the call object.
    
    This matches what was returned in POST /call.
    
    Note: This might get stale during the call. To get the latest call object, especially after the call is ended, use GET /call/:id.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
