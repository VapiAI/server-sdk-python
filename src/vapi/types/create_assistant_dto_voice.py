# This file was auto-generated by Fern from our API Definition.

import typing
from .azure_voice import AzureVoice
from .cartesia_voice import CartesiaVoice
from .custom_voice import CustomVoice
from .deepgram_voice import DeepgramVoice
from .eleven_labs_voice import ElevenLabsVoice
from .hume_voice import HumeVoice
from .lmnt_voice import LmntVoice
from .neuphonic_voice import NeuphonicVoice
from .open_ai_voice import OpenAiVoice
from .play_ht_voice import PlayHtVoice
from .rime_ai_voice import RimeAiVoice
from .smallest_ai_voice import SmallestAiVoice
from .tavus_voice import TavusVoice
from .vapi_voice import VapiVoice

CreateAssistantDtoVoice = typing.Union[
    AzureVoice,
    CartesiaVoice,
    CustomVoice,
    DeepgramVoice,
    ElevenLabsVoice,
    HumeVoice,
    LmntVoice,
    NeuphonicVoice,
    OpenAiVoice,
    PlayHtVoice,
    RimeAiVoice,
    SmallestAiVoice,
    TavusVoice,
    VapiVoice,
]
