# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .tool_template_setup import ToolTemplateSetup
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MakeToolProviderDetails(UncheckedBaseModel):
    template_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="templateUrl")] = (
        pydantic.Field(default=None)
    )
    """
    This is the Template URL or the Snapshot URL corresponding to the Template.
    """

    setup_instructions: typing_extensions.Annotated[
        typing.Optional[typing.List[ToolTemplateSetup]], FieldMetadata(alias="setupInstructions")
    ] = None
    type: typing.Literal["make"] = pydantic.Field(default="make")
    """
    The type of tool. "make" for Make tool.
    """

    scenario_id: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="scenarioId")] = None
    scenario_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="scenarioName")] = None
    trigger_hook_id: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="triggerHookId")] = None
    trigger_hook_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="triggerHookName")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
