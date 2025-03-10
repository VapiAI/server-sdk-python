# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientMessageToolCallsResult(UncheckedBaseModel):
    type: typing.Literal["tool-calls-result"] = pydantic.Field(default="tool-calls-result")
    """
    This is the type of the message. "tool-calls-result" is sent to forward the result of a tool call to the client.
    """

    tool_call_result: typing_extensions.Annotated[
        typing.Dict[str, typing.Optional[typing.Any]], FieldMetadata(alias="toolCallResult")
    ] = pydantic.Field()
    """
    This is the result of the tool call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
