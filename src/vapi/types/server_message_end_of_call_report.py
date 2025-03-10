# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing_extensions
import typing
from .server_message_end_of_call_report_phone_number import ServerMessageEndOfCallReportPhoneNumber
from ..core.serialization import FieldMetadata
import pydantic
from .server_message_end_of_call_report_ended_reason import ServerMessageEndOfCallReportEndedReason
from .server_message_end_of_call_report_costs_item import ServerMessageEndOfCallReportCostsItem
from .artifact import Artifact
from .create_assistant_dto import CreateAssistantDto
from .create_customer_dto import CreateCustomerDto
from .call import Call
from .analysis import Analysis
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ServerMessageEndOfCallReport(UncheckedBaseModel):
    phone_number: typing_extensions.Annotated[
        typing.Optional[ServerMessageEndOfCallReportPhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number associated with the call.
    
    This matches one of the following:
    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    type: typing.Literal["end-of-call-report"] = pydantic.Field(default="end-of-call-report")
    """
    This is the type of the message. "end-of-call-report" is sent when the call ends and post-processing is complete.
    """

    ended_reason: typing_extensions.Annotated[
        ServerMessageEndOfCallReportEndedReason, FieldMetadata(alias="endedReason")
    ] = pydantic.Field()
    """
    This is the reason the call ended. This can also be found at `call.endedReason` on GET /call/:id.
    """

    cost: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the cost of the call in USD. This can also be found at `call.cost` on GET /call/:id.
    """

    costs: typing.Optional[typing.List[ServerMessageEndOfCallReportCostsItem]] = pydantic.Field(default=None)
    """
    These are the costs of individual components of the call in USD. This can also be found at `call.costs` on GET /call/:id.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the ISO-8601 formatted timestamp of when the message was sent.
    """

    artifact: Artifact = pydantic.Field()
    """
    These are the artifacts from the call. This can also be found at `call.artifact` on GET /call/:id.
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

    analysis: Analysis = pydantic.Field()
    """
    This is the analysis of the call. This can also be found at `call.analysis` on GET /call/:id.
    """

    started_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="startedAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ISO 8601 date-time string of when the call started. This can also be found at `call.startedAt` on GET /call/:id.
    """

    ended_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="endedAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ISO 8601 date-time string of when the call ended. This can also be found at `call.endedAt` on GET /call/:id.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
