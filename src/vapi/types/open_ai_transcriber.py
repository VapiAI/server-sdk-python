# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .open_ai_transcriber_model import OpenAiTranscriberModel
from .open_ai_transcriber_language import OpenAiTranscriberLanguage
import typing_extensions
from .fallback_transcriber_plan import FallbackTranscriberPlan
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OpenAiTranscriber(UncheckedBaseModel):
    provider: typing.Literal["openai"] = pydantic.Field(default="openai")
    """
    This is the transcription provider that will be used.
    """

    model: OpenAiTranscriberModel = pydantic.Field()
    """
    This is the model that will be used for the transcription.
    """

    language: typing.Optional[OpenAiTranscriberLanguage] = pydantic.Field(default=None)
    """
    This is the language that will be set for the transcription.
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
