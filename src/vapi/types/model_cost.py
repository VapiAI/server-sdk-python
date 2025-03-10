# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ModelCost(UncheckedBaseModel):
    type: typing.Literal["model"] = pydantic.Field(default="model")
    """
    This is the type of cost, always 'model' for this class.
    """

    model: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    This is the model that was used during the call.
    
    This matches one of the following:
    - `call.assistant.model`,
    - `call.assistantId->model`,
    - `call.squad[n].assistant.model`,
    - `call.squad[n].assistantId->model`,
    - `call.squadId->[n].assistant.model`,
    - `call.squadId->[n].assistantId->model`.
    """

    prompt_tokens: typing_extensions.Annotated[float, FieldMetadata(alias="promptTokens")] = pydantic.Field()
    """
    This is the number of prompt tokens used in the call. These should be total prompt tokens used in the call for single assistant calls, while squad calls will have multiple model costs one for each assistant that was used.
    """

    completion_tokens: typing_extensions.Annotated[float, FieldMetadata(alias="completionTokens")] = pydantic.Field()
    """
    This is the number of completion tokens generated in the call. These should be total completion tokens used in the call for single assistant calls, while squad calls will have multiple model costs one for each assistant that was used.
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
