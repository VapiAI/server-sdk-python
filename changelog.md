## 3.0.0 - Unreleased

### Breaking Changes

This release regenerates the Python SDK from the current Vapi API definition. The migration notes below compare 3.0.0 with the published 1.11.1 package. Client method names and parameters remain available, but public helper imports, model field declarations, and two return annotations change.

#### Update renamed helper imports

Update imports and type annotations that use these names:

| Previous helper | Current helper |
| --- | --- |
| `CartesiaExperimentalControlsSpeedZero` | `CartesiaSpeedControlZero` |
| `FallbackAzureVoiceVoiceIdZero` | `FallbackAzureVoiceIdZero` |
| `GladiaTranscriberLanguages` | `GladiaTranscriberLanguagesItem` |
| `FallbackGladiaTranscriberLanguages` | `FallbackGladiaTranscriberLanguagesItem` |

`VapiVoice.voice_id` and `FallbackVapiVoice.voice_id` now use strings instead of the removed voice-ID helper types. Pass a supported voice ID directly. The OpenAI voice-ID helpers combine the current named voice choices with strings; voice availability depends on the selected model.

Gladia `languages` fields now use a list of language codes, such as `["en", "fr"]`. The new `LanguagesItem` helpers describe one element of that list, including in embedded assistant, workflow, and fallback transcriber configurations.

#### Use tagged Vapi request models

For assistant requests using `provider="vapi"`, use the request-specific model type. The standalone `VapiModel` no longer declares or defaults `provider`. The tagged request type supplies the discriminator required by the assistant request union.

```python
import os

from vapi import Vapi
from vapi.types.create_assistant_dto_model import CreateAssistantDtoModel_Vapi

client = Vapi(token=os.environ["VAPI_API_KEY"])
assistant = client.assistants.create(
    model=CreateAssistantDtoModel_Vapi(version="latest"),
)
print(assistant.id)
```

For `client.assistants.update()`, use `UpdateAssistantDtoModel_Vapi` from `vapi.assistants.types.update_assistant_dto_model`. For `AssistantOverrides.model`, use `AssistantOverridesModel_Vapi` from `vapi.types.assistant_overrides_model`.

#### Handle structured-output run responses

The sync and async `structured_output_controller_run()` methods return `StructuredOutputControllerRunResponse`, a union of preview and rerun response models. They no longer declare a `StructuredOutput` return type.

Use `preview_enabled=True` to preview one call without updating its artifacts. A rerun response is a `StructuredOutputRerunResponse` with a `message` and an optional `workflow_id`. A preview response contains output-ID keys and an optional `skipped` field.

```python
import os

from vapi import Vapi
from vapi.types.structured_output_rerun_response import StructuredOutputRerunResponse

client = Vapi(token=os.environ["VAPI_API_KEY"])
result = client.structured_outputs.structured_output_controller_run(
    call_ids=["YOUR_CALL_ID"],
    structured_output_id="YOUR_STRUCTURED_OUTPUT_ID",
    preview_enabled=True,
)
if isinstance(result, StructuredOutputRerunResponse):
    print(result.message, result.workflow_id)
else:
    print(result)
```

