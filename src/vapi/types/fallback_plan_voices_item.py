# This file was auto-generated by Fern from our API Definition.

import typing
from .fallback_azure_voice import FallbackAzureVoice
from .fallback_cartesia_voice import FallbackCartesiaVoice
from .fallback_custom_voice import FallbackCustomVoice
from .fallback_deepgram_voice import FallbackDeepgramVoice
from .fallback_eleven_labs_voice import FallbackElevenLabsVoice
from .fallback_lmnt_voice import FallbackLmntVoice
from .fallback_neets_voice import FallbackNeetsVoice
from .fallback_open_ai_voice import FallbackOpenAiVoice
from .fallback_play_ht_voice import FallbackPlayHtVoice
from .fallback_rime_ai_voice import FallbackRimeAiVoice
from .fallback_tavus_voice import FallbackTavusVoice

FallbackPlanVoicesItem = typing.Union[
    FallbackAzureVoice,
    FallbackCartesiaVoice,
    FallbackCustomVoice,
    FallbackDeepgramVoice,
    FallbackElevenLabsVoice,
    FallbackLmntVoice,
    FallbackNeetsVoice,
    FallbackOpenAiVoice,
    FallbackPlayHtVoice,
    FallbackRimeAiVoice,
    FallbackTavusVoice,
]
