# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VoiceCost(UniversalBaseModel):
    voice: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    This is the voice that was used during the call.
    
    This matches one of the following:
    
    - `call.assistant.voice`,
    - `call.assistantId->voice`,
    - `call.squad[n].assistant.voice`,
    - `call.squad[n].assistantId->voice`,
    - `call.squadId->[n].assistant.voice`,
    - `call.squadId->[n].assistantId->voice`.
    """

    characters: float = pydantic.Field()
    """
    This is the number of characters that were generated during the call. These should be total characters used in the call for single assistant calls, while squad calls will have multiple voice costs one for each assistant that was used.
    """

    cost: float = pydantic.Field()
    """
    This is the cost of the component in USD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow