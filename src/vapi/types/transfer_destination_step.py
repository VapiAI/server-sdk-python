# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .transfer_destination_step_message import TransferDestinationStepMessage
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TransferDestinationStep(UniversalBaseModel):
    message: typing.Optional[TransferDestinationStepMessage] = pydantic.Field(default=None)
    """
    This is spoken to the customer before connecting them to the destination.
    
    Usage:
    - If this is not provided and transfer tool messages is not provided, default is "Transferring the call now".
    - If set to "", nothing is spoken. This is useful when you want to silently transfer. This is especially useful when transferring between assistants in a squad. In this scenario, you likely also want to set `assistant.firstMessageMode=assistant-speaks-first-with-model-generated-message` for the destination assistant.
    
    This accepts a string or a ToolMessageStart class. Latter is useful if you want to specify multiple messages for different languages through the `contents` field.
    """

    type: typing.Literal["step"] = "step"
    step_name: typing_extensions.Annotated[str, FieldMetadata(alias="stepName")] = pydantic.Field()
    """
    This is the step to transfer to.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the description of the destination, used by the AI to choose when and how to transfer the call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
