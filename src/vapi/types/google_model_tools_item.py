# This file was auto-generated by Fern from our API Definition.

import typing
from .create_dtmf_tool_dto import CreateDtmfToolDto
from .create_end_call_tool_dto import CreateEndCallToolDto
from .create_voicemail_tool_dto import CreateVoicemailToolDto
from .create_function_tool_dto import CreateFunctionToolDto
from .create_ghl_tool_dto import CreateGhlToolDto
from .create_make_tool_dto import CreateMakeToolDto
from .create_transfer_call_tool_dto import CreateTransferCallToolDto

GoogleModelToolsItem = typing.Union[
    CreateDtmfToolDto,
    CreateEndCallToolDto,
    CreateVoicemailToolDto,
    CreateFunctionToolDto,
    CreateGhlToolDto,
    CreateMakeToolDto,
    CreateTransferCallToolDto,
]
