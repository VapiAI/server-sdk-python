# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .server_message_message import ServerMessageMessage
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ServerMessage(UncheckedBaseModel):
    message: ServerMessageMessage = pydantic.Field()
    """
    These are all the messages that can be sent to your server before, after and during the call. Configure the messages you'd like to receive in `assistant.serverMessages`.
    
    The server where the message is sent is determined by the following precedence order:
    
    1. `tool.server.url` (if configured, and only for "tool-calls" message)
    2. `assistant.serverUrl` (if configure)
    3. `phoneNumber.serverUrl` (if configured)
    4. `org.serverUrl` (if configured)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
