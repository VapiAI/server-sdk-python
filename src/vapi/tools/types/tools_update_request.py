# This file was auto-generated by Fern from our API Definition.

import typing
from ...types.update_dtmf_tool_dto import UpdateDtmfToolDto
from ...types.update_end_call_tool_dto import UpdateEndCallToolDto
from ...types.update_function_tool_dto import UpdateFunctionToolDto
from ...types.update_ghl_tool_dto import UpdateGhlToolDto
from ...types.update_make_tool_dto import UpdateMakeToolDto
from ...types.update_transfer_call_tool_dto import UpdateTransferCallToolDto
from ...types.update_output_tool_dto import UpdateOutputToolDto
from ...types.update_bash_tool_dto import UpdateBashToolDto
from ...types.update_computer_tool_dto import UpdateComputerToolDto
from ...types.update_text_editor_tool_dto import UpdateTextEditorToolDto

ToolsUpdateRequest = typing.Union[
    UpdateDtmfToolDto,
    UpdateEndCallToolDto,
    UpdateFunctionToolDto,
    UpdateGhlToolDto,
    UpdateMakeToolDto,
    UpdateTransferCallToolDto,
    UpdateOutputToolDto,
    UpdateBashToolDto,
    UpdateComputerToolDto,
    UpdateTextEditorToolDto,
]