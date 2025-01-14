# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing
from .update_workflow_block_dto_messages_item import UpdateWorkflowBlockDtoMessagesItem
import pydantic
import typing_extensions
from .json_schema import JsonSchema
from ..core.serialization import FieldMetadata
from .update_workflow_block_dto_steps_item import UpdateWorkflowBlockDtoStepsItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class UpdateWorkflowBlockDto(UniversalBaseModel):
    messages: typing.Optional[typing.List[UpdateWorkflowBlockDtoMessagesItem]] = pydantic.Field(default=None)
    """
    These are the pre-configured messages that will be spoken to the user while the block is running.
    """

    input_schema: typing_extensions.Annotated[typing.Optional[JsonSchema], FieldMetadata(alias="inputSchema")] = (
        pydantic.Field(default=None)
    )
    """
    This is the input schema for the block. This is the input the block needs to run. It's given to the block as `steps[0].input`
    
    These are accessible as variables:
    - ({{input.propertyName}}) in context of the block execution (step)
    - ({{stepName.input.propertyName}}) in context of the workflow
    """

    output_schema: typing_extensions.Annotated[typing.Optional[JsonSchema], FieldMetadata(alias="outputSchema")] = (
        pydantic.Field(default=None)
    )
    """
    This is the output schema for the block. This is the output the block will return to the workflow (`{{stepName.output}}`).
    
    These are accessible as variables:
    - ({{output.propertyName}}) in context of the block execution (step)
    - ({{stepName.output.propertyName}}) in context of the workflow (read caveat #1)
    - ({{blockName.output.propertyName}}) in context of the workflow (read caveat #2)
    
    Caveats:
    1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output.propertyName}} will reference the latest usage of the step.
    2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.
    """

    steps: typing.Optional[typing.List[UpdateWorkflowBlockDtoStepsItem]] = pydantic.Field(default=None)
    """
    These are the steps in the workflow.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the block. This is just for your reference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CallbackStep, UpdateWorkflowBlockDto=UpdateWorkflowBlockDto)
update_forward_refs(CreateWorkflowBlockDto, UpdateWorkflowBlockDto=UpdateWorkflowBlockDto)
update_forward_refs(HandoffStep, UpdateWorkflowBlockDto=UpdateWorkflowBlockDto)