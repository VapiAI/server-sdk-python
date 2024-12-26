# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .start_speaking_plan_custom_endpointing_rules_item import StartSpeakingPlanCustomEndpointingRulesItem
from .transcription_endpointing_plan import TranscriptionEndpointingPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class StartSpeakingPlan(UniversalBaseModel):
    wait_seconds: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="waitSeconds")] = (
        pydantic.Field(default=None)
    )
    """
    This is how long assistant waits before speaking. Defaults to 0.4.
    
    This is the minimum it will wait but if there is latency is the pipeline, this minimum will be exceeded. This is intended as a stopgap in case the pipeline is moving too fast.
    
    Example:
    - If model generates tokens and voice generates bytes within 100ms, the pipeline still waits 300ms before outputting speech.
    
    Usage:
    - If the customer is taking long pauses, set this to a higher value.
    - If the assistant is accidentally jumping in too much, set this to a higher value.
    
    @default 0.4
    """

    smart_endpointing_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="smartEndpointingEnabled")
    ] = pydantic.Field(default=None)
    """
    This determines if a customer speech is considered done (endpointing) using a Vapi custom-trained model on customer's speech. This is good for middle-of-thought detection.
    
    Once an endpoint is triggered, the request is sent to `assistant.model`.
    
    Usage:
    - If your conversations are long-form and you want assistant to wait smartly even if customer pauses for a bit to think, you can use this instead.
    
    This overrides `transcriptionEndpointingPlan`.
    
    @default false
    """

    custom_endpointing_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[StartSpeakingPlanCustomEndpointingRulesItem]],
        FieldMetadata(alias="customEndpointingRules"),
    ] = pydantic.Field(default=None)
    """
    These are the custom endpointing rules to set an endpointing timeout based on a regex on the customer's speech or the assistant's last message.
    
    Usage:
    - If you have yes/no questions like "are you interested in a loan?", you can set a shorter timeout.
    - If you have questions where the customer may pause to look up information like "what's my account number?", you can set a longer timeout.
    - If you want to wait longer while customer is enumerating a list of numbers, you can set a longer timeout.
    
    These override `transcriptionEndpointingPlan` and `smartEndpointingEnabled` when a rule is matched.
    
    The rules are evaluated in order and the first one that matches will be used.
    
    @default []
    """

    transcription_endpointing_plan: typing_extensions.Annotated[
        typing.Optional[TranscriptionEndpointingPlan], FieldMetadata(alias="transcriptionEndpointingPlan")
    ] = pydantic.Field(default=None)
    """
    This determines how a customer speech is considered done (endpointing) using the transcription of customer's speech.
    
    Once an endpoint is triggered, the request is sent to `assistant.model`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
