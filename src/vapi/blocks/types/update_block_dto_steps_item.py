# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...types.step_destination import StepDestination
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ...types.assignment_mutation import AssignmentMutation
from ...core.pydantic_utilities import update_forward_refs


class UpdateBlockDtoStepsItem_Handoff(UniversalBaseModel):
    type: typing.Literal["handoff"] = "handoff"
    block: typing.Optional["HandoffStepBlock"] = None
    destinations: typing.Optional[typing.List[StepDestination]] = None
    name: str
    block_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="blockId")] = None
    input: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from ...types.handoff_step_block import HandoffStepBlock  # noqa: E402


class UpdateBlockDtoStepsItem_Callback(UniversalBaseModel):
    type: typing.Literal["callback"] = "callback"
    block: typing.Optional["CallbackStepBlock"] = None
    mutations: typing.Optional[typing.List[AssignmentMutation]] = None
    name: str
    block_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="blockId")] = None
    input: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from ...types.callback_step import CallbackStep  # noqa: E402
from ...types.create_workflow_block_dto import CreateWorkflowBlockDto  # noqa: E402
from ...types.handoff_step import HandoffStep  # noqa: E402
from ...types.callback_step_block import CallbackStepBlock  # noqa: E402

UpdateBlockDtoStepsItem = typing.Union[UpdateBlockDtoStepsItem_Handoff, UpdateBlockDtoStepsItem_Callback]
update_forward_refs(CallbackStep, UpdateBlockDtoStepsItem_Handoff=UpdateBlockDtoStepsItem_Handoff)
update_forward_refs(CreateWorkflowBlockDto, UpdateBlockDtoStepsItem_Handoff=UpdateBlockDtoStepsItem_Handoff)
update_forward_refs(HandoffStep, UpdateBlockDtoStepsItem_Handoff=UpdateBlockDtoStepsItem_Handoff)
update_forward_refs(UpdateBlockDtoStepsItem_Handoff)
update_forward_refs(CallbackStep, UpdateBlockDtoStepsItem_Callback=UpdateBlockDtoStepsItem_Callback)
update_forward_refs(CreateWorkflowBlockDto, UpdateBlockDtoStepsItem_Callback=UpdateBlockDtoStepsItem_Callback)
update_forward_refs(HandoffStep, UpdateBlockDtoStepsItem_Callback=UpdateBlockDtoStepsItem_Callback)
update_forward_refs(UpdateBlockDtoStepsItem_Callback)