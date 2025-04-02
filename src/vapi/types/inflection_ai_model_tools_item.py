# This file was auto-generated by Fern from our API Definition.

import typing
from .create_dtmf_tool_dto import CreateDtmfToolDto
from .create_end_call_tool_dto import CreateEndCallToolDto
from .create_voicemail_tool_dto import CreateVoicemailToolDto
from .create_function_tool_dto import CreateFunctionToolDto
from .create_ghl_tool_dto import CreateGhlToolDto
from .create_make_tool_dto import CreateMakeToolDto
from .create_transfer_call_tool_dto import CreateTransferCallToolDto
from .create_query_tool_dto import CreateQueryToolDto
from .create_google_calendar_create_event_tool_dto import CreateGoogleCalendarCreateEventToolDto
from .create_google_sheets_row_append_tool_dto import CreateGoogleSheetsRowAppendToolDto
from .create_google_calendar_check_availability_tool_dto import CreateGoogleCalendarCheckAvailabilityToolDto
from .create_slack_send_message_tool_dto import CreateSlackSendMessageToolDto

InflectionAiModelToolsItem = typing.Union[
    CreateDtmfToolDto,
    CreateEndCallToolDto,
    CreateVoicemailToolDto,
    CreateFunctionToolDto,
    CreateGhlToolDto,
    CreateMakeToolDto,
    CreateTransferCallToolDto,
    CreateQueryToolDto,
    CreateGoogleCalendarCreateEventToolDto,
    CreateGoogleSheetsRowAppendToolDto,
    CreateGoogleCalendarCheckAvailabilityToolDto,
    CreateSlackSendMessageToolDto,
]
