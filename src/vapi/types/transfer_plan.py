# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .transfer_plan_mode import TransferPlanMode
import pydantic
import typing
from .transfer_plan_message import TransferPlanMessage
import typing_extensions
from ..core.serialization import FieldMetadata
from .summary_plan import SummaryPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TransferPlan(UniversalBaseModel):
    mode: TransferPlanMode = pydantic.Field()
    """
    This configures how transfer is executed and the experience of the destination party receiving the call.
    
    Usage:
    - `blind-transfer`: The assistant forwards the call to the destination without any message or summary.
    - `blind-transfer-add-summary-to-sip-header`: The assistant forwards the call to the destination and adds a SIP header X-Transfer-Summary to the call to include the summary.
    - `warm-transfer-say-message`: The assistant dials the destination, delivers the `message` to the destination party, connects the customer, and leaves the call.
    - `warm-transfer-say-summary`: The assistant dials the destination, provides a summary of the call to the destination party, connects the customer, and leaves the call.
    - `warm-transfer-wait-for-operator-to-speak-first-and-then-say-message`: The assistant dials the destination, waits for the operator to speak, delivers the `message` to the destination party, and then connects the customer.
    - `warm-transfer-wait-for-operator-to-speak-first-and-then-say-summary`: The assistant dials the destination, waits for the operator to speak, provides a summary of the call to the destination party, and then connects the customer.
    - `warm-transfer-twiml`: The assistant dials the destination, executes the twiml instructions on the destination call leg, connects the customer, and leaves the call.
    
    @default 'blind-transfer'
    """

    message: typing.Optional[TransferPlanMessage] = pydantic.Field(default=None)
    """
    This is the message the assistant will deliver to the destination party before connecting the customer.
    
    Usage:
    - Used only when `mode` is `blind-transfer-add-summary-to-sip-header`, `warm-transfer-say-message` or `warm-transfer-wait-for-operator-to-speak-first-and-then-say-message`.
    """

    sip_verb: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="sipVerb")
    ] = pydantic.Field(default=None)
    """
    This specifies the SIP verb to use while transferring the call.
    - 'refer': Uses SIP REFER to transfer the call (default)
    - 'bye': Ends current call with SIP BYE
    - 'dial': Uses SIP DIAL to transfer the call
    """

    twiml: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the TwiML instructions to execute on the destination call leg before connecting the customer.
    
    Usage:
    - Used only when `mode` is `warm-transfer-twiml`.
    - Supports only `Play`, `Say`, `Gather`, `Hangup` and `Pause` verbs.
    - Maximum length is 4096 characters.
    
    Example:
    ```
    <Say voice="alice" language="en-US">Hello, transferring a customer to you.</Say>
    <Pause length="2"/>
    <Say>They called about billing questions.</Say>
    ```
    """

    summary_plan: typing_extensions.Annotated[typing.Optional[SummaryPlan], FieldMetadata(alias="summaryPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for generating a summary of the call to present to the destination party.
    
    Usage:
    - Used only when `mode` is `blind-transfer-add-summary-to-sip-header` or `warm-transfer-say-summary` or `warm-transfer-wait-for-operator-to-speak-first-and-then-say-summary`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
