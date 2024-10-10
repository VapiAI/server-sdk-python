# This file was auto-generated by Fern from our API Definition.

from .types import (
    AddVoiceToProviderDto,
    Analysis,
    AnalysisCost,
    AnalysisCostAnalysisType,
    AnalysisCostBreakdown,
    AnalysisPlan,
    AnalyticsOperation,
    AnalyticsOperationColumn,
    AnalyticsOperationOperation,
    AnalyticsQuery,
    AnalyticsQueryGroupByItem,
    AnalyticsQueryResult,
    AnthropicCredential,
    AnthropicModel,
    AnthropicModelModel,
    AnthropicModelToolsItem,
    AnyscaleCredential,
    AnyscaleModel,
    AnyscaleModelToolsItem,
    Artifact,
    ArtifactMessagesItem,
    ArtifactPlan,
    AssignmentMutation,
    AssignmentMutationConditionsItem,
    Assistant,
    AssistantBackgroundSound,
    AssistantClientMessagesItem,
    AssistantFirstMessageMode,
    AssistantModel,
    AssistantOverrides,
    AssistantOverridesBackgroundSound,
    AssistantOverridesClientMessagesItem,
    AssistantOverridesFirstMessageMode,
    AssistantOverridesModel,
    AssistantOverridesServerMessagesItem,
    AssistantOverridesTranscriber,
    AssistantOverridesVoice,
    AssistantServerMessagesItem,
    AssistantTranscriber,
    AssistantVoice,
    AzureOpenAiCredential,
    AzureOpenAiCredentialModelsItem,
    AzureOpenAiCredentialRegion,
    AzureVoice,
    AzureVoiceId,
    AzureVoiceIdEnum,
    BlockCompleteMessage,
    BlockCompleteMessageConditionsItem,
    BlockStartMessage,
    BlockStartMessageConditionsItem,
    BotMessage,
    BucketPlan,
    BuyPhoneNumberDto,
    BuyPhoneNumberDtoFallbackDestination,
    ByoPhoneNumber,
    ByoPhoneNumberFallbackDestination,
    ByoSipTrunkCredential,
    Call,
    CallCostsItem,
    CallDestination,
    CallEndedReason,
    CallMessagesItem,
    CallPaginatedResponse,
    CallPhoneCallProvider,
    CallPhoneCallTransport,
    CallStatus,
    CallType,
    CallbackStep,
    CallbackStepBlock,
    CartesiaCredential,
    CartesiaVoice,
    CartesiaVoiceLanguage,
    CartesiaVoiceModel,
    ChunkPlan,
    ClientInboundMessage,
    ClientInboundMessageAddMessage,
    ClientInboundMessageControl,
    ClientInboundMessageControlControl,
    ClientInboundMessageMessage,
    ClientInboundMessageSay,
    ClientMessage,
    ClientMessageConversationUpdate,
    ClientMessageConversationUpdateMessagesItem,
    ClientMessageHang,
    ClientMessageLanguageChanged,
    ClientMessageMessage,
    ClientMessageMetadata,
    ClientMessageModelOutput,
    ClientMessageSpeechUpdate,
    ClientMessageSpeechUpdateRole,
    ClientMessageSpeechUpdateStatus,
    ClientMessageToolCalls,
    ClientMessageToolCallsResult,
    ClientMessageToolCallsToolWithToolCallListItem,
    ClientMessageTranscript,
    ClientMessageTranscriptRole,
    ClientMessageTranscriptTranscriptType,
    ClientMessageUserInterrupted,
    ClientMessageVoiceInput,
    CloneVoiceDto,
    Condition,
    ConditionOperator,
    ConversationBlock,
    ConversationBlockMessagesItem,
    CostBreakdown,
    CreateAnthropicCredentialDto,
    CreateAnyscaleCredentialDto,
    CreateAssistantDto,
    CreateAssistantDtoBackgroundSound,
    CreateAssistantDtoClientMessagesItem,
    CreateAssistantDtoFirstMessageMode,
    CreateAssistantDtoModel,
    CreateAssistantDtoServerMessagesItem,
    CreateAssistantDtoTranscriber,
    CreateAssistantDtoVoice,
    CreateAzureOpenAiCredentialDto,
    CreateAzureOpenAiCredentialDtoModelsItem,
    CreateAzureOpenAiCredentialDtoRegion,
    CreateByoPhoneNumberDto,
    CreateByoPhoneNumberDtoFallbackDestination,
    CreateByoSipTrunkCredentialDto,
    CreateCartesiaCredentialDto,
    CreateConversationBlockDto,
    CreateConversationBlockDtoMessagesItem,
    CreateCustomLlmCredentialDto,
    CreateCustomerDto,
    CreateDeepInfraCredentialDto,
    CreateDeepgramCredentialDto,
    CreateDtmfToolDto,
    CreateDtmfToolDtoMessagesItem,
    CreateElevenLabsCredentialDto,
    CreateEndCallToolDto,
    CreateEndCallToolDtoMessagesItem,
    CreateFunctionToolDto,
    CreateFunctionToolDtoMessagesItem,
    CreateGcpCredentialDto,
    CreateGhlToolDto,
    CreateGhlToolDtoMessagesItem,
    CreateGladiaCredentialDto,
    CreateGoHighLevelCredentialDto,
    CreateGroqCredentialDto,
    CreateLmntCredentialDto,
    CreateMakeCredentialDto,
    CreateMakeToolDto,
    CreateMakeToolDtoMessagesItem,
    CreateOpenAiCredentialDto,
    CreateOpenRouterCredentialDto,
    CreateOrgDto,
    CreateOutboundCallDto,
    CreateOutputToolDto,
    CreateOutputToolDtoMessagesItem,
    CreatePerplexityAiCredentialDto,
    CreatePlayHtCredentialDto,
    CreateRimeAiCredentialDto,
    CreateRunpodCredentialDto,
    CreateS3CredentialDto,
    CreateSquadDto,
    CreateTogetherAiCredentialDto,
    CreateTokenDto,
    CreateTokenDtoTag,
    CreateToolCallBlockDto,
    CreateToolCallBlockDtoMessagesItem,
    CreateToolCallBlockDtoTool,
    CreateToolTemplateDto,
    CreateToolTemplateDtoDetails,
    CreateToolTemplateDtoProvider,
    CreateToolTemplateDtoProviderDetails,
    CreateToolTemplateDtoVisibility,
    CreateTransferCallToolDto,
    CreateTransferCallToolDtoDestinationsItem,
    CreateTransferCallToolDtoMessagesItem,
    CreateTwilioCredentialDto,
    CreateTwilioPhoneNumberDto,
    CreateTwilioPhoneNumberDtoFallbackDestination,
    CreateVapiPhoneNumberDto,
    CreateVapiPhoneNumberDtoFallbackDestination,
    CreateVoicemailToolDto,
    CreateVoicemailToolDtoMessagesItem,
    CreateVonageCredentialDto,
    CreateVonagePhoneNumberDto,
    CreateVonagePhoneNumberDtoFallbackDestination,
    CreateWebCallDto,
    CreateWorkflowBlockDto,
    CreateWorkflowBlockDtoMessagesItem,
    CreateWorkflowBlockDtoStepsItem,
    CustomLlmCredential,
    CustomLlmModel,
    CustomLlmModelMetadataSendMode,
    CustomLlmModelToolsItem,
    DeepInfraCredential,
    DeepInfraModel,
    DeepInfraModelToolsItem,
    DeepgramCredential,
    DeepgramTranscriber,
    DeepgramTranscriberLanguage,
    DeepgramTranscriberModel,
    DeepgramVoice,
    DeepgramVoiceId,
    DeepgramVoiceIdEnum,
    DtmfTool,
    DtmfToolMessagesItem,
    ElevenLabsCredential,
    ElevenLabsVoice,
    ElevenLabsVoiceId,
    ElevenLabsVoiceIdEnum,
    ElevenLabsVoiceModel,
    EndCallTool,
    EndCallToolMessagesItem,
    Error,
    ExactReplacement,
    File,
    FileStatus,
    FormatPlan,
    FormatPlanReplacementsItem,
    FunctionTool,
    FunctionToolMessagesItem,
    FunctionToolProviderDetails,
    FunctionToolWithToolCall,
    FunctionToolWithToolCallMessagesItem,
    GcpCredential,
    GcpKey,
    GhlTool,
    GhlToolMessagesItem,
    GhlToolMetadata,
    GhlToolProviderDetails,
    GhlToolWithToolCall,
    GhlToolWithToolCallMessagesItem,
    GladiaCredential,
    GladiaTranscriber,
    GladiaTranscriberLanguage,
    GladiaTranscriberLanguageBehaviour,
    GladiaTranscriberModel,
    GoHighLevelCredential,
    GroqCredential,
    GroqModel,
    GroqModelModel,
    GroqModelToolsItem,
    HandoffStep,
    HandoffStepBlock,
    ImportTwilioPhoneNumberDto,
    ImportTwilioPhoneNumberDtoFallbackDestination,
    ImportVonagePhoneNumberDto,
    ImportVonagePhoneNumberDtoFallbackDestination,
    InviteUserDto,
    InviteUserDtoRole,
    JsonSchema,
    JsonSchemaType,
    KnowledgeBase,
    LmntCredential,
    LmntVoice,
    LmntVoiceId,
    LmntVoiceIdEnum,
    Log,
    LogRequestHttpMethod,
    LogResource,
    LogType,
    LogsPaginatedResponse,
    MakeCredential,
    MakeTool,
    MakeToolMessagesItem,
    MakeToolMetadata,
    MakeToolProviderDetails,
    MakeToolWithToolCall,
    MakeToolWithToolCallMessagesItem,
    MessagePlan,
    Metrics,
    ModelBasedCondition,
    ModelCost,
    Monitor,
    MonitorPlan,
    NeetsVoice,
    NeetsVoiceId,
    NeetsVoiceIdEnum,
    OpenAiCredential,
    OpenAiFunction,
    OpenAiFunctionParameters,
    OpenAiMessage,
    OpenAiMessageRole,
    OpenAiModel,
    OpenAiModelFallbackModelsItem,
    OpenAiModelModel,
    OpenAiModelToolsItem,
    OpenAiVoice,
    OpenAiVoiceId,
    OpenRouterCredential,
    OpenRouterModel,
    OpenRouterModelToolsItem,
    Org,
    OrgPlan,
    OutputTool,
    OutputToolMessagesItem,
    PaginationMeta,
    PerplexityAiCredential,
    PerplexityAiModel,
    PerplexityAiModelToolsItem,
    PlayHtCredential,
    PlayHtVoice,
    PlayHtVoiceEmotion,
    PlayHtVoiceId,
    PlayHtVoiceIdEnum,
    PunctuationBoundary,
    RegexOption,
    RegexOptionType,
    RegexReplacement,
    RimeAiCredential,
    RimeAiVoice,
    RimeAiVoiceId,
    RimeAiVoiceIdEnum,
    RimeAiVoiceModel,
    RuleBasedCondition,
    RuleBasedConditionOperator,
    RunpodCredential,
    S3Credential,
    SbcConfiguration,
    Server,
    ServerMessage,
    ServerMessageAssistantRequest,
    ServerMessageAssistantRequestPhoneNumber,
    ServerMessageConversationUpdate,
    ServerMessageConversationUpdateMessagesItem,
    ServerMessageConversationUpdatePhoneNumber,
    ServerMessageEndOfCallReport,
    ServerMessageEndOfCallReportCostsItem,
    ServerMessageEndOfCallReportEndedReason,
    ServerMessageEndOfCallReportPhoneNumber,
    ServerMessageHang,
    ServerMessageHangPhoneNumber,
    ServerMessageLanguageChanged,
    ServerMessageLanguageChangedPhoneNumber,
    ServerMessageMessage,
    ServerMessageModelOutput,
    ServerMessageModelOutputPhoneNumber,
    ServerMessagePhoneCallControl,
    ServerMessagePhoneCallControlDestination,
    ServerMessagePhoneCallControlPhoneNumber,
    ServerMessagePhoneCallControlRequest,
    ServerMessageResponse,
    ServerMessageResponseAssistantRequest,
    ServerMessageResponseAssistantRequestDestination,
    ServerMessageResponseMessageResponse,
    ServerMessageResponseToolCalls,
    ServerMessageResponseTransferDestinationRequest,
    ServerMessageResponseTransferDestinationRequestDestination,
    ServerMessageResponseVoiceRequest,
    ServerMessageSpeechUpdate,
    ServerMessageSpeechUpdatePhoneNumber,
    ServerMessageSpeechUpdateRole,
    ServerMessageSpeechUpdateStatus,
    ServerMessageStatusUpdate,
    ServerMessageStatusUpdateDestination,
    ServerMessageStatusUpdateEndedReason,
    ServerMessageStatusUpdateMessagesItem,
    ServerMessageStatusUpdatePhoneNumber,
    ServerMessageStatusUpdateStatus,
    ServerMessageToolCalls,
    ServerMessageToolCallsPhoneNumber,
    ServerMessageToolCallsToolWithToolCallListItem,
    ServerMessageTranscript,
    ServerMessageTranscriptPhoneNumber,
    ServerMessageTranscriptRole,
    ServerMessageTranscriptTranscriptType,
    ServerMessageTransferDestinationRequest,
    ServerMessageTransferDestinationRequestPhoneNumber,
    ServerMessageTransferUpdate,
    ServerMessageTransferUpdateDestination,
    ServerMessageTransferUpdatePhoneNumber,
    ServerMessageUserInterrupted,
    ServerMessageUserInterruptedPhoneNumber,
    ServerMessageVoiceInput,
    ServerMessageVoiceInputPhoneNumber,
    ServerMessageVoiceRequest,
    ServerMessageVoiceRequestPhoneNumber,
    SipTrunkGateway,
    SipTrunkGatewayOutboundProtocol,
    SipTrunkOutboundAuthenticationPlan,
    SipTrunkOutboundSipRegisterPlan,
    Squad,
    SquadMemberDto,
    StartSpeakingPlan,
    StepDestination,
    StepDestinationConditionsItem,
    StopSpeakingPlan,
    StructuredDataPlan,
    SuccessEvaluationPlan,
    SuccessEvaluationPlanRubric,
    SummaryPlan,
    SyncVoiceLibraryDto,
    SyncVoiceLibraryDtoProvidersItem,
    SystemMessage,
    TalkscriberTranscriber,
    TalkscriberTranscriberLanguage,
    Template,
    TemplateDetails,
    TemplateProvider,
    TemplateProviderDetails,
    TemplateVisibility,
    TimeRange,
    TimeRangeStep,
    TogetherAiCredential,
    TogetherAiModel,
    TogetherAiModelToolsItem,
    Token,
    TokenRestrictions,
    TokenTag,
    ToolCall,
    ToolCallBlock,
    ToolCallBlockMessagesItem,
    ToolCallBlockTool,
    ToolCallFunction,
    ToolCallMessage,
    ToolCallResult,
    ToolCallResultMessage,
    ToolCallResultMessageItem,
    ToolMessageComplete,
    ToolMessageCompleteRole,
    ToolMessageDelayed,
    ToolMessageFailed,
    ToolMessageStart,
    ToolTemplateMetadata,
    ToolTemplateSetup,
    TranscriberCost,
    TranscriptPlan,
    TranscriptionEndpointingPlan,
    TransferCallTool,
    TransferCallToolDestinationsItem,
    TransferCallToolMessagesItem,
    TransferDestinationAssistant,
    TransferDestinationNumber,
    TransferDestinationSip,
    TransferDestinationStep,
    TransferMode,
    TransportConfigurationTwilio,
    TransportConfigurationTwilioRecordingChannels,
    TransportCost,
    TwilioCredential,
    TwilioPhoneNumber,
    TwilioPhoneNumberFallbackDestination,
    TwilioVoicemailDetection,
    TwilioVoicemailDetectionVoicemailDetectionTypesItem,
    UpdateAnthropicCredentialDto,
    UpdateAnyscaleCredentialDto,
    UpdateAzureOpenAiCredentialDto,
    UpdateAzureOpenAiCredentialDtoModelsItem,
    UpdateAzureOpenAiCredentialDtoRegion,
    UpdateByoSipTrunkCredentialDto,
    UpdateCartesiaCredentialDto,
    UpdateCustomLlmCredentialDto,
    UpdateDeepInfraCredentialDto,
    UpdateDeepgramCredentialDto,
    UpdateElevenLabsCredentialDto,
    UpdateGcpCredentialDto,
    UpdateGladiaCredentialDto,
    UpdateGoHighLevelCredentialDto,
    UpdateGroqCredentialDto,
    UpdateLmntCredentialDto,
    UpdateMakeCredentialDto,
    UpdateOpenAiCredentialDto,
    UpdateOpenRouterCredentialDto,
    UpdateOrgDto,
    UpdatePerplexityAiCredentialDto,
    UpdatePlayHtCredentialDto,
    UpdateRimeAiCredentialDto,
    UpdateRunpodCredentialDto,
    UpdateS3CredentialDto,
    UpdateTogetherAiCredentialDto,
    UpdateToolTemplateDto,
    UpdateToolTemplateDtoDetails,
    UpdateToolTemplateDtoProvider,
    UpdateToolTemplateDtoProviderDetails,
    UpdateToolTemplateDtoVisibility,
    UpdateTwilioCredentialDto,
    UpdateUserRoleDto,
    UpdateUserRoleDtoRole,
    UpdateVonageCredentialDto,
    User,
    UserMessage,
    VapiCost,
    VapiModel,
    VapiModelStepsItem,
    VapiModelToolsItem,
    VapiPhoneNumber,
    VapiPhoneNumberFallbackDestination,
    VoiceCost,
    VoiceLibrary,
    VoiceLibraryGender,
    VoiceLibraryVoiceResponse,
    VonageCredential,
    VonagePhoneNumber,
    VonagePhoneNumberFallbackDestination,
    WorkflowBlock,
    WorkflowBlockMessagesItem,
    WorkflowBlockStepsItem,
)
from .errors import BadRequestError
from . import analytics, assistants, blocks, calls, files, logs, phone_numbers, squads, tools
from .assistants import (
    UpdateAssistantDtoBackgroundSound,
    UpdateAssistantDtoClientMessagesItem,
    UpdateAssistantDtoFirstMessageMode,
    UpdateAssistantDtoModel,
    UpdateAssistantDtoServerMessagesItem,
    UpdateAssistantDtoTranscriber,
    UpdateAssistantDtoVoice,
)
from .blocks import (
    BlocksCreateRequest,
    BlocksCreateResponse,
    BlocksDeleteResponse,
    BlocksGetResponse,
    BlocksListResponseItem,
    BlocksUpdateResponse,
    UpdateBlockDtoMessagesItem,
    UpdateBlockDtoStepsItem,
    UpdateBlockDtoTool,
)
from .client import AsyncVapi, Vapi
from .environment import VapiEnvironment
from .logs import LogsGetRequestSortOrder, LogsGetRequestType
from .phone_numbers import (
    PhoneNumbersCreateRequest,
    PhoneNumbersCreateResponse,
    PhoneNumbersDeleteResponse,
    PhoneNumbersGetResponse,
    PhoneNumbersListResponseItem,
    PhoneNumbersUpdateResponse,
    UpdatePhoneNumberDtoFallbackDestination,
)
from .tools import (
    ToolsCreateRequest,
    ToolsCreateResponse,
    ToolsDeleteResponse,
    ToolsGetResponse,
    ToolsListResponseItem,
    ToolsUpdateResponse,
    UpdateToolDtoMessagesItem,
)
from .version import __version__

