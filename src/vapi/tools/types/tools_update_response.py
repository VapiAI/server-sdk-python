# This file was auto-generated by Fern from our API Definition.

import typing
from ...types.dtmf_tool import DtmfTool
from ...types.end_call_tool import EndCallTool
from ...types.function_tool import FunctionTool
from ...types.ghl_tool import GhlTool
from ...types.make_tool import MakeTool
from ...types.transfer_call_tool import TransferCallTool
from ...types.output_tool import OutputTool
from ...types.bash_tool import BashTool
from ...types.computer_tool import ComputerTool
from ...types.text_editor_tool import TextEditorTool
from ...types.query_tool import QueryTool
from ...types.google_calendar_create_event_tool import GoogleCalendarCreateEventTool
from ...types.google_sheets_row_append_tool import GoogleSheetsRowAppendTool
from ...types.google_calendar_check_availability_tool import GoogleCalendarCheckAvailabilityTool
from ...types.slack_send_message_tool import SlackSendMessageTool
from ...types.mcp_tool import McpTool

ToolsUpdateResponse = typing.Union[
    DtmfTool,
    EndCallTool,
    FunctionTool,
    GhlTool,
    MakeTool,
    TransferCallTool,
    OutputTool,
    BashTool,
    ComputerTool,
    TextEditorTool,
    QueryTool,
    GoogleCalendarCreateEventTool,
    GoogleSheetsRowAppendTool,
    GoogleCalendarCheckAvailabilityTool,
    SlackSendMessageTool,
    McpTool,
]
