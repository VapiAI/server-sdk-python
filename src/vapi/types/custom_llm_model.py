# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .open_ai_message import OpenAiMessage
import pydantic
from .custom_llm_model_tools_item import CustomLlmModelToolsItem
import typing_extensions
from ..core.serialization import FieldMetadata
from .create_custom_knowledge_base_dto import CreateCustomKnowledgeBaseDto
from .custom_llm_model_metadata_send_mode import CustomLlmModelMetadataSendMode
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CustomLlmModel(UncheckedBaseModel):
    messages: typing.Optional[typing.List[OpenAiMessage]] = pydantic.Field(default=None)
    """
    This is the starting state for the conversation.
    """

    tools: typing.Optional[typing.List[CustomLlmModelToolsItem]] = pydantic.Field(default=None)
    """
    These are the tools that the assistant can use during the call. To use existing tools, use `toolIds`.
    
    Both `tools` and `toolIds` can be used together.
    """

    tool_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="toolIds")] = (
        pydantic.Field(default=None)
    )
    """
    These are the tools that the assistant can use during the call. To use transient tools, use `tools`.
    
    Both `tools` and `toolIds` can be used together.
    """

    knowledge_base: typing_extensions.Annotated[
        typing.Optional[CreateCustomKnowledgeBaseDto], FieldMetadata(alias="knowledgeBase")
    ] = pydantic.Field(default=None)
    """
    These are the options for the knowledge base.
    """

    knowledge_base_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="knowledgeBaseId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ID of the knowledge base the model will use.
    """

    provider: typing.Literal["custom-llm"] = pydantic.Field(default="custom-llm")
    """
    This is the provider that will be used for the model. Any service, including your own server, that is compatible with the OpenAI API can be used.
    """

    metadata_send_mode: typing_extensions.Annotated[
        typing.Optional[CustomLlmModelMetadataSendMode], FieldMetadata(alias="metadataSendMode")
    ] = pydantic.Field(default=None)
    """
    This determines whether metadata is sent in requests to the custom provider.
    
    - `off` will not send any metadata. payload will look like `{ messages }`
    - `variable` will send `assistant.metadata` as a variable on the payload. payload will look like `{ messages, metadata }`
    - `destructured` will send `assistant.metadata` fields directly on the payload. payload will look like `{ messages, ...metadata }`
    
    Further, `variable` and `destructured` will send `call`, `phoneNumber`, and `customer` objects in the payload.
    
    Default is `variable`.
    """

    url: str = pydantic.Field()
    """
    These is the URL we'll use for the OpenAI client's `baseURL`. Ex. https://openrouter.ai/api/v1
    """

    timeout_seconds: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="timeoutSeconds")] = (
        pydantic.Field(default=None)
    )
    """
    This sets the timeout for the connection to the custom provider without needing to stream any tokens back. Default is 20 seconds.
    """

    model: str = pydantic.Field()
    """
    This is the name of the model. Ex. cognitivecomputations/dolphin-mixtral-8x7b
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the temperature that will be used for calls. Default is 0 to leverage caching for lower latency.
    """

    max_tokens: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="maxTokens")] = pydantic.Field(
        default=None
    )
    """
    This is the max number of tokens that the assistant will be allowed to generate in each turn of the conversation. Default is 250.
    """

    emotion_recognition_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="emotionRecognitionEnabled")
    ] = pydantic.Field(default=None)
    """
    This determines whether we detect user's emotion while they speak and send it as an additional info to model.
    
    Default `false` because the model is usually are good at understanding the user's emotion from text.
    
    @default false
    """

    num_fast_turns: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="numFastTurns")] = (
        pydantic.Field(default=None)
    )
    """
    This sets how many turns at the start of the conversation to use a smaller, faster model from the same provider before switching to the primary model. Example, gpt-3.5-turbo if provider is openai.
    
    Default is 0.
    
    @default 0
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
