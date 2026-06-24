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

