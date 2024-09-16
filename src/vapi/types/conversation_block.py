# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .conversation_block_messages_item import ConversationBlockMessagesItem
import pydantic
import typing_extensions
from .json_schema import JsonSchema
from ..core.serialization import FieldMetadata
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ConversationBlock(UniversalBaseModel):
    messages: typing.Optional[typing.List[ConversationBlockMessagesItem]] = pydantic.Field(default=None)
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

    id: str = pydantic.Field()
    """
    This is the unique identifier for the block.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the organization that this block belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the block was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the block was last updated.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the block. This is just for your reference.
    """

    instruction: str = pydantic.Field()
    """
    This is the instruction to the model.
    
    You can reference any variable in the context of the current block execution (step):
    
    - "{{input.your-property-name}}" for the current step's input
    - "{{your-step-name.output.your-property-name}}" for another step's output (in the same workflow; read caveat #1)
    - "{{your-step-name.input.your-property-name}}" for another step's input (in the same workflow; read caveat #1)
    - "{{your-block-name.output.your-property-name}}" for another block's output (in the same workflow; read caveat #2)
    - "{{your-block-name.input.your-property-name}}" for another block's input (in the same workflow; read caveat #2)
    - "{{workflow.input.your-property-name}}" for the current workflow's input
    - "{{global.your-property-name}}" for the global context
    
    This can be as simple or as complex as you want it to be.
    
    - "say hello and ask the user about their day!"
    - "collect the user's first and last name"
    - "user is {{input.firstName}} {{input.lastName}}. their age is {{input.age}}. ask them about their salary and if they might be interested in buying a house. we offer {{input.offer}}"
    
    Caveats:
    
    1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output/input.propertyName}} will reference the latest usage of the step.
    2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output/input.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow