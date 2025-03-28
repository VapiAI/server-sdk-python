# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .talkscriber_transcriber_language import TalkscriberTranscriberLanguage
import typing_extensions
from .fallback_transcriber_plan import FallbackTranscriberPlan
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TalkscriberTranscriber(UncheckedBaseModel):
    provider: typing.Literal["talkscriber"] = pydantic.Field(default="talkscriber")
    """
    This is the transcription provider that will be used.
    """

    model: typing.Optional[typing.Literal["whisper"]] = pydantic.Field(default=None)
    """
    This is the model that will be used for the transcription.
    """

    language: typing.Optional[TalkscriberTranscriberLanguage] = pydantic.Field(default=None)
    """
    This is the language that will be set for the transcription. The list of languages Whisper supports can be found here: https://github.com/openai/whisper/blob/main/whisper/tokenizer.py
    """

    fallback_plan: typing_extensions.Annotated[
        typing.Optional[FallbackTranscriberPlan], FieldMetadata(alias="fallbackPlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan for voice provider fallbacks in the event that the primary voice provider fails.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
