# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .tool_node_tool import ToolNodeTool


class ToolNode(UncheckedBaseModel):
    type: typing.Literal["tool"] = pydantic.Field(default="tool")
    """
    This is the Tool node. This can be used to call a tool in your workflow.
    
    The flow is:
    - Workflow starts the tool node
    - Model is called to extract parameters needed by the tool from the conversation history
    - Tool is called with the parameters
    - Server returns a response
    - Workflow continues with the response
    """

    tool: typing.Optional[ToolNodeTool] = pydantic.Field(default=None)
    """
    This is the tool to call. To use an existing tool, send `toolId` instead.
    """

    tool_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="toolId")] = pydantic.Field(
        default=None
    )
    """
    This is the tool to call. To use a transient tool, send `tool` instead.
    """

    name: str
    is_start: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isStart")] = pydantic.Field(
        default=None
    )
    """
    This is whether or not the node is the start of the workflow.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    This is for metadata you want to store on the task.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
