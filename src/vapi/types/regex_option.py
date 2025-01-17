# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .regex_option_type import RegexOptionType
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class RegexOption(UniversalBaseModel):
    type: RegexOptionType = pydantic.Field()
    """
    This is the type of the regex option. Options are:
    - `ignore-case`: Ignores the case of the text being matched. Add
    - `whole-word`: Matches whole words only.
    - `multi-line`: Matches across multiple lines.
    """

    enabled: bool = pydantic.Field()
    """
    This is whether to enable the option.
    
    @default false
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