__all__ = [
    "AddVoiceToProviderDto",
    "Analysis",
    "AnalysisCost",
    "AnalysisCostAnalysisType",
    "AnalysisCostBreakdown",
    "AnalysisPlan",
    "AnalyticsOperation",
    "AnalyticsOperationColumn",
    "AnalyticsOperationOperation",
    "AnalyticsQuery",
    "AnalyticsQueryGroupByItem",
    "AnalyticsQueryResult",
    "AnthropicCredential",
    "AnthropicModel",
    "AnthropicModelModel",
    "AnthropicModelToolsItem",
    "AnyscaleCredential",
    "AnyscaleModel",
    "AnyscaleModelToolsItem",
    "Artifact",
    "ArtifactMessagesItem",
    "ArtifactPlan",
    "AssignmentMutation",
    "AssignmentMutationConditionsItem",
    "Assistant",
    "AssistantBackgroundSound",
    "AssistantClientMessagesItem",
    "AssistantFirstMessageMode",
    "AssistantModel",
    "AssistantOverrides",
    "AssistantOverridesBackgroundSound",
    "AssistantOverridesClientMessagesItem",
    "AssistantOverridesFirstMessageMode",
    "AssistantOverridesModel",
    "AssistantOverridesServerMessagesItem",
    "AssistantOverridesTranscriber",
    "AssistantOverridesVoice",
    "AssistantServerMessagesItem",
    "AssistantTranscriber",
    "AssistantVoice",
    "AsyncVapi",
    "AzureOpenAiCredential",
    "AzureOpenAiCredentialModelsItem",
    "AzureOpenAiCredentialRegion",
    "AzureVoice",
    "AzureVoiceId",
    "AzureVoiceIdEnum",
    "BadRequestError",
    "BlockCompleteMessage",
    "BlockCompleteMessageConditionsItem",
    "BlockStartMessage",
    "BlockStartMessageConditionsItem",
    "BlocksCreateRequest",
    "BlocksCreateResponse",
    "BlocksDeleteResponse",
    "BlocksGetResponse",
    "BlocksListResponseItem",
    "BlocksUpdateResponse",
    "BotMessage",
    "BucketPlan",
    "BuyPhoneNumberDto",
    "BuyPhoneNumberDtoFallbackDestination",
    "ByoPhoneNumber",
    "ByoPhoneNumberFallbackDestination",
    "ByoSipTrunkCredential",
    "Call",
    "CallCostsItem",
    "CallDestination",
    "CallEndedReason",
    "CallMessagesItem",
    "CallPaginatedResponse",
    "CallPhoneCallProvider",
    "CallPhoneCallTransport",
    "CallStatus",
    "CallType",
    "CallbackStep",
    "CallbackStepBlock",
    "CartesiaCredential",
    "CartesiaVoice",
    "CartesiaVoiceLanguage",
    "CartesiaVoiceModel",
    "ChunkPlan",
    "ClientInboundMessage",
    "ClientInboundMessageAddMessage",
    "ClientInboundMessageControl",
    "ClientInboundMessageControlControl",
    "ClientInboundMessageMessage",
    "ClientInboundMessageSay",
    "ClientMessage",
    "ClientMessageConversationUpdate",
    "ClientMessageConversationUpdateMessagesItem",
    "ClientMessageHang",
    "ClientMessageLanguageChanged",
    "ClientMessageMessage",
    "ClientMessageMetadata",
    "ClientMessageModelOutput",
    "ClientMessageSpeechUpdate",
    "ClientMessageSpeechUpdateRole",
    "ClientMessageSpeechUpdateStatus",
    "ClientMessageToolCalls",
    "ClientMessageToolCallsResult",
    "ClientMessageToolCallsToolWithToolCallListItem",
    "ClientMessageTranscript",
    "ClientMessageTranscriptRole",
    "ClientMessageTranscriptTranscriptType",
    "ClientMessageUserInterrupted",
    "ClientMessageVoiceInput",
    "CloneVoiceDto",
    "Condition",
    "ConditionOperator",
    "ConversationBlock",
    "ConversationBlockMessagesItem",
    "CostBreakdown",
    "CreateAnthropicCredentialDto",
    "CreateAnyscaleCredentialDto",
    "CreateAssistantDto",
    "CreateAssistantDtoBackgroundSound",
    "CreateAssistantDtoClientMessagesItem",
    "CreateAssistantDtoFirstMessageMode",
    "CreateAssistantDtoModel",
    "CreateAssistantDtoServerMessagesItem",
    "CreateAssistantDtoTranscriber",
    "CreateAssistantDtoVoice",
    "CreateAzureOpenAiCredentialDto",
    "CreateAzureOpenAiCredentialDtoModelsItem",
    "CreateAzureOpenAiCredentialDtoRegion",
    "CreateByoPhoneNumberDto",
    "CreateByoPhoneNumberDtoFallbackDestination",
    "CreateByoSipTrunkCredentialDto",
    "CreateCartesiaCredentialDto",
    "CreateConversationBlockDto",
    "CreateConversationBlockDtoMessagesItem",
    "CreateCustomLlmCredentialDto",
    "CreateCustomerDto",
    "CreateDeepInfraCredentialDto",
    "CreateDeepgramCredentialDto",
    "CreateDtmfToolDto",
    "CreateDtmfToolDtoMessagesItem",
    "CreateElevenLabsCredentialDto",
    "CreateEndCallToolDto",
    "CreateEndCallToolDtoMessagesItem",
    "CreateFunctionToolDto",
    "CreateFunctionToolDtoMessagesItem",
    "CreateGcpCredentialDto",
    "CreateGhlToolDto",
    "CreateGhlToolDtoMessagesItem",
    "CreateGladiaCredentialDto",
    "CreateGoHighLevelCredentialDto",
    "CreateGroqCredentialDto",
    "CreateLmntCredentialDto",
    "CreateMakeCredentialDto",
    "CreateMakeToolDto",
    "CreateMakeToolDtoMessagesItem",
    "CreateOpenAiCredentialDto",
    "CreateOpenRouterCredentialDto",
    "CreateOrgDto",
    "CreateOutboundCallDto",
    "CreateOutputToolDto",
    "CreateOutputToolDtoMessagesItem",
    "CreatePerplexityAiCredentialDto",
    "CreatePlayHtCredentialDto",
    "CreateRimeAiCredentialDto",
    "CreateRunpodCredentialDto",
    "CreateS3CredentialDto",
    "CreateSquadDto",
    "CreateTogetherAiCredentialDto",
    "CreateTokenDto",
    "CreateTokenDtoTag",
    "CreateToolCallBlockDto",
    "CreateToolCallBlockDtoMessagesItem",
    "CreateToolCallBlockDtoTool",
    "CreateToolTemplateDto",
    "CreateToolTemplateDtoDetails",
    "CreateToolTemplateDtoProvider",
    "CreateToolTemplateDtoProviderDetails",
    "CreateToolTemplateDtoVisibility",
    "CreateTransferCallToolDto",
    "CreateTransferCallToolDtoDestinationsItem",
    "CreateTransferCallToolDtoMessagesItem",
    "CreateTwilioCredentialDto",
    "CreateTwilioPhoneNumberDto",
    "CreateTwilioPhoneNumberDtoFallbackDestination",
    "CreateVapiPhoneNumberDto",
    "CreateVapiPhoneNumberDtoFallbackDestination",
    "CreateVoicemailToolDto",
    "CreateVoicemailToolDtoMessagesItem",
    "CreateVonageCredentialDto",
    "CreateVonagePhoneNumberDto",
    "CreateVonagePhoneNumberDtoFallbackDestination",
    "CreateWebCallDto",
    "CreateWorkflowBlockDto",
    "CreateWorkflowBlockDtoMessagesItem",
    "CreateWorkflowBlockDtoStepsItem",
    "CustomLlmCredential",
    "CustomLlmModel",
    "CustomLlmModelMetadataSendMode",
    "CustomLlmModelToolsItem",
    "DeepInfraCredential",
    "DeepInfraModel",
    "DeepInfraModelToolsItem",
    "DeepgramCredential",
    "DeepgramTranscriber",
    "DeepgramTranscriberLanguage",
    "DeepgramTranscriberModel",
    "DeepgramVoice",
    "DeepgramVoiceId",
    "DeepgramVoiceIdEnum",
    "DtmfTool",
    "DtmfToolMessagesItem",
    "ElevenLabsCredential",
    "ElevenLabsVoice",
    "ElevenLabsVoiceId",
    "ElevenLabsVoiceIdEnum",
    "ElevenLabsVoiceModel",
    "EndCallTool",
    "EndCallToolMessagesItem",
    "Error",
    "ExactReplacement",
    "File",
    "FileStatus",
    "FormatPlan",
    "FormatPlanReplacementsItem",
    "FunctionTool",
    "FunctionToolMessagesItem",
    "FunctionToolProviderDetails",
    "FunctionToolWithToolCall",
    "FunctionToolWithToolCallMessagesItem",
    "GcpCredential",
    "GcpKey",
    "GhlTool",
    "GhlToolMessagesItem",
    "GhlToolMetadata",
    "GhlToolProviderDetails",
    "GhlToolWithToolCall",
    "GhlToolWithToolCallMessagesItem",
    "GladiaCredential",
    "GladiaTranscriber",
    "GladiaTranscriberLanguage",
    "GladiaTranscriberLanguageBehaviour",
    "GladiaTranscriberModel",
    "GoHighLevelCredential",
    "GroqCredential",
    "GroqModel",
    "GroqModelModel",
    "GroqModelToolsItem",
    "HandoffStep",
    "HandoffStepBlock",
    "ImportTwilioPhoneNumberDto",
    "ImportTwilioPhoneNumberDtoFallbackDestination",
    "ImportVonagePhoneNumberDto",
    "ImportVonagePhoneNumberDtoFallbackDestination",
    "InviteUserDto",
    "InviteUserDtoRole",
    "JsonSchema",
    "JsonSchemaType",
    "KnowledgeBase",
    "LmntCredential",
    "LmntVoice",
    "LmntVoiceId",
    "LmntVoiceIdEnum",
    "Log",
    "LogRequestHttpMethod",
    "LogResource",
    "LogType",
    "LogsGetRequestSortOrder",
    "LogsGetRequestType",
    "LogsPaginatedResponse",
    "MakeCredential",
    "MakeTool",
    "MakeToolMessagesItem",
    "MakeToolMetadata",
    "MakeToolProviderDetails",
    "MakeToolWithToolCall",
    "MakeToolWithToolCallMessagesItem",
    "MessagePlan",
    "Metrics",
    "ModelBasedCondition",
    "ModelCost",
    "Monitor",
    "MonitorPlan",
    "NeetsVoice",
    "NeetsVoiceId",
    "NeetsVoiceIdEnum",
    "OpenAiCredential",
    "OpenAiFunction",
    "OpenAiFunctionParameters",
    "OpenAiMessage",
    "OpenAiMessageRole",
    "OpenAiModel",
    "OpenAiModelFallbackModelsItem",
    "OpenAiModelModel",
    "OpenAiModelToolsItem",
    "OpenAiVoice",
    "OpenAiVoiceId",
    "OpenRouterCredential",
    "OpenRouterModel",
    "OpenRouterModelToolsItem",
    "Org",
    "OrgPlan",
    "OutputTool",
    "OutputToolMessagesItem",
    "PaginationMeta",
    "PerplexityAiCredential",
    "PerplexityAiModel",
    "PerplexityAiModelToolsItem",
    "PhoneNumbersCreateRequest",
    "PhoneNumbersCreateResponse",
    "PhoneNumbersDeleteResponse",
    "PhoneNumbersGetResponse",
    "PhoneNumbersListResponseItem",
    "PhoneNumbersUpdateResponse",
    "PlayHtCredential",
    "PlayHtVoice",
    "PlayHtVoiceEmotion",
    "PlayHtVoiceId",
    "PlayHtVoiceIdEnum",
    "PunctuationBoundary",
    "RegexOption",
    "RegexOptionType",
    "RegexReplacement",
    "RimeAiCredential",
    "RimeAiVoice",
    "RimeAiVoiceId",
    "RimeAiVoiceIdEnum",
    "RimeAiVoiceModel",
    "RuleBasedCondition",
    "RuleBasedConditionOperator",
    "RunpodCredential",
    "S3Credential",
    "SbcConfiguration",
    "Server",
    "ServerMessage",
    "ServerMessageAssistantRequest",
    "ServerMessageAssistantRequestPhoneNumber",
    "ServerMessageConversationUpdate",
    "ServerMessageConversationUpdateMessagesItem",
    "ServerMessageConversationUpdatePhoneNumber",
    "ServerMessageEndOfCallReport",
    "ServerMessageEndOfCallReportCostsItem",
    "ServerMessageEndOfCallReportEndedReason",
    "ServerMessageEndOfCallReportPhoneNumber",
    "ServerMessageHang",
    "ServerMessageHangPhoneNumber",
    "ServerMessageLanguageChanged",
    "ServerMessageLanguageChangedPhoneNumber",
    "ServerMessageMessage",
    "ServerMessageModelOutput",
    "ServerMessageModelOutputPhoneNumber",
    "ServerMessagePhoneCallControl",
    "ServerMessagePhoneCallControlDestination",
    "ServerMessagePhoneCallControlPhoneNumber",
    "ServerMessagePhoneCallControlRequest",
    "ServerMessageResponse",
    "ServerMessageResponseAssistantRequest",
    "ServerMessageResponseAssistantRequestDestination",
    "ServerMessageResponseMessageResponse",
    "ServerMessageResponseToolCalls",
    "ServerMessageResponseTransferDestinationRequest",
    "ServerMessageResponseTransferDestinationRequestDestination",
    "ServerMessageResponseVoiceRequest",
    "ServerMessageSpeechUpdate",
    "ServerMessageSpeechUpdatePhoneNumber",
    "ServerMessageSpeechUpdateRole",
    "ServerMessageSpeechUpdateStatus",
    "ServerMessageStatusUpdate",
    "ServerMessageStatusUpdateDestination",
    "ServerMessageStatusUpdateEndedReason",
    "ServerMessageStatusUpdateMessagesItem",
    "ServerMessageStatusUpdatePhoneNumber",
    "ServerMessageStatusUpdateStatus",
    "ServerMessageToolCalls",
    "ServerMessageToolCallsPhoneNumber",
    "ServerMessageToolCallsToolWithToolCallListItem",
    "ServerMessageTranscript",
    "ServerMessageTranscriptPhoneNumber",
    "ServerMessageTranscriptRole",
    "ServerMessageTranscriptTranscriptType",
    "ServerMessageTransferDestinationRequest",
    "ServerMessageTransferDestinationRequestPhoneNumber",
    "ServerMessageTransferUpdate",
    "ServerMessageTransferUpdateDestination",
    "ServerMessageTransferUpdatePhoneNumber",
    "ServerMessageUserInterrupted",
    "ServerMessageUserInterruptedPhoneNumber",
    "ServerMessageVoiceInput",
    "ServerMessageVoiceInputPhoneNumber",
    "ServerMessageVoiceRequest",
    "ServerMessageVoiceRequestPhoneNumber",
    "SipTrunkGateway",
    "SipTrunkGatewayOutboundProtocol",
    "SipTrunkOutboundAuthenticationPlan",
    "SipTrunkOutboundSipRegisterPlan",
    "Squad",
    "SquadMemberDto",
    "StartSpeakingPlan",
    "StepDestination",
    "StepDestinationConditionsItem",
    "StopSpeakingPlan",
    "StructuredDataPlan",
    "SuccessEvaluationPlan",
    "SuccessEvaluationPlanRubric",
    "SummaryPlan",
    "SyncVoiceLibraryDto",
    "SyncVoiceLibraryDtoProvidersItem",
    "SystemMessage",
    "TalkscriberTranscriber",
    "TalkscriberTranscriberLanguage",
    "Template",
    "TemplateDetails",
    "TemplateProvider",
    "TemplateProviderDetails",
    "TemplateVisibility",
    "TimeRange",
    "TimeRangeStep",
    "TogetherAiCredential",
    "TogetherAiModel",
    "TogetherAiModelToolsItem",
    "Token",
    "TokenRestrictions",
    "TokenTag",
    "ToolCall",
    "ToolCallBlock",
    "ToolCallBlockMessagesItem",
    "ToolCallBlockTool",
    "ToolCallFunction",
    "ToolCallMessage",
    "ToolCallResult",
    "ToolCallResultMessage",
    "ToolCallResultMessageItem",
    "ToolMessageComplete",
    "ToolMessageCompleteRole",
    "ToolMessageDelayed",
    "ToolMessageFailed",
    "ToolMessageStart",
    "ToolTemplateMetadata",
    "ToolTemplateSetup",
    "ToolsCreateRequest",
    "ToolsCreateResponse",
    "ToolsDeleteResponse",
    "ToolsGetResponse",
    "ToolsListResponseItem",
    "ToolsUpdateResponse",
    "TranscriberCost",
    "TranscriptPlan",
    "TranscriptionEndpointingPlan",
    "TransferCallTool",
    "TransferCallToolDestinationsItem",
    "TransferCallToolMessagesItem",
    "TransferDestinationAssistant",
    "TransferDestinationNumber",
    "TransferDestinationSip",
    "TransferDestinationStep",
    "TransferMode",
    "TransportConfigurationTwilio",
    "TransportConfigurationTwilioRecordingChannels",
    "TransportCost",
    "TwilioCredential",
    "TwilioPhoneNumber",
    "TwilioPhoneNumberFallbackDestination",
    "TwilioVoicemailDetection",
    "TwilioVoicemailDetectionVoicemailDetectionTypesItem",
    "UpdateAnthropicCredentialDto",
    "UpdateAnyscaleCredentialDto",
    "UpdateAssistantDtoBackgroundSound",
    "UpdateAssistantDtoClientMessagesItem",
    "UpdateAssistantDtoFirstMessageMode",
    "UpdateAssistantDtoModel",
    "UpdateAssistantDtoServerMessagesItem",
    "UpdateAssistantDtoTranscriber",
    "UpdateAssistantDtoVoice",
    "UpdateAzureOpenAiCredentialDto",
    "UpdateAzureOpenAiCredentialDtoModelsItem",
    "UpdateAzureOpenAiCredentialDtoRegion",
    "UpdateBlockDtoMessagesItem",
    "UpdateBlockDtoStepsItem",
    "UpdateBlockDtoTool",
    "UpdateByoSipTrunkCredentialDto",
    "UpdateCartesiaCredentialDto",
    "UpdateCustomLlmCredentialDto",
    "UpdateDeepInfraCredentialDto",
    "UpdateDeepgramCredentialDto",
    "UpdateElevenLabsCredentialDto",
    "UpdateGcpCredentialDto",
    "UpdateGladiaCredentialDto",
    "UpdateGoHighLevelCredentialDto",
    "UpdateGroqCredentialDto",
    "UpdateLmntCredentialDto",
    "UpdateMakeCredentialDto",
    "UpdateOpenAiCredentialDto",
    "UpdateOpenRouterCredentialDto",
    "UpdateOrgDto",
    "UpdatePerplexityAiCredentialDto",
    "UpdatePhoneNumberDtoFallbackDestination",
    "UpdatePlayHtCredentialDto",
    "UpdateRimeAiCredentialDto",
    "UpdateRunpodCredentialDto",
    "UpdateS3CredentialDto",
    "UpdateTogetherAiCredentialDto",
    "UpdateToolDtoMessagesItem",
    "UpdateToolTemplateDto",
    "UpdateToolTemplateDtoDetails",
    "UpdateToolTemplateDtoProvider",
    "UpdateToolTemplateDtoProviderDetails",
    "UpdateToolTemplateDtoVisibility",
    "UpdateTwilioCredentialDto",
    "UpdateUserRoleDto",
    "UpdateUserRoleDtoRole",
    "UpdateVonageCredentialDto",
    "User",
    "UserMessage",
    "Vapi",
    "VapiCost",
    "VapiEnvironment",
    "VapiModel",
    "VapiModelStepsItem",
    "VapiModelToolsItem",
    "VapiPhoneNumber",
    "VapiPhoneNumberFallbackDestination",
    "VoiceCost",
    "VoiceLibrary",
    "VoiceLibraryGender",
    "VoiceLibraryVoiceResponse",
    "VonageCredential",
    "VonagePhoneNumber",
    "VonagePhoneNumberFallbackDestination",
    "WorkflowBlock",
    "WorkflowBlockMessagesItem",
    "WorkflowBlockStepsItem",
    "__version__",
    "analytics",
    "assistants",
    "blocks",
    "calls",
    "files",
    "logs",
    "phone_numbers",
    "squads",
    "tools",
]
