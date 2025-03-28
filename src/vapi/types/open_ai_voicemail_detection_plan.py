# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OpenAiVoicemailDetectionPlan(UncheckedBaseModel):
    provider: typing.Literal["openai"] = pydantic.Field(default="openai")
    """
    This is the provider to use for voicemail detection.
    """

    voicemail_expected_duration_seconds: typing_extensions.Annotated[
        float, FieldMetadata(alias="voicemailExpectedDurationSeconds")
    ] = pydantic.Field()
    """
    This is how long should we listen in order to determine if we were sent to voicemail or not?
    
    @default 15
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
