# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .workflow_open_ai_model_model import WorkflowOpenAiModelModel


class WorkflowOpenAiModel(UncheckedBaseModel):
    provider: typing.Literal["openai"] = pydantic.Field(default="openai")
    """
    This is the provider of the model (`openai`).
    """

    model: WorkflowOpenAiModelModel = pydantic.Field()
    """
    This is the OpenAI model that will be used.
    
    When using Vapi OpenAI or your own Azure Credentials, you have the option to specify the region for the selected model. This shouldn't be specified unless you have a specific reason to do so. Vapi will automatically find the fastest region that make sense.
    This is helpful when you are required to comply with Data Residency rules. Learn more about Azure regions here https://azure.microsoft.com/en-us/explore/global-infrastructure/data-residency/.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the temperature of the model.
    """

    max_tokens: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="maxTokens")] = pydantic.Field(
        default=None
    )
    """
    This is the max tokens of the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
