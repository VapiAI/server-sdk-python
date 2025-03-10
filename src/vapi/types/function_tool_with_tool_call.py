# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .function_tool_with_tool_call_messages_item import FunctionToolWithToolCallMessagesItem
from .tool_call import ToolCall
from .open_ai_function import OpenAiFunction
from .server import Server
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FunctionToolWithToolCall(UncheckedBaseModel):
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = pydantic.Field(
        default=None
    )
    """
    This determines if the tool is async.
    
    If async, the assistant will move forward without waiting for your server to respond. This is useful if you just want to trigger something on your server.
    
    If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with the result from your server.
    
    Defaults to synchronous (`false`).
    """

    messages: typing.Optional[typing.List[FunctionToolWithToolCallMessagesItem]] = pydantic.Field(default=None)
    """
    These are the messages that will be spoken to the user as the tool is running.
    
    For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the function tool, these can be custom configured.
    """

    type: typing.Literal["function"] = pydantic.Field(default="function")
    """
    The type of tool. "function" for Function tool.
    """

    tool_call: typing_extensions.Annotated[ToolCall, FieldMetadata(alias="toolCall")]
    function: typing.Optional[OpenAiFunction] = pydantic.Field(default=None)
    """
    This is the function definition of the tool.
    
    For `endCall`, `transferCall`, and `dtmf` tools, this is auto-filled based on tool-specific fields like `tool.destinations`. But, even in those cases, you can provide a custom function definition for advanced use cases.
    
    An example of an advanced use case is if you want to customize the message that's spoken for `endCall` tool. You can specify a function where it returns an argument "reason". Then, in `messages` array, you can have many "request-complete" messages. One of these messages will be triggered if the `messages[].conditions` matches the "reason" argument.
    """

    server: typing.Optional[Server] = pydantic.Field(default=None)
    """
    This is the server that will be hit when this tool is requested by the model.
    
    All requests will be sent with the call object among other things. You can find more details in the Server URL documentation.
    
    This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: highest tool.server.url, then assistant.serverUrl, then phoneNumber.serverUrl, then org.serverUrl.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
