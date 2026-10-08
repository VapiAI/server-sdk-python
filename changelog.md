## [3.0.0] - 2026-10-08
### Breaking Changes
- **`UpdateAssistantDtoTranscriber_Deepgram.eager_eot_threshold`** has been removed. Remove any references to this field in your code.
- **`UpdateAssistantDtoVoice_Vapi.fallback_plan`** has been removed from the Vapi voice variant. Remove any references to `fallback_plan` on Vapi voice configurations.
- **`UpdateAssistantDtoVoice_Vapi.voice_id`** type changed from `VapiVoiceVoiceId` to `str`. Update any strict type annotations referencing `VapiVoiceVoiceId` for this field.
- **`UpdateAssistantDtoTranscriber_Gladia.languages`** type changed from `GladiaTranscriberLanguages` to `typing.List[GladiaTranscriberLanguagesItem]`. Update imports and type annotations accordingly.

### Added
- **`UpdateAssistantDtoTranscriber_Xai`** and **`UpdateAssistantDtoTranscriber_Vapi`** — new transcriber provider variants supporting xAI and Vapi as transcription backends.
- **`UpdateAssistantDtoVoice_Xai`** and **`UpdateAssistantDtoVoice_Microsoft`** — new voice provider variants for xAI and Microsoft TTS.
- **`UpdateAssistantDtoTranscriber_AssemblyAi`** gains optional `mode`, `prompt`, `agent_context`, `agent_context_auto_update_enabled`, and `language_codes` fields.
- **`UpdateAssistantDtoTranscriber_Soniox`** gains optional `languages`, `endpoint_sensitivity`, `endpoint_latency_adjustment_level`, `context_general`, and `confidence_threshold` fields.
- **`UpdateAssistantDtoTranscriber_Deepgram`** gains optional `redaction` and `languages` fields; **`UpdateAssistantDtoVoice_Deepgram`** gains optional `speed` and `expressivity` fields.

### Added
- **`CallsClient.call_artifact_controller_mono_recording_download`**, **`stereo_recording_download`**, **`video_recording_download`**, **`customer_recording_download`**, **`assistant_recording_download`**, **`pcap_download`**, and **`call_logs_download`** — new methods (sync and async) to download call artifact files directly from the client.
- **`assistant_version`** and **`squad_version`** optional parameters on **`CallsClient.create`** — pin a specific assistant or squad version when creating a call.

### Changed
- **`CallsClient.create`** `transport` parameter type changed from `Dict[str, Any]` to the strongly-typed **`CreateCallDtoTransport`** model — update any callers passing a raw dict to use the new type.

### Added
- **`call_artifact_controller_mono_recording_download`**, **`stereo_recording_download`**, **`video_recording_download`**, **`customer_recording_download`**, **`assistant_recording_download`**, **`pcap_download`**, and **`call_logs_download`** — new methods on `RawCallsClient` and `AsyncRawCallsClient` to download call artifact files by call ID.
- **`assistant_version`** and **`squad_version`** optional parameters on `CallsClient.create()` — pin a specific assistant or squad version for a call instead of always following the latest.

### Changed
- **`CallsClient.create()` `transport` parameter** — now accepts the strongly-typed `CreateCallDtoTransport` instead of an untyped `Dict[str, Any]`, enabling proper serialization and IDE support.
- **`CallsClient.create()`** now raises `BadRequestError` (HTTP 400) and `InternalServerError` (HTTP 500) instead of falling through to a generic `ApiError`.
- **`CallsClient.delete()`** now raises `ServiceUnavailableError` (HTTP 503) instead of falling through to a generic `ApiError`.

### Added
- **`campaign_controller_find_all_v_2`** — new V2 list endpoint returning `CampaignSummaryPaginatedResponse` with optional `include_counters`, `sort_by`, and full timestamp range filters.
- **`campaign_controller_create_v_2`** and **`campaign_controller_create`** — campaign creation now accepts `max_concurrency`, `assistant_overrides`, `squad_overrides`, `server`, `server_messages`, `predial_plan`, and `duplicate_from_campaign_id` optional parameters.
- **`campaign_controller_find_one_v_2`** and **`campaign_controller_remove_v_2`** — V2 get and delete methods returning `CampaignSummary` with an optional `include_counters` flag.
- **`campaign_controller_update_v_2`** — V2 update method mirroring V1 but under the new versioned endpoint.
- **`campaign_controller_get_campaign_v_2_contacts`** — paginated contact retrieval for a campaign with status filtering and sort control, returning `CampaignContactPaginatedResponse`.

