# This file was auto-generated by Fern from our API Definition.

import typing
from .function_tool_with_tool_call import FunctionToolWithToolCall
from .ghl_tool_with_tool_call import GhlToolWithToolCall
from .make_tool_with_tool_call import MakeToolWithToolCall
from .bash_tool_with_tool_call import BashToolWithToolCall
from .computer_tool_with_tool_call import ComputerToolWithToolCall
from .text_editor_tool_with_tool_call import TextEditorToolWithToolCall
from .google_calendar_create_event_tool_with_tool_call import GoogleCalendarCreateEventToolWithToolCall

ClientMessageToolCallsToolWithToolCallListItem = typing.Union[
    FunctionToolWithToolCall,
    GhlToolWithToolCall,
    MakeToolWithToolCall,
    BashToolWithToolCall,
    ComputerToolWithToolCall,
    TextEditorToolWithToolCall,
    GoogleCalendarCreateEventToolWithToolCall,
]
