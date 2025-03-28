# This file was auto-generated by Fern from our API Definition.

import typing
from .google_voicemail_detection_plan import GoogleVoicemailDetectionPlan
from .open_ai_voicemail_detection_plan import OpenAiVoicemailDetectionPlan
from .twilio_voicemail_detection_plan import TwilioVoicemailDetectionPlan

AssistantOverridesVoicemailDetection = typing.Union[
    GoogleVoicemailDetectionPlan, OpenAiVoicemailDetectionPlan, TwilioVoicemailDetectionPlan
]
