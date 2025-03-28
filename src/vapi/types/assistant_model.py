# This file was auto-generated by Fern from our API Definition.

import typing
from .anyscale_model import AnyscaleModel
from .anthropic_model import AnthropicModel
from .cerebras_model import CerebrasModel
from .custom_llm_model import CustomLlmModel
from .deep_infra_model import DeepInfraModel
from .deep_seek_model import DeepSeekModel
from .google_model import GoogleModel
from .groq_model import GroqModel
from .inflection_ai_model import InflectionAiModel
from .open_ai_model import OpenAiModel
from .open_router_model import OpenRouterModel
from .perplexity_ai_model import PerplexityAiModel
from .together_ai_model import TogetherAiModel
from .vapi_model import VapiModel
from .xai_model import XaiModel

AssistantModel = typing.Union[
    AnyscaleModel,
    AnthropicModel,
    CerebrasModel,
    CustomLlmModel,
    DeepInfraModel,
    DeepSeekModel,
    GoogleModel,
    GroqModel,
    InflectionAiModel,
    OpenAiModel,
    OpenRouterModel,
    PerplexityAiModel,
    TogetherAiModel,
    VapiModel,
    XaiModel,
]
