# This file was auto-generated by Fern from our API Definition.

import typing
from .tool_message_start import ToolMessageStart
from .tool_message_complete import ToolMessageComplete
from .tool_message_failed import ToolMessageFailed
from .tool_message_delayed import ToolMessageDelayed

CreateBashToolDtoMessagesItem = typing.Union[
    ToolMessageStart, ToolMessageComplete, ToolMessageFailed, ToolMessageDelayed
]
