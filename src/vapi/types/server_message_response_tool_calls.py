# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .tool_call_result import ToolCallResult
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ServerMessageResponseToolCalls(UncheckedBaseModel):
    results: typing.Optional[typing.List[ToolCallResult]] = pydantic.Field(default=None)
    """
    These are the results of the "tool-calls" message.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the error message if the tool call was not successful.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
