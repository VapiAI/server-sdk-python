# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing
import pydantic
from .client_message_transfer_update_destination import ClientMessageTransferUpdateDestination
import typing_extensions
from .create_assistant_dto import CreateAssistantDto
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientMessageTransferUpdate(UniversalBaseModel):
    type: typing.Literal["transfer-update"] = pydantic.Field(default="transfer-update")
    """
    This is the type of the message. "transfer-update" is sent whenever a transfer happens.
    """

    destination: typing.Optional[ClientMessageTransferUpdateDestination] = pydantic.Field(default=None)
    """
    This is the destination of the transfer.
    """

    to_assistant: typing_extensions.Annotated[
        typing.Optional[CreateAssistantDto], FieldMetadata(alias="toAssistant")
    ] = pydantic.Field(default=None)
    """
    This is the assistant that the call is being transferred to. This is only sent if `destination.type` is "assistant".
    """

    from_assistant: typing_extensions.Annotated[
        typing.Optional[CreateAssistantDto], FieldMetadata(alias="fromAssistant")
    ] = pydantic.Field(default=None)
    """
    This is the assistant that the call is being transferred from. This is only sent if `destination.type` is "assistant".
    """

    to_step_record: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="toStepRecord")
    ] = pydantic.Field(default=None)
    """
    This is the step that the conversation moved to.
    """

    from_step_record: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="fromStepRecord")
    ] = pydantic.Field(default=None)
    """
    This is the step that the conversation moved from. =
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
