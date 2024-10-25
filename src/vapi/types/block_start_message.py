# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .block_start_message_conditions_item import BlockStartMessageConditionsItem
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BlockStartMessage(UniversalBaseModel):
    conditions: typing.Optional[typing.List[BlockStartMessageConditionsItem]] = pydantic.Field(default=None)
    """
    This is an optional array of conditions that must be met for this message to be triggered.
    """

    type: typing.Literal["block-start"] = pydantic.Field(default="block-start")
    """
    This is the message type that is triggered when the block starts.
    """

    content: str = pydantic.Field()
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
