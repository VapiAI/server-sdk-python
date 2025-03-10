# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .text_content import TextContent
import pydantic
from .block_complete_message_conditions_item import BlockCompleteMessageConditionsItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BlockCompleteMessage(UncheckedBaseModel):
    contents: typing.Optional[typing.List[TextContent]] = pydantic.Field(default=None)
    """
    This is an alternative to the `content` property. It allows to specify variants of the same content, one per language.
    
    Usage:
    - If your assistants are multilingual, you can provide content for each language.
    - If you don't provide content for a language, the first item in the array will be automatically translated to the active language at that moment.
    
    This will override the `content` property.
    """

    conditions: typing.Optional[typing.List[BlockCompleteMessageConditionsItem]] = pydantic.Field(default=None)
    """
    This is an optional array of conditions that must be met for this message to be triggered.
    """

    type: typing.Literal["block-complete"] = pydantic.Field(default="block-complete")
    """
    This is the message type that is triggered when the block completes.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the content that the assistant will say when this message is triggered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
