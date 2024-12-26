# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class StopSpeakingPlan(UniversalBaseModel):
    num_words: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="numWords")] = pydantic.Field(
        default=None
    )
    """
    This is the number of words that the customer has to say before the assistant will stop talking.
    
    Words like "stop", "actually", "no", etc. will always interrupt immediately regardless of this value.
    
    Words like "okay", "yeah", "right" will never interrupt.
    
    When set to 0, `voiceSeconds` is used in addition to the transcriptions to determine the customer has started speaking.
    
    Defaults to 0.
    
    @default 0
    """

    voice_seconds: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="voiceSeconds")] = (
        pydantic.Field(default=None)
    )
    """
    This is the seconds customer has to speak before the assistant stops talking. This uses the VAD (Voice Activity Detection) spike to determine if the customer has started speaking.
    
    Considerations:
    - A lower value might be more responsive but could potentially pick up non-speech sounds.
    - A higher value reduces false positives but might slightly delay the detection of speech onset.
    
    This is only used if `numWords` is set to 0.
    
    Defaults to 0.2
    
    @default 0.2
    """

    backoff_seconds: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="backoffSeconds")] = (
        pydantic.Field(default=None)
    )
    """
    This is the seconds to wait before the assistant will start talking again after being interrupted.
    
    Defaults to 1.
    
    @default 1
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