Replace both IDs with a call and saved structured output in your organization. See the [Run Structured Output API reference](https://docs.vapi.ai/api-reference/structured-outputs/structured-output-controller-run) for preview and rerun behavior.

#### Update simulation request construction

The removed simulation DTO helper classes below are no longer public imports. Supply request values through the corresponding client method's named parameters. For example, `client.simulation_suites.simulation_suite_controller_create()` accepts `name` and `simulation_ids`; `client.simulation_scenarios.scenario_controller_create()` accepts `name`, `instructions`, and `evaluations`.

#### Review changed model field declarations

The following fields are no longer declared on the listed models. Recheck code that accesses the Python field name or relies on its type or alias. Response properties outside the declared model fields can still be preserved as extra data under their wire names.

`AssistantVersionPaginatedResponse.metadata` now uses `AssistantVersionPaginatedMetadata`, with `next_cursor`, `has_next_page`, and `limit`. Its `results` are typed as `AssistantVersion` objects.

When constructing `CreateSesameVoiceDto` directly, supply `file`, `voice_name`, and `transcription`. `file` is a new required bytes field; `voice_name` and `transcription` are now required strings. `SimulationSuite` now declares a required `target_assignments` list. These model declarations do not add required parameters to existing client methods.

Several fields now use specific model types instead of generic dictionaries or strings:

| Field | Current type |
| --- | --- |
| `Artifact.transfers` | Optional list of `TransferArtifact` objects, rather than strings |
| `Call.phone_number` | Optional `TransientTwilioPhoneNumber`, rather than `ImportTwilioPhoneNumberDto` |
| `Call.transport` | Optional `CallTransport` |
| `CreateOutboundCallDto.transport` | Optional `CreateOutboundCallDtoTransport` |
| `SayHookAction.exact` and embedded say-hook actions | Optional `SayHookActionExact` |
| `CustomerSpeechTimeoutOptions.trigger_reset_mode` | Optional `CustomerSpeechTimeoutOptionsTriggerResetMode` |
| `ScorecardMetric.conditions` | List of `ScorecardMetricConditionsItem` |
| `RecordingConsent.type` | `RecordingConsentType` |
| `VoiceLibraryVoiceResponse.age` | Optional `VoiceLibraryVoiceResponseAge` |
| `ToolCallResult.message` | Optional `ToolCallResultSpokenMessage`, rather than `ToolCallResultMessage` |
| `UserMessage.metadata` | Optional `UserMessageMetadata` |

Update type annotations and code that expects dictionary indexing or string transfer values. `ElevenLabsPronunciationDictionaryLocator.version_id`, `FallbackTranscriberPlan.transcribers`, and `VapiModel.model` now allow `None`.

| Removed declared field | Affected models |
| --- | --- |
| `eager_eot_threshold` | `AssistantOverridesTranscriber_Deepgram`, `AssistantTranscriber_Deepgram`, `ConversationNodeTranscriber_Deepgram`, `CreateAssistantDtoTranscriber_Deepgram`, `CreateWorkflowDtoTranscriber_Deepgram`, `DeepgramTranscriber`, `FallbackDeepgramTranscriber`, `FallbackTranscriberPlanTranscribersItem_Deepgram`, `TransferAssistantTranscriber_Deepgram`, `UpdateAssistantDtoTranscriber_Deepgram`, `UpdateWorkflowDtoTranscriber_Deepgram`, `WorkflowTranscriber_Deepgram`, `WorkflowUserEditableTranscriber_Deepgram` |
| `fallback_plan` | `AssistantOverridesVoice_Vapi`, `AssistantVoice_Vapi`, `ConversationNodeVoice_Vapi`, `CreateAssistantDtoVoice_Vapi`, `CreateWorkflowDtoVoice_Vapi`, `RecordingConsentPlanStayOnLineVoice_Vapi`, `RecordingConsentPlanVerbalVoice_Vapi`, `TransferAssistantVoice_Vapi`, `UpdateAssistantDtoVoice_Vapi`, `UpdateWorkflowDtoVoice_Vapi`, `VapiVoice`, `WorkflowUserEditableVoice_Vapi`, `WorkflowVoice_Vapi` |
| `max_tokens` | `VapiModel` |
| `next_page_state` | `AssistantVersionPaginatedResponse` |
| `provider` | `VapiModel` |
| `sbc_configuration` | `AssistantCredentialsItem_ByoSipTrunk`, `AssistantOverridesCredentialsItem_ByoSipTrunk`, `ByoSipTrunkCredential`, `CreateAssistantDtoCredentialsItem_ByoSipTrunk`, `CreateByoSipTrunkCredentialDto`, `CreateWorkflowDtoCredentialsItem_ByoSipTrunk`, `UpdateAssistantDtoCredentialsItem_ByoSipTrunk`, `UpdateByoSipTrunkCredentialDto`, `UpdateWorkflowDtoCredentialsItem_ByoSipTrunk`, `WorkflowCredentialsItem_ByoSipTrunk`, `WorkflowUserEditableCredentialsItem_ByoSipTrunk` |
| `slack_channel_id` | `Subscription` |
| `slack_support_enabled` | `Subscription` |
| `subscription_limits` | `Call` |
| `type` | `GhlTool` |

Trieve credential and knowledge-base types are no longer included in this SDK. This includes `CreateTrieveCredentialDto`, `CreateTrieveKnowledgeBaseDto`, `UpdateTrieveKnowledgeBaseDto`, `TrieveKnowledgeBase`, and `TrieveKnowledgeBaseImport`. No compatibility aliases or replacement Trieve models are provided. The current public API definition does not include Trieve schemas. If your integration constructs these types, verify that integration's request format before upgrading.

#### Removed public imports

The following names were exported by 1.11.1 and are absent from 3.0.0. The helper migrations above cover names with verified alternatives:

- `AssistantCredentialsItem_Trieve`
- `AssistantOverridesCredentialsItem_Trieve`
- `CartesiaExperimentalControlsSpeedZero`
- `CreateAssistantDtoCredentialsItem_Trieve`
- `CreateSimulationDto`
- `CreateSimulationRunDto`
- `CreateSimulationSuiteDto`
- `CreateTrieveCredentialDto`
- `CreateTrieveKnowledgeBaseDto`
- `CreateTrieveKnowledgeBaseDtoProvider`
- `CreateWorkflowDtoCredentialsItem_Trieve`
- `FallbackAzureVoiceVoiceIdZero`
- `FallbackGladiaTranscriberLanguages`
- `FallbackVapiVoiceVoiceId`
- `GenerateScenariosDto`
- `GhlToolType`
- `GladiaTranscriberLanguages`
- `TrieveCredential`
- `TrieveCredentialProvider`
- `TrieveKnowledgeBase`
- `TrieveKnowledgeBaseChunkPlan`
- `TrieveKnowledgeBaseCreate`
- `TrieveKnowledgeBaseCreateType`
- `TrieveKnowledgeBaseImport`
- `TrieveKnowledgeBaseImportType`
- `TrieveKnowledgeBaseProvider`
- `TrieveKnowledgeBaseSearchPlan`
- `TrieveKnowledgeBaseSearchPlanSearchType`
- `UpdateAssistantDtoCredentialsItem_Trieve`
- `UpdatePersonalityDto`
- `UpdateScenarioDto`
- `UpdateSimulationDto`
- `UpdateSimulationSuiteDto`
- `UpdateTrieveCredentialDto`
- `UpdateTrieveKnowledgeBaseDto`
- `UpdateWorkflowDtoCredentialsItem_Trieve`
- `VapiModelProvider`
- `VapiVoiceVoiceId`
- `WorkflowCredentialsItem_Trieve`
- `WorkflowUserEditableCredentialsItem_Trieve`

### Added

- Regenerated API types and methods from the current public API definition.
- `with_raw_response` accessors for response status, headers, and parsed data.
- Current model deprecation notices, including `replacement_status` and optional `replacement_model`.

### Fixed

- Structured-output rerun parsing preserves `workflow_id`, including responses without a workflow ID.
- Code-tool request unions and GHL-tool response unions include their schema discriminator mappings.
- Assistant server-message type hints include the current event names from the API definition.

### Compatibility

- Supported and locally tested Python versions: 3.10 through 3.14.
- Local regression checks cover Pydantic 1 and 2 and the optional `aiohttp` transport.

## [2.0.1] - 2026-10-07

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

