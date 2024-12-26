# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from .fallback_play_ht_voice_id import FallbackPlayHtVoiceId
from ..core.serialization import FieldMetadata
from .fallback_play_ht_voice_emotion import FallbackPlayHtVoiceEmotion
from .fallback_play_ht_voice_model import FallbackPlayHtVoiceModel
from .fallback_play_ht_voice_language import FallbackPlayHtVoiceLanguage
from .chunk_plan import ChunkPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackPlayHtVoice(UniversalBaseModel):
    provider: typing.Literal["playht"] = pydantic.Field(default="playht")
    """
    This is the voice provider that will be used.
    """

    voice_id: typing_extensions.Annotated[FallbackPlayHtVoiceId, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    This is the provider-specific ID that will be used.
    """

    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the speed multiplier that will be used.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    A floating point number between 0, exclusive, and 2, inclusive. If equal to null or not provided, the model's default temperature will be used. The temperature parameter controls variance. Lower temperatures result in more predictable results, higher temperatures allow each run to vary more, so the voice may sound less like the baseline voice.
    """

    emotion: typing.Optional[FallbackPlayHtVoiceEmotion] = pydantic.Field(default=None)
    """
    An emotion to be applied to the speech.
    """

    voice_guidance: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="voiceGuidance")] = (
        pydantic.Field(default=None)
    )
    """
    A number between 1 and 6. Use lower numbers to reduce how unique your chosen voice will be compared to other voices.
    """

    style_guidance: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="styleGuidance")] = (
        pydantic.Field(default=None)
    )
    """
    A number between 1 and 30. Use lower numbers to to reduce how strong your chosen emotion will be. Higher numbers will create a very emotional performance.
    """

    text_guidance: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="textGuidance")] = (
        pydantic.Field(default=None)
    )
    """
    A number between 1 and 2. This number influences how closely the generated speech adheres to the input text. Use lower values to create more fluid speech, but with a higher chance of deviating from the input text. Higher numbers will make the generated speech more accurate to the input text, ensuring that the words spoken align closely with the provided text.
    """

    model: typing.Optional[FallbackPlayHtVoiceModel] = pydantic.Field(default=None)
    """
    Playht voice model/engine to use.
    """

    language: typing.Optional[FallbackPlayHtVoiceLanguage] = pydantic.Field(default=None)
    """
    The language to use for the speech.
    """

    chunk_plan: typing_extensions.Annotated[typing.Optional[ChunkPlan], FieldMetadata(alias="chunkPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for chunking the model output before it is sent to the voice provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
