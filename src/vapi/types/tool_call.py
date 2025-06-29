# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .tool_call_function import ToolCallFunction


class ToolCall(UncheckedBaseModel):
    id: str = pydantic.Field()
    """
    This is the ID of the tool call
    """

    type: str = pydantic.Field()
    """
    This is the type of tool
    """

    function: ToolCallFunction = pydantic.Field()
    """
    This is the function that was called
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