### Added
- **`campaign_controller_find_all_v_2`** — new method on `RawCampaignsClient` and `AsyncRawCampaignsClient` that lists campaigns via the `v2/campaign` endpoint, returning `CampaignSummaryPaginatedResponse` with optional aggregate `contactCounters` and `callMetrics` via `include_counters`.
- **`campaign_controller_create_v_2`**, **`campaign_controller_find_one_v_2`**, **`campaign_controller_remove_v_2`**, and **`campaign_controller_update_v_2`** — full CRUD suite on the v2 campaigns API for both sync and async clients.
- **`campaign_controller_get_campaign_v_2_contacts`** — new endpoint (`v2/campaign/{id}/contacts`) for paginated, filterable contact listing per campaign, available on both sync and async clients.
- **New optional parameters on `campaign_controller_create`** — `max_concurrency`, `assistant_overrides`, `squad_overrides`, `server`, `server_messages`, `predial_plan`, and `duplicate_from_campaign_id` added to both sync and async variants.
- **`sort_by` parameter** added to `campaign_controller_find_all` (sync and async) for column-level sort control alongside the existing `sort_order`.

### Added
- **`FilesClient.list()` / `AsyncFilesClient.list()`** — new optional `purpose` parameter (`ListFilesRequestPurpose`) to filter returned files by purpose.
- **`FilesClient.create()` / `AsyncFilesClient.create()`** — new optional `purpose` (`CreateFilesRequestPurpose`) and `metadata` (str) parameters for richer file upload control.
- **`CreateToolsResponse_KnowledgeBase`** — new `knowledgeBase` variant added to the `CreateToolsResponse` union type, enabling knowledge-base tools to be represented in tool creation responses.
- **`latest_version`** — new optional field added to all `CreateToolsResponse_*` model variants to surface the tool's latest version.

### Added
- **`GetToolsResponse_KnowledgeBase`** and **`DeleteToolsResponse_KnowledgeBase`** — new `knowledgeBase` discriminated union members in tool list and delete response types, exposing `knowledge_base_id`, `function`, `messages`, `rejection_plan`, and standard audit fields.
- **`latest_version`** — new optional `str` field added to every tool response variant (e.g. `GetToolsResponse_ApiRequest`, `GetToolsResponse_Function`, etc.) that surfaces the tool's latest published version.

### Added
- **`ListToolsResponseItem_KnowledgeBase`** — new union member representing a `knowledgeBase`-typed tool in list tool responses, exposing `knowledge_base_id`, `function`, and standard tool metadata fields.
- **`UpdateToolsResponse_KnowledgeBase`** and **`UpdateToolsRequestBody_KnowledgeBase`** — new union members enabling retrieval and update of knowledge base tools via the tools API.
- **`latest_version`** (`latestVersion`) — new optional string field added to every tool variant in `ListToolsResponseItem` and `UpdateToolsResponse`, surfacing the tool's latest version string.

### Breaking Changes
- **`AssistantCredentialsItem_Trieve`** and **`AssistantOverridesCredentialsItem_Trieve`** have been removed from the credentials union. Remove any code that constructs or matches on the `trieve` provider variant.
- **`sbc_configuration`** field has been removed from `AssistantCredentialsItem_ByoSipTrunk` and `AssistantOverridesCredentialsItem_ByoSipTrunk`. Remove references to `sbc_configuration` on ByoSipTrunk credential objects.

### Added
- **`AssistantCredentialsItem_S3Compatible`** and **`AssistantOverridesCredentialsItem_S3Compatible`** — new S3-compatible storage credential variant using `S3CompatibleBucketPlan`.
- **`AssistantCredentialsItem_Microsoft`** and **`AssistantOverridesCredentialsItem_Microsoft`** — new Microsoft credential variant with `api_key` and optional `region`.
- **`AssistantOverridesTranscriber_Xai`** and **`AssistantOverridesTranscriber_Vapi`** — new transcriber provider variants for xAI and Vapi.
- **`AssistantOverridesVoice_Xai`** and **`AssistantOverridesVoice_Microsoft`** — new voice provider variants for xAI and Microsoft (with style, role, and speed controls).
- New optional fields on existing transcribermodels: `mode`, `prompt`, `language_codes` on AssemblyAI; `redaction`, `languages` on Deepgram; `languages`, `endpoint_sensitivity`, `context_general`, `confidence_threshold` on Soniox; `api_url` on 11Labs, Cartesia, and Soniox credentials.

### Added
- **`ConversationNodeVoice_Xai`** and **`ConversationNodeVoice_Microsoft`** — new voice provider variants added to the `ConversationNodeVoice` union, enabling xAI and Microsoft TTS in conversation nodes.
- **`CreateAssistantDtoVoice_Xai`** and **`CreateAssistantDtoVoice_Microsoft`** — new voice provider variants added to the `CreateAssistantDtoVoice` union for assistant configuration.
- **`CreateAssistantDtoTranscriber_Xai`** and **`CreateAssistantDtoTranscriber_Vapi`** — new transcriber provider variants added to the `CreateAssistantDtoTranscriber` union.
- **`CreateAssistantDtoCredentialsItem_S3Compatible`** and **`CreateAssistantDtoCredentialsItem_Microsoft`** — new credential item variants for S3-compatible storage and Microsoft Speech services.
- New optional fields on existing transcriber models: `mode`, `prompt`, `language_codes` on AssemblyAI; `redaction`, `languages` on Deepgram; `languages`, `endpoint_sensitivity`, `context_general`, `confidence_threshold` on Soniox; and `version`, `language`, `turn_taking` on the new Vapi transcriber.

### Added
- **`CreateWorkflowDtoVoice_Xai`** and **`CreateWorkflowDtoVoice_Microsoft`** — new voice provider variants for xAI and Microsoft TTS, also available as **`FallbackPlanVoicesItem_Xai`** and **`FallbackPlanVoicesItem_Microsoft`** in fallback plans.
- **`CreateWorkflowDtoTranscriber_Xai`** and **`CreateWorkflowDtoTranscriber_Vapi`** — new transcriber provider variants for xAI and Vapi native transcription.
- **`CreateWorkflowDtoCredentialsItem_S3Compatible`** and **`CreateWorkflowDtoCredentialsItem_Microsoft`** — new credential provider variants for S3-compatible storage and Microsoft services.
- **`api_url`** optional field added to `CreateWorkflowDtoCredentialsItem_11Labs`, `CreateWorkflowDtoCredentialsItem_Cartesia`, and `CreateWorkflowDtoCredentialsItem_Soniox` credential models.
- New optional fields on AssemblyAI (`mode`, `prompt`, `language_codes`), Deepgram (`redaction`, `languages`), Soniox (`languages`, `endpoint_sensitivity`, `context_general`, `confidence_threshold`), and Gladia (`languages` now typed as a list) transcriber models.

### Breaking Changes
- **`UpdatePersonalityDto`** has been removed and replaced by **`ServerMessageCampaignPredial`** with an entirely new field structure. Update any imports or type annotations referencing `UpdatePersonalityDto` to use `ServerMessageCampaignPredial` instead.
- **`CreateSimulationRunDtoTarget`**, **`CreateSimulationRunDtoTarget_Assistant`**, and **`CreateSimulationRunDtoTarget_Squad`** have been renamed to **`SimulationRunListItemTarget`**, **`SimulationRunListItemTarget_Assistant`**, and **`SimulationRunListItemTarget_Squad`**. Update all imports and type annotations accordingly.

### Added
- **`TransferAssistantTranscriber_Xai`** and **`TransferAssistantTranscriber_Vapi`** — new transcriber provider variants added to the `TransferAssistantTranscriber` union, enabling xAI and Vapi-native transcription for transfer assistants.
- **`TransferAssistantVoice_Xai`** and **`TransferAssistantVoice_Microsoft`** — new voice provider variants added to the `TransferAssistantVoice` union, enabling xAI and Microsoft voices for transfer assistants.
- New optional fields on existing transcriber models: AssemblyAI gains `mode`, `prompt`, `agentContext`, and `languageCodes`; Deepgram gains `redaction` and `languages`; Soniox gains `languages`, `endpointSensitivity`, `endpointLatencyAdjustmentLevel`, `contextGeneral`, and `confidenceThreshold`.

### Added
- **`WorkflowCredentialsItem_S3Compatible`** and **`WorkflowUserEditableCredentialsItem_S3Compatible`** — new credential variant for S3-compatible storage providers.
- **`WorkflowCredentialsItem_Microsoft`** and **`WorkflowUserEditableCredentialsItem_Microsoft`** — new credential variant for Microsoft with optional `region` field.
- **`WorkflowTranscriber_Xai`** and **`WorkflowTranscriber_Vapi`** — new transcriber variants (mirrored in `WorkflowUserEditableTranscriber`) for xAI and Vapi providers.
- Optional `api_url` field on **`WorkflowCredentialsItem_11Labs`**, **`WorkflowCredentialsItem_Cartesia`**, and **`WorkflowCredentialsItem_Soniox`** credential models.
- New optional fields on transcriber models: `mode`, `prompt`, `agent_context`, and `language_codes` on AssemblyAI; `redaction` and `languages` on Deepgram; `endpoint_sensitivity`, `endpoint_latency_adjustment_level`, `context_general`, and `confidence_threshold` on Soniox.

### Changed
- **`WorkflowCredentialsItem_ByoSipTrunk`** — `sbc_configuration` field removed; update any code reading this field.
- **`WorkflowCredentialsItem_Trieve`** and **`WorkflowUserEditableCredentialsItem_Trieve`** — removed from the credentials union; use an alternative provider variant.
- **`WorkflowTranscriber_Gladia`** `languages` field type changed from `GladiaTranscriberLanguages` to `List[GladiaTranscriberLanguagesItem]`; update type annotations accordingly.

### Added
- **`WorkflowVoice_Xai`** and **`WorkflowUserEditableVoice_Xai`** — new voice variant for the xAI provider, supporting `voice_id`, `language`, `speed`, `chunk_plan`, and `fallback_plan`.
- **`WorkflowVoice_Microsoft`** and **`WorkflowUserEditableVoice_Microsoft`** — new voice variant for the Microsoft provider, supporting `voice_id`, `style`, `style_degree`, `role`, `speed`, and `chunk_plan`.
- **`WorkflowVoice_Azure.speed`** and **`WorkflowVoice_Azure.expressivity`** — new optional fields on the Azure voice variant for controlling speech rate and expressivity.
- **`WorkflowVoice_Vapi.version`** and **`WorkflowVoice_Vapi.language`** — new optional fields on the Vapi voice variant; `voice_id` is now typed as `str` for broader compatibility.

### Breaking Changes
- **`UpdateAssistantDtoCredentialsItem_Trieve`** has been removed from all exports. Remove any imports or type annotations referencing this symbol.
- **`UpdateCampaignDtoStatus`** has been removed from all exports. Replace usages with the new `CampaignControllerFindAllRequestStatus` or `CampaignControllerFindAllV2RequestStatus` enums as appropriate.

### Added
- **New `UpdateAssistantDto` provider variants** — `UpdateAssistantDtoCredentialsItem_Microsoft`, `UpdateAssistantDtoCredentialsItem_S3Compatible`, `UpdateAssistantDtoModel_Vapi`, `UpdateAssistantDtoTranscriber_Vapi`, `UpdateAssistantDtoTranscriber_Xai`, `UpdateAssistantDtoVoice_Microsoft`, and `UpdateAssistantDtoVoice_Xai` are now available as union members.
- **`CreateCallDtoTransport`** union type and its provider variants (`CreateCallDtoTransport_Daily`, `_Telnyx`, `_Twilio`, `_VapiSip`, `_VapiWebsocket`, `_Vonage`) are now exported from the `calls` module.
- **Campaign V2 query enums** — `CampaignControllerFindAllRequestSortBy`, `CampaignControllerFindAllV2RequestSortBy/SortOrder/Status`, and `CampaignControllerGetCampaignV2ContactsRequestSortBy/StatusItem` are now exported.
- **New HTTP error classes** — `ConflictError`, `ForbiddenError`, `InternalServerError`, `PaymentRequiredError`, `ServiceUnavailableError`, and `UnauthorizedError` are now exported from the `errors` module.
- **`CampaignControllerFindAllRequestStatus`** now includes `"cancelled"` and `"archived"` as valid literal values.

### Added
- **`EvalControllerGetPaginatedRequestSortBy`** — new optional `sort_by` parameter on `eval_controller_get_paginated` (sync and async) to control which column results are sorted by, defaulting to `createdAt`.
- **`EvalControllerGetRunsPaginatedRequestSortBy`** — new optional `sort_by` parameter on `eval_controller_get_runs_paginated` (sync and async) for column-level sort control.
- **`search`** — new optional parameter on `eval_controller_get_runs_paginated` (sync and async) for literal, case-insensitive search across eval and assistant names.
- Comprehensive docstrings added to all `EvalClient` and `AsyncEvalClient` methods, including per-parameter descriptions.

### Added
- **`sort_by`** optional parameter on `eval_controller_get_paginated` (sync and async) to control which column eval definitions are sorted by; defaults to `createdAt`.
- **`sort_by`** and **`search`** optional parameters on `eval_controller_get_runs_paginated` (sync and async) to sort eval runs by column and perform a literal, case-insensitive search across eval and assistant names.
- **`ForbiddenError`** is now raised on HTTP 403 responses from all eval and eval-run endpoints, replacing the previous fall-through to a generic `ApiError`.

### Added
- **`sort_by`** optional parameter on `InsightClient.find_all` (and async variant) accepts the new `InsightControllerFindAllRequestSortBy` type to control which column results are sorted by (defaults to `createdAt`).
- **`assistant_id`** optional parameter on `InsightClient.insight_controller_run` (and async variant) scopes call-table queries to a specific assistant at runtime without mutating the saved insight.
- **`sort_by`** optional parameter on `ObservabilityScorecardClient.scorecard_controller_get_paginated` (and async variant) accepts the new `ScorecardControllerGetPaginatedRequestSortBy` type for column-level sort control.
- **`ScorecardControllerGetPaginatedRequestSortBy`** is now exported from the `vapi.observability_scorecard` and `vapi.observability_scorecard.types` packages.
- **`name`** optional field added to `CreateSimulationRunDtoSimulationsItem` simulation variant.

### Added
- **`StructuredOutputsClient.create` / `AsyncStructuredOutputsClient.create`** — new optional `conditions` parameter (`CreateStructuredOutputDtoConditionsItem` sequence) to gate structured-output execution with AND semantics.
- **`StructuredOutputsClient.update` / `AsyncStructuredOutputsClient.update`** — new optional `conditions` parameter (`UpdateStructuredOutputDtoConditionsItem` sequence) to update execution-gate conditions on an existing definition.
- **`StructuredOutputsClient.list` / `AsyncStructuredOutputsClient.list`** — new optional `sort_by` parameter (`StructuredOutputControllerFindAllRequestSortBy`) to control which column results are sorted by (defaults to `createdAt`).

### Changed
- **`StructuredOutputsClient.run` / `AsyncStructuredOutputsClient.run`** — return type changed from `StructuredOutput` to `StructuredOutputControllerRunResponse` to reflect the richer response returned when running a structured output against one or more calls.

### Added
- **`conditions`** — new optional parameter on `create` and `update` in `RawStructuredOutputsClient` and `AsyncRawStructuredOutputsClient` that gates structured-output execution; every condition must pass (AND semantics) for the output to run.
- **`sort_by`** — new optional `StructuredOutputControllerFindAllRequestSortBy` parameter on the `list` endpoints, allowing results to be sorted by a chosen column (defaults to `createdAt`).
- **`StructuredOutputControllerRunResponse`** — the `run` method now returns this dedicated response type instead of `StructuredOutput`, providing richer run result data.
- **New type registrations** — `ConversationNode`, `ToolNode`, `VapiModel`, `WorkflowUserEditable`, `CallHookModelResponseTimeout`, and their related subtypes are now available via the tools module.

### Added
- **`MicrosoftVoice`** and **`MicrosoftCredential`** — new Microsoft TTS voice provider and credential type, available across all assistant, workflow, conversation node, and fallback voice union types.
- **`XaiTranscriber`** and **`XaiVoice`** — new XAI transcriber and voice provider types, including fallback variants (`FallbackXaiTranscriber`, `FallbackXaiVoice`) and discriminator variants across all transcriber/voice unions.
- **`AssistantDraft`**, **`AssistantVersion`**, and related DTOs — full assistant draft and version lifecycle management, including `CreateAssistantDraftDto`, `UpdateAssistantDraftDto`, `AssistantDraftPaginatedResponse`, `AssistantVersionPaginatedResponse`, and conflict response types.
- **`TrafficAllocation`**, **`ToolDraft`**, **`ToolVersion`** — new traffic allocation, tool draft, and tool version management types with full CRUD DTOs, paginated responses, and conflict response types.
- **`Board`**, **`CampaignContact`**, **`CampaignSummary`**, **`KnowledgeBaseV2`**, **`OpenAiReasoner`**, **`S3CompatibleStorageCredential`**, **`SkippedStructuredOutput`**, **`TransferArtifact`**, **`VapiTranscriber`**, and many more new model types across the SDK.
- See full changelog for all changes

### Added
- **`tool_refs`** — new optional field on all model types (`AnthropicModel`, `AnthropicBedrockModel`, `AnyscaleModel`, and others) for version-pinned tool references by `(toolId, version)`.
- **`fallback_models`** — new optional field on `AnthropicBedrockModel` to specify a same-provider Bedrock fallback model tried if the primary fails.
- **`CallHookModelResponseTimeout` / `CallHookModelResponseTimeoutDoItem`** — new call hook types for handling model response timeout events.
- **`ConversationNode`, `ToolNode`, `VapiModel`, `WorkflowUserEditable`** — new workflow node and model types, along with their associated item/helper types, exported from the SDK.
- **`eu-central-1`** added to the `AnthropicBedrockCredentialRegion` supported region literals.

### Changed
- **`temperature` docstring** on all model types updated to reflect a default of `0.5` (previously documented as `0`).

### Added
- **`AssemblyAiTranscriber`** gains `mode`, `prompt`, `agentContext`, `agentContextAutoUpdateEnabled`, and `languageCodes` fields supporting the new Universal Pro speech models (`universal-3-5-pro`, `universal-3-6-pro`).
- **`Artifact`** gains presigned download URL fields (`presignedMonoUrl`, `presignedStereoUrl`, `presignedVideoUrl`, `presignedAssistantUrl`, `presignedCustomerUrl`, `presignedPcapUrl`, `presignedLogUrl`, `presignedUrlsExpiresAt`) and a `skippedStructuredOutputs` map; `transfers` is now typed as `List[TransferArtifact]` instead of `List[str]`.
- **`Assistant`** gains `latestVersion` (version label string) and `modelDeprecations` (list of `ModelDeprecationNotice`) read-only fields.
- **New types** `CallHookModelResponseTimeout`, `ConversationNode`, `ToolNode`, `VapiModel`, `WorkflowUserEditable`, and their associated item/helper types are now exported from the SDK.
- **`ApiRequestTool`** gains a `latestVersion` optional field; `AssemblyAiTranscriberSpeechModel` adds `universal-3-5-pro` and `universal-3-6-pro` literal values.

### Breaking Changes
- **`Call.subscription_limits`** has been removed. Remove any code that reads or type-checks this field.
- **`Call.phone_number`** now has type `TransientTwilioPhoneNumber` instead of `ImportTwilioPhoneNumberDto`. Update any code that constructs or inspects this field.
- **`AssistantVersionPaginatedResponse.next_page_state`** has been removed and `metadata` now uses `AssistantVersionPaginatedMetadata` instead of `PaginationMeta`. Update pagination code accordingly.
- **`TrieveCredentialProvider`** has been renamed to **`AudioFormatContainer`**. Update any imports or type annotations referencing `TrieveCredentialProvider`.

### Added
- **`CallHookModelResponseTimeout`** and **`CallHookModelResponseTimeoutDoItem`** — new hook types for handling model response timeouts during a call.
- **`ConversationNode`**, **`ToolNode`**, **`VapiModel`**, and **`WorkflowUserEditable`** — new workflow node and model types for building structured call workflows.
- **`Call.assistant_version`**, **`Call.squad_version`**, and **`Call.transport`** — new optional fields on `Call` exposing the assistant/squad version used and the typed call transport.
- **`BashTool.latest_version`** — new optional field indicating the latest version of the bash tool.
- **`BarInsight.system_key`** — new optional field exposing the stable server-owned identifier for system-created insights.

### Added
- **`Campaign`** gains new optional fields: `maxConcurrency`, `assistantOverrides`, `squadOverrides`, `server`, `serverMessages`, and `predialPlan` for richer outbound campaign configuration.
- **`SayHookActionExact`** is now a typed model; the `exact` field on Say hook action variants (`CallHookModelResponseTimeoutDoItem_Say`, `CallHookTranscriberEndpointedSpeechLowConfidenceDoItem_Say`) is now `Optional[SayHookActionExact]` instead of `Optional[Dict[str, Any]]`.
- **`CampaignStatus`** now includes `"cancelled"` and `"archived"` as valid literal values.
- **`CartesiaTranscriberModel`** now includes `"ink-2"` as a valid literal value alongside `"ink-whisper"`.

### Added
- **`ConversationNode`**, **`ToolNode`**, and **`WorkflowUserEditable`** — new types for building workflow-driven assistant configurations with node-level model, voice, transcriber, and tool overrides.
- **`VapiModel`** and **`VapiModelToolsItem`** — new model provider option for generating assistant responses via the Vapi model.
- **`CallHookModelResponseTimeout`** and **`CallHookModelResponseTimeoutDoItem`** — new hook types for handling model response timeout events during calls.
- **`tool_refs`** field on `CerebrasModel` — supports version-pinned tool references via `(toolId, version)` pairs; when the same `toolId` appears in both `toolIds` and `tool_refs`, the pinned ref takes precedence.
- **`latest_version`** field on `CodeTool` and `ComputerTool`, and `eu-central-1` region added to `CreateAnthropicBedrockCredentialDtoRegion`.

### Changed
- **`CerebrasModelModel`** — the deprecated `llama-3.3-70b` literal has been removed from the type union; use `llama3.1-8b` or pass a custom string value.

### Breaking Changes
- **`CreateByoSipTrunkCredentialDto.sbc_configuration`** has been removed. Remove any references to `sbc_configuration` when constructing or reading `CreateByoSipTrunkCredentialDto` instances.

### Added
- **`CallHookModelResponseTimeout`** and **`CallHookModelResponseTimeoutDoItem`** — new hook types for handling model response timeout events in call flows.
- **`VapiModel`** and **`VapiModelToolsItem`** — new model types for Vapi-native model configuration.
- **`WorkflowUserEditable`**, **`WorkflowUserEditableHooksItem`**, and **`WorkflowUserEditableNodesItem`** — new types for user-editable workflow definitions.
- **`ConversationNode`**, **`ConversationNodeToolsItem`**, **`ToolNode`**, and **`ToolNodeTool`** — new node types for building structured conversation and tool workflows.

### Breaking Changes
- **`CreateSesameVoiceDto`** — `voice_name` and `transcription` are now required (previously optional), and a new required `file` (`bytes`) field has been added. Update all call sites to supply all three fields.
- **`CreateTrieveCredentialDto`** — `api_key` and `name` fields have been removed and replaced with an optional `provider` field. Remove any code that sets `api_key` or `name` on this DTO.
- **`CreateOutboundCallDto.transport`** — type changed from `Dict[str, Any]` to `CreateOutboundCallDtoTransport`; update any code constructing this field with a raw dict.

### Added
- **`CreateOutboundCallDto`** — new optional `assistant_version` and `squad_version` fields to pin a specific assistant or squad version for a call.
- **`CreateScenarioDto`** — new optional `latency_expectations` field (`List[LatencyExpectation]`) for defining per-turn latency ceilings in voice simulations.
- **New types** — `ConversationNode`, `ToolNode`, `VapiModel`, `WorkflowUserEditable`, `CallHookModelResponseTimeout`, and their companion types are now available across the SDK.

### Added
- **`tool_refs`** — new optional `List[ToolRef]` field on `CustomLlmModel` and `DeepInfraModel` that allows version-pinned tool references by `(toolId, version)`; when the same `toolId` appears in both `toolIds` and `tool_refs`, the `tool_refs` pin takes precedence.
- **`CustomerSpeechTimeoutOptions.trigger_reset_mode`** — new optional field typed as `CustomerSpeechTimeoutOptionsTriggerResetMode` (replaces the previous untyped `Dict[str, Any]`), controlling whether the hook's trigger counter resets after the customer speaks.

### Changed
- **`CreateWorkflowDtoNodesItem`** forward-reference resolution now covers the full dependency graph, including workflow, hook, conversation-node, and tool-node types, improving runtime type resolution for complex workflow configurations.

### Added
- **`VapiModel`**, **`ConversationNode`**, **`ToolNode`**, and **`WorkflowUserEditable`** — new model and workflow node types (with associated `*ToolsItem`, `*HooksItem`, and `*NodesItem` variants) are now exported from the SDK.
- **`CallHookModelResponseTimeout`** and **`CallHookModelResponseTimeoutDoItem`** — new hook types for handling model response timeout events.
- **`DeepSeekModel.tool_refs`** — new optional field for version-pinned tool references (`toolRefs`); also adds `deepseek-flash` and `deepseek-flash-thinking` to `DeepSeekModelModel` literals.
- **`DeepgramTranscriber.redaction`** and **`DeepgramTranscriber.languages`** — new optional fields for PCI/PII/PHI redaction and multilingual language hints; `DeepgramVoiceModel` gains the `flux` literal, and `DeepgramVoice` gains `speed` and `expressivity` fields.

### Changed
- **`ElevenLabsPronunciationDictionaryLocator.version_id`** — is now optional (defaults to the dictionary's latest version); `DtmfTool` and `EndCallTool` gain a new optional `latest_version` field.

### Added
- **`FallbackAssemblyAiTranscriber`** gains `mode`, `prompt`, `agent_context`, `agent_context_auto_update_enabled`, and `language_codes` fields, plus `universal-3-5-pro` and `universal-3-6-pro` speech model options.
- **`FallbackDeepgramTranscriber`** gains a `redaction` field for PCI/PII/PHI/number redaction and a `languages` field for multilingual Flux hints; **`FallbackDeepgramVoice`** gains `speed` and `expressivity` fields and a new `flux` model option.
- **`FallbackSonioxTranscriber`** gains `languages`, `endpoint_sensitivity`, `endpoint_latency_adjustment_level`, `context_general`, and `confidence_threshold` fields, plus the `stt-rt-v5` model option.
- **`EvaluationPlanItem`** gains an optional `path` field for dot-notation access to primitive leaves within object structured outputs.
- **New enum/literal values** added: `ink-2` for `FallbackCartesiaTranscriberModel`, `coda` and `mistv3` for `FallbackRimeAiVoiceModel`, and 17 additional voice IDs (e.g. `ash`, `coral`, `quartz`, `willow`) for `FallbackOpenAiVoiceIdEnum`.

### Added
- **`latest_version`** — new optional field added to all reusable tool types (`FunctionTool`, `GhlTool`, `GoHighLevelCalendarAvailabilityTool`, `GoHighLevelCalendarEventCreateTool`, `GoHighLevelContactCreateTool`, `GoHighLevelContactGetTool`, `GoogleCalendarCheckAvailabilityTool`, `GoogleCalendarCreateEventTool`) to track the tool's latest version.
- **`FallbackVapiVoice.version`** and **`FallbackVapiVoice.language`** — new optional fields for selecting the Vapi voice routing generation and synthesis language.
- **`GetEvalRunPaginatedDto.sort_by`** and **`GetEvalRunPaginatedDto.search`** — new optional fields for sorting and filtering eval run pagination results.

### Changed
- **`FallbackTranscriberPlan.transcribers`** — changed from required to optional (defaults to `None`); existing code that always provided this field is unaffected.
- **`FallbackVapiVoice.voice_id`** — type widened from `FallbackVapiVoiceVoiceId` to `str`, accepting any voice name or cloned voice ID.

### Added
- **`tool_refs`** — new optional field on `GoogleModel`, `GroqModel`, and `InflectionAiModel` for version-pinned tool references; each entry pins a specific `(toolId, version)` pair and takes precedence over `toolIds` when the same tool appears in both.
- **`VapiModel`** and **`VapiModelToolsItem`** — new model configuration types for Vapi-native assistant responses.
- **`WorkflowUserEditable`**, **`WorkflowUserEditableHooksItem`**, and **`WorkflowUserEditableNodesItem`** — new types for workflow-based assistant configuration.
- **`ConversationNode`**, **`ConversationNodeToolsItem`**, **`ToolNode`**, and **`ToolNodeTool`** — new workflow node types for conversation and tool steps.
- **`CallHookModelResponseTimeout`** and **`CallHookModelResponseTimeoutDoItem`** — new call hook types triggered when a model response exceeds its timeout.

### Changed
- **`latest_version`** — new optional field added to `GoogleSheetsRowAppendTool` and `HandoffTool` to track the latest published version of a reusable tool.
- **`temperature` docstring** on `GoogleModel`, `GroqModel`, and `InflectionAiModel` updated to reflect a default of `0.5` (previously documented as `0`).

### Added
- **`ConversationNode`**, **`ToolNode`**, **`WorkflowUserEditable`**, and their associated subtypes for workflow-based assistant configuration.
- **`VapiModel`** and **`VapiModelToolsItem`** as a new LLM backend option.
- **`CallHookModelResponseTimeout`** and **`CallHookModelResponseTimeoutDoItem`** for handling model-response-timeout call hooks.
- **`tool_refs`** (`toolRefs`) optional field on `MinimaxLlmModel` for version-pinned tool references via `ToolRef`.
- **`latest_version`** optional field on `MakeTool` and `McpTool`; **`system_key`** optional field on `LineInsight`; `InviteUserDtoRole` now backed by the new **`InviteUserDtoRoleZero`** enum.

### Added
- **`OpenAiModel.speaker`** and **`OpenAiModel.reasoner`** — new optional fields for configuring GPT-Live speaker and reasoner settings.
- **`OpenAiModel.service_tier`** and **`OpenAiModel.reasoning_effort`** — new optional fields to control OpenAI service tier (fast/auto/default) and reasoning effort for reasoning-capable models.
- **`OpenAiModel.tool_refs`** and **`OpenRouterModel.tool_refs`** — new optional field for version-pinned tool references by `(toolId, version)`.
- **`OpenAiVoiceIdEnum`** — expanded with 17 new GPT-Live voice literals including `quartz`, `ripple`, `vesper`, `willow`, `stone`, `gleam`, `meridian`, `bossa`, `tempo`, `beacon`, `delta`, `cinder`, `ash`, `ballad`, `coral`, `sage`, and `verse`.
- **New types** `ConversationNode`, `ToolNode`, `VapiModel`, `WorkflowUserEditable`, `CallHookModelResponseTimeout`, `OpenAiReasoner`, `OpenAiSpeaker`, `OpenAiModelServiceTier`, `OpenAiModelReasoningEffort`, and `ToolRef` are now publicly exported.

### Changed
- **`PaginationMeta`** — adds optional `total_pages`, `has_next_page`, `next_cursor` (opaque cursor for keyset pagination), and `sort_order` fields to support cursor-based pagination.

## 2.0.0 - 2026-06-24
### Breaking Changes
* **`CartesiaExperimentalControlsSpeedZero`** has been removed and replaced by **`CartesiaSpeedControlZero`**. Update any imports or type annotations referencing `CartesiaExperimentalControlsSpeedZero` to use `CartesiaSpeedControlZero` instead.
* **`FallbackAzureVoiceVoiceIdZero`** has been removed and replaced by **`FallbackAzureVoiceIdZero`**. Update any imports or type annotations referencing `FallbackAzureVoiceVoiceIdZero` to use `FallbackAzureVoiceIdZero` instead.

## 1.11.1 - 2026-05-20
* chore: remove redundant content-type headers from raw clients
* Remove explicitly set `"content-type": "application/json"` headers from
* multiple raw client request calls across the SDK. These headers are
* already handled by the underlying HTTP client when a JSON body is
* present, making the explicit declarations redundant.
* Key changes:
* Remove hardcoded `content-type: application/json` headers from `RawAssistantsClient` and `AsyncRawAssistantsClient`
* Remove same redundant headers from `RawEvalClient`, `RawInsightClient`, `RawObservabilityScorecardClient`, `RawPhoneNumbersClient`, `RawSquadsClient`, `RawStructuredOutputsClient`, and `RawToolsClient`
* Applies to both sync and async variants of all affected clients
* 🌿 Generated with Fern

## 1.11.0 - 2026-04-22
### Added
* **`Call.subscription_limits`** — new optional field that exposes the org's `SubscriptionLimits` (including concurrency limit information) at the time of a call.

## 1.10.0 - 2026-04-10
* The SDK now supports `aiohttp` as an optional async HTTP transport backend. Install the new extra (`pip install vapi_server_sdk[aiohttp]`) to have `AsyncVapi` automatically use `httpx-aiohttp` under the hood. Two new convenience classes, `DefaultAioHttpClient` and `DefaultAsyncHttpxClient`, are also now available for users who want to configure the async HTTP client explicitly.

## 1.9.1 - 2026-04-07
* SDK regeneration
* Unable to analyze changes with AI, incrementing PATCH version.

