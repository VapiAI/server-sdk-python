# This file was auto-generated by Fern from our API Definition.

import typing
from .anyscale_model import AnyscaleModel
from .anthropic_model import AnthropicModel
from .custom_llm_model import CustomLlmModel
from .deep_infra_model import DeepInfraModel
from .groq_model import GroqModel
from .open_ai_model import OpenAiModel
from .open_router_model import OpenRouterModel
from .perplexity_ai_model import PerplexityAiModel
from .together_ai_model import TogetherAiModel
from .vapi_model import VapiModel

AssistantOverridesModel = typing.Union[
    AnyscaleModel,
    AnthropicModel,
    CustomLlmModel,
    DeepInfraModel,
    GroqModel,
    OpenAiModel,
    OpenRouterModel,
    PerplexityAiModel,
    TogetherAiModel,
    VapiModel,
]
