# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
from .create_dtmf_tool_dto_messages_item import CreateDtmfToolDtoMessagesItem
from .open_ai_function import OpenAiFunction
from .server import Server
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .create_end_call_tool_dto_messages_item import CreateEndCallToolDtoMessagesItem
from .create_voicemail_tool_dto_messages_item import CreateVoicemailToolDtoMessagesItem
from .create_function_tool_dto_messages_item import CreateFunctionToolDtoMessagesItem
from .create_ghl_tool_dto_messages_item import CreateGhlToolDtoMessagesItem
from .ghl_tool_metadata import GhlToolMetadata
from .create_make_tool_dto_messages_item import CreateMakeToolDtoMessagesItem
from .make_tool_metadata import MakeToolMetadata
from .create_transfer_call_tool_dto_messages_item import CreateTransferCallToolDtoMessagesItem
from .create_transfer_call_tool_dto_destinations_item import CreateTransferCallToolDtoDestinationsItem


class CreateToolCallBlockDtoTool_Dtmf(UniversalBaseModel):
    """
    This is the tool that the block will call. To use an existing tool, use `toolId`.
    """

    type: typing.Literal["dtmf"] = "dtmf"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateDtmfToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolCallBlockDtoTool_EndCall(UniversalBaseModel):
    """
    This is the tool that the block will call. To use an existing tool, use `toolId`.
    """

    type: typing.Literal["endCall"] = "endCall"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateEndCallToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolCallBlockDtoTool_Voicemail(UniversalBaseModel):
    """
    This is the tool that the block will call. To use an existing tool, use `toolId`.
    """

    type: typing.Literal["voicemail"] = "voicemail"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateVoicemailToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolCallBlockDtoTool_Function(UniversalBaseModel):
    """
    This is the tool that the block will call. To use an existing tool, use `toolId`.
    """

    type: typing.Literal["function"] = "function"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateFunctionToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolCallBlockDtoTool_Ghl(UniversalBaseModel):
    """
    This is the tool that the block will call. To use an existing tool, use `toolId`.
    """

    type: typing.Literal["ghl"] = "ghl"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateGhlToolDtoMessagesItem]] = None
    metadata: GhlToolMetadata
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolCallBlockDtoTool_Make(UniversalBaseModel):
    """
    This is the tool that the block will call. To use an existing tool, use `toolId`.
    """

    type: typing.Literal["make"] = "make"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateMakeToolDtoMessagesItem]] = None
    metadata: MakeToolMetadata
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolCallBlockDtoTool_TransferCall(UniversalBaseModel):
    """
    This is the tool that the block will call. To use an existing tool, use `toolId`.
    """

    type: typing.Literal["transferCall"] = "transferCall"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateTransferCallToolDtoMessagesItem]] = None
    destinations: typing.Optional[typing.List[CreateTransferCallToolDtoDestinationsItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateToolCallBlockDtoTool = typing.Union[
    CreateToolCallBlockDtoTool_Dtmf,
    CreateToolCallBlockDtoTool_EndCall,
    CreateToolCallBlockDtoTool_Voicemail,
    CreateToolCallBlockDtoTool_Function,
    CreateToolCallBlockDtoTool_Ghl,
    CreateToolCallBlockDtoTool_Make,
    CreateToolCallBlockDtoTool_TransferCall,
]