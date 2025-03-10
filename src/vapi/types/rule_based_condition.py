# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .rule_based_condition_operator import RuleBasedConditionOperator
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class RuleBasedCondition(UncheckedBaseModel):
    type: typing.Literal["rule-based"] = pydantic.Field(default="rule-based")
    """
    This condition is based on a strict rule.
    """

    operator: RuleBasedConditionOperator = pydantic.Field()
    """
    This is the operator you want to use to compare the left side and right side.
    
    The operation becomes `(leftSide) operator (rightSide)`.
    """

    left_side: typing_extensions.Annotated[str, FieldMetadata(alias="leftSide")] = pydantic.Field()
    """
    This is the left side of the operation.
    
    You can reference any variable in the context of the current block execution (step):
    - "{{output.your-property-name}}" for current step's output
    - "{{input.your-property-name}}" for current step's input
    - "{{your-step-name.output.your-property-name}}" for another step's output (in the same workflow; read caveat #1)
    - "{{your-step-name.input.your-property-name}}" for another step's input (in the same workflow; read caveat #1)
    - "{{your-block-name.output.your-property-name}}" for another block's output (in the same workflow; read caveat #2)
    - "{{your-block-name.input.your-property-name}}" for another block's input (in the same workflow; read caveat #2)
    - "{{workflow.input.your-property-name}}" for the current workflow's input
    - "{{global.your-property-name}}" for the global context
    
    Or, you can use a constant:
    - "1"
    - "text"
    - "true"
    - "false"
    
    Or, you can mix and match with string interpolation:
    - "{{your-property-name}}-{{input.your-property-name-2}}-1"
    
    Caveats:
    1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.input/output.propertyName}} will reference the latest usage of the step.
    2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.input/output.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.
    """

    right_side: typing_extensions.Annotated[str, FieldMetadata(alias="rightSide")] = pydantic.Field()
    """
    This is the right side of the operation.
    
    You can reference any variable in the context of the current block execution (step):
    - "{{output.your-property-name}}" for current step's output
    - "{{input.your-property-name}}" for current step's input
    - "{{your-step-name.output.your-property-name}}" for another step's output (in the same workflow; read caveat #1)
    - "{{your-step-name.input.your-property-name}}" for another step's input (in the same workflow; read caveat #1)
    - "{{your-block-name.output.your-property-name}}" for another block's output (in the same workflow; read caveat #2)
    - "{{your-block-name.input.your-property-name}}" for another block's input (in the same workflow; read caveat #2)
    - "{{workflow.input.your-property-name}}" for the current workflow's input
    - "{{global.your-property-name}}" for the global context
    
    Or, you can use a constant:
    - "1"
    - "text"
    - "true"
    - "false"
    
    Or, you can mix and match with string interpolation:
    - "{{your-property-name}}-{{input.your-property-name-2}}-1"
    
    Caveats:
    1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.input/output.propertyName}} will reference the latest usage of the step.
    2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.input/output.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
