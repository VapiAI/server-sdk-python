# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing
from .assistant_transcriber import AssistantTranscriber
import pydantic
from .assistant_model import AssistantModel
from .assistant_voice import AssistantVoice
import typing_extensions
from ..core.serialization import FieldMetadata
from .assistant_first_message_mode import AssistantFirstMessageMode
from .assistant_client_messages_item import AssistantClientMessagesItem
from .assistant_server_messages_item import AssistantServerMessagesItem
from .assistant_background_sound import AssistantBackgroundSound
from .transport_configuration_twilio import TransportConfigurationTwilio
from .assistant_credentials_item import AssistantCredentialsItem
from .twilio_voicemail_detection import TwilioVoicemailDetection
from .compliance_plan import CompliancePlan
from .analysis_plan import AnalysisPlan
from .artifact_plan import ArtifactPlan
from .message_plan import MessagePlan
from .start_speaking_plan import StartSpeakingPlan
from .stop_speaking_plan import StopSpeakingPlan
from .monitor_plan import MonitorPlan
from .server import Server
from .assistant_hooks import AssistantHooks
from .keypad_input_plan import KeypadInputPlan
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Assistant(UncheckedBaseModel):
    transcriber: typing.Optional[AssistantTranscriber] = pydantic.Field(default=None)
    """
    These are the options for the assistant's transcriber.
    """

    model: typing.Optional[AssistantModel] = pydantic.Field(default=None)
    """
    These are the options for the assistant's LLM.
    """

    voice: typing.Optional[AssistantVoice] = pydantic.Field(default=None)
    """
    These are the options for the assistant's voice.
    """

    first_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="firstMessage")] = (
        pydantic.Field(default=None)
    )
    """
    This is the first message that the assistant will say. This can also be a URL to a containerized audio file (mp3, wav, etc.).
    
    If unspecified, assistant will wait for user to speak and use the model to respond once they speak.
    """

    first_message_mode: typing_extensions.Annotated[
        typing.Optional[AssistantFirstMessageMode], FieldMetadata(alias="firstMessageMode")
    ] = pydantic.Field(default=None)
    """
    This is the mode for the first message. Default is 'assistant-speaks-first'.
    
    Use:
    - 'assistant-speaks-first' to have the assistant speak first.
    - 'assistant-waits-for-user' to have the assistant wait for the user to speak first.
    - 'assistant-speaks-first-with-model-generated-message' to have the assistant speak first with a message generated by the model based on the conversation state. (`assistant.model.messages` at call start, `call.messages` at squad transfer points).
    
    @default 'assistant-speaks-first'
    """

    client_messages: typing_extensions.Annotated[
        typing.Optional[typing.List[AssistantClientMessagesItem]], FieldMetadata(alias="clientMessages")
    ] = pydantic.Field(default=None)
    """
    These are the messages that will be sent to your Client SDKs. Default is conversation-update,function-call,hang,model-output,speech-update,status-update,transfer-update,transcript,tool-calls,user-interrupted,voice-input. You can check the shape of the messages in ClientMessage schema.
    """

    server_messages: typing_extensions.Annotated[
        typing.Optional[typing.List[AssistantServerMessagesItem]], FieldMetadata(alias="serverMessages")
    ] = pydantic.Field(default=None)
    """
    These are the messages that will be sent to your Server URL. Default is conversation-update,end-of-call-report,function-call,hang,speech-update,status-update,tool-calls,transfer-destination-request,user-interrupted. You can check the shape of the messages in ServerMessage schema.
    """

    silence_timeout_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="silenceTimeoutSeconds")
    ] = pydantic.Field(default=None)
    """
    How many seconds of silence to wait before ending the call. Defaults to 30.
    
    @default 30
    """

    max_duration_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxDurationSeconds")
    ] = pydantic.Field(default=None)
    """
    This is the maximum number of seconds that the call will last. When the call reaches this duration, it will be ended.
    
    @default 600 (10 minutes)
    """

    background_sound: typing_extensions.Annotated[
        typing.Optional[AssistantBackgroundSound], FieldMetadata(alias="backgroundSound")
    ] = pydantic.Field(default=None)
    """
    This is the background sound in the call. Default for phone calls is 'office' and default for web calls is 'off'.
    """

    background_denoising_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="backgroundDenoisingEnabled")
    ] = pydantic.Field(default=None)
    """
    This enables filtering of noise and background speech while the user is talking.
    
    Default `false` while in beta.
    
    @default false
    """

    model_output_in_messages_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="modelOutputInMessagesEnabled")
    ] = pydantic.Field(default=None)
    """
    This determines whether the model's output is used in conversation history rather than the transcription of assistant's speech.
    
    Default `false` while in beta.
    
    @default false
    """

    transport_configurations: typing_extensions.Annotated[
        typing.Optional[typing.List[TransportConfigurationTwilio]], FieldMetadata(alias="transportConfigurations")
    ] = pydantic.Field(default=None)
    """
    These are the configurations to be passed to the transport providers of assistant's calls, like Twilio. You can store multiple configurations for different transport providers. For a call, only the configuration matching the call transport provider is used.
    """

    credentials: typing.Optional[typing.List[AssistantCredentialsItem]] = pydantic.Field(default=None)
    """
    These are dynamic credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can supplement an additional credentials using this. Dynamic credentials override existing credentials.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the assistant.
    
    This is required when you want to transfer between assistants in a call.
    """

    voicemail_detection: typing_extensions.Annotated[
        typing.Optional[TwilioVoicemailDetection], FieldMetadata(alias="voicemailDetection")
    ] = pydantic.Field(default=None)
    """
    These are the settings to configure or disable voicemail detection. Alternatively, voicemail detection can be configured using the model.tools=[VoicemailTool].
    This uses Twilio's built-in detection while the VoicemailTool relies on the model to detect if a voicemail was reached.
    You can use neither of them, one of them, or both of them. By default, Twilio built-in detection is enabled while VoicemailTool is not.
    """

    voicemail_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="voicemailMessage")] = (
        pydantic.Field(default=None)
    )
    """
    This is the message that the assistant will say if the call is forwarded to voicemail.
    
    If unspecified, it will hang up.
    """

    end_call_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="endCallMessage")] = (
        pydantic.Field(default=None)
    )
    """
    This is the message that the assistant will say if it ends the call.
    
    If unspecified, it will hang up without saying anything.
    """

    end_call_phrases: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="endCallPhrases")
    ] = pydantic.Field(default=None)
    """
    This list contains phrases that, if spoken by the assistant, will trigger the call to be hung up. Case insensitive.
    """

    compliance_plan: typing_extensions.Annotated[
        typing.Optional[CompliancePlan], FieldMetadata(alias="compliancePlan")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    This is for metadata you want to store on the assistant.
    """

    analysis_plan: typing_extensions.Annotated[typing.Optional[AnalysisPlan], FieldMetadata(alias="analysisPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for analysis of assistant's calls. Stored in `call.analysis`.
    """

    artifact_plan: typing_extensions.Annotated[typing.Optional[ArtifactPlan], FieldMetadata(alias="artifactPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for artifacts generated during assistant's calls. Stored in `call.artifact`.
    
    Note: `recordingEnabled` is currently at the root level. It will be moved to `artifactPlan` in the future, but will remain backwards compatible.
    """

    message_plan: typing_extensions.Annotated[typing.Optional[MessagePlan], FieldMetadata(alias="messagePlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for static predefined messages that can be spoken by the assistant during the call, like `idleMessages`.
    
    Note: `firstMessage`, `voicemailMessage`, and `endCallMessage` are currently at the root level. They will be moved to `messagePlan` in the future, but will remain backwards compatible.
    """

    start_speaking_plan: typing_extensions.Annotated[
        typing.Optional[StartSpeakingPlan], FieldMetadata(alias="startSpeakingPlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan for when the assistant should start talking.
    
    You should configure this if you're running into these issues:
    - The assistant is too slow to start talking after the customer is done speaking.
    - The assistant is too fast to start talking after the customer is done speaking.
    - The assistant is so fast that it's actually interrupting the customer.
    """

    stop_speaking_plan: typing_extensions.Annotated[
        typing.Optional[StopSpeakingPlan], FieldMetadata(alias="stopSpeakingPlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan for when assistant should stop talking on customer interruption.
    
    You should configure this if you're running into these issues:
    - The assistant is too slow to recognize customer's interruption.
    - The assistant is too fast to recognize customer's interruption.
    - The assistant is getting interrupted by phrases that are just acknowledgments.
    - The assistant is getting interrupted by background noises.
    - The assistant is not properly stopping -- it starts talking right after getting interrupted.
    """

    monitor_plan: typing_extensions.Annotated[typing.Optional[MonitorPlan], FieldMetadata(alias="monitorPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for real-time monitoring of the assistant's calls.
    
    Usage:
    - To enable live listening of the assistant's calls, set `monitorPlan.listenEnabled` to `true`.
    - To enable live control of the assistant's calls, set `monitorPlan.controlEnabled` to `true`.
    
    Note, `serverMessages`, `clientMessages`, `serverUrl` and `serverUrlSecret` are currently at the root level but will be moved to `monitorPlan` in the future. Will remain backwards compatible
    """

    credential_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="credentialIds")
    ] = pydantic.Field(default=None)
    """
    These are the credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can provide a subset using this.
    """

    server: typing.Optional[Server] = pydantic.Field(default=None)
    """
    This is where Vapi will send webhooks. You can find all webhooks available along with their shape in ServerMessage schema.
    
    The order of precedence is:
    
    1. assistant.server.url
    2. phoneNumber.serverUrl
    3. org.serverUrl
    """

    hooks: typing.Optional[typing.List[AssistantHooks]] = pydantic.Field(default=None)
    """
    This is a set of actions that will be performed on certain events.
    """

    keypad_input_plan: typing_extensions.Annotated[
        typing.Optional[KeypadInputPlan], FieldMetadata(alias="keypadInputPlan")
    ] = None
    id: str = pydantic.Field()
    """
    This is the unique identifier for the assistant.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this assistant belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the assistant was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the assistant was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
