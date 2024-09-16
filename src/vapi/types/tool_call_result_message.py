# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ToolCallResultMessage(UniversalBaseModel):
    role: str = pydantic.Field()
    """
    The role of the tool call result in the conversation.
    """

    tool_call_id: typing_extensions.Annotated[str, FieldMetadata(alias="toolCallId")] = pydantic.Field()
    """
    The ID of the tool call.
    """

    name: str = pydantic.Field()
    """
    The name of the tool that returned the result.
    """

    result: str = pydantic.Field()
    """
    The result of the tool call in JSON format.
    """

    time: float = pydantic.Field()
    """
    The timestamp when the message was sent.
    """

    seconds_from_start: typing_extensions.Annotated[float, FieldMetadata(alias="secondsFromStart")] = pydantic.Field()
    """
    The number of seconds from the start of the conversation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow