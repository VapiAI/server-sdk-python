# This file was auto-generated by Fern from our API Definition.

import typing

from .analysis_cost import AnalysisCost
from .knowledge_base_cost import KnowledgeBaseCost
from .model_cost import ModelCost
from .transcriber_cost import TranscriberCost
from .transport_cost import TransportCost
from .vapi_cost import VapiCost
from .voice_cost import VoiceCost
from .voicemail_detection_cost import VoicemailDetectionCost

CallCostsItem = typing.Union[
    TransportCost,
    TranscriberCost,
    ModelCost,
    VoiceCost,
    VapiCost,
    VoicemailDetectionCost,
    AnalysisCost,
    KnowledgeBaseCost,
]
