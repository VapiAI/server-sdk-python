# This file was auto-generated by Fern from our API Definition.

import typing
from .transport_cost import TransportCost
from .transcriber_cost import TranscriberCost
from .model_cost import ModelCost
from .voice_cost import VoiceCost
from .vapi_cost import VapiCost
from .voicemail_detection_cost import VoicemailDetectionCost
from .analysis_cost import AnalysisCost

CallCostsItem = typing.Union[
    TransportCost, TranscriberCost, ModelCost, VoiceCost, VapiCost, VoicemailDetectionCost, AnalysisCost
]
