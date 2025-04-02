# This file was auto-generated by Fern from our API Definition.

import typing

ServerMessageEndOfCallReportEndedReason = typing.Union[
    typing.Literal[
        "call-start-error-neither-assistant-nor-server-set",
        "assistant-request-failed",
        "assistant-request-returned-error",
        "assistant-request-returned-unspeakable-error",
        "assistant-request-returned-invalid-assistant",
        "assistant-request-returned-no-assistant",
        "assistant-request-returned-forwarding-phone-number",
        "call.start.error-get-org",
        "call.start.error-get-subscription",
        "call.start.error-get-assistant",
        "call.start.error-get-phone-number",
        "call.start.error-get-customer",
        "call.start.error-get-resources-validation",
        "call.start.error-vapi-number-international",
        "call.start.error-vapi-number-outbound-daily-limit",
        "call.start.error-get-transport",
        "assistant-not-valid",
        "database-error",
        "assistant-not-found",
        "pipeline-error-openai-voice-failed",
        "pipeline-error-cartesia-voice-failed",
        "pipeline-error-deepgram-voice-failed",
        "pipeline-error-eleven-labs-voice-failed",
        "pipeline-error-playht-voice-failed",
        "pipeline-error-lmnt-voice-failed",
        "pipeline-error-azure-voice-failed",
        "pipeline-error-rime-ai-voice-failed",
        "pipeline-error-smallest-ai-voice-failed",
        "pipeline-error-neuphonic-voice-failed",
        "pipeline-error-hume-voice-failed",
        "pipeline-error-sesame-voice-failed",
        "pipeline-error-tavus-video-failed",
        "call.in-progress.error-vapifault-openai-voice-failed",
        "call.in-progress.error-vapifault-cartesia-voice-failed",
        "call.in-progress.error-vapifault-deepgram-voice-failed",
        "call.in-progress.error-vapifault-eleven-labs-voice-failed",
        "call.in-progress.error-vapifault-playht-voice-failed",
        "call.in-progress.error-vapifault-lmnt-voice-failed",
        "call.in-progress.error-vapifault-azure-voice-failed",
        "call.in-progress.error-vapifault-rime-ai-voice-failed",
        "call.in-progress.error-vapifault-smallest-ai-voice-failed",
        "call.in-progress.error-vapifault-neuphonic-voice-failed",
        "call.in-progress.error-vapifault-hume-voice-failed",
        "call.in-progress.error-vapifault-sesame-voice-failed",
        "call.in-progress.error-vapifault-tavus-video-failed",
        "pipeline-error-vapi-llm-failed",
        "pipeline-error-vapi-400-bad-request-validation-failed",
        "pipeline-error-vapi-401-unauthorized",
        "pipeline-error-vapi-403-model-access-denied",
        "pipeline-error-vapi-429-exceeded-quota",
        "pipeline-error-vapi-500-server-error",
        "pipeline-error-vapi-503-server-overloaded-error",
        "call.in-progress.error-vapifault-vapi-llm-failed",
        "call.in-progress.error-vapifault-vapi-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-vapi-401-unauthorized",
        "call.in-progress.error-vapifault-vapi-403-model-access-denied",
        "call.in-progress.error-vapifault-vapi-429-exceeded-quota",
        "call.in-progress.error-providerfault-vapi-500-server-error",
        "call.in-progress.error-providerfault-vapi-503-server-overloaded-error",
        "pipeline-error-deepgram-transcriber-failed",
        "call.in-progress.error-vapifault-deepgram-transcriber-failed",
        "pipeline-error-gladia-transcriber-failed",
        "call.in-progress.error-vapifault-gladia-transcriber-failed",
        "pipeline-error-speechmatics-transcriber-failed",
        "call.in-progress.error-vapifault-speechmatics-transcriber-failed",
        "pipeline-error-assembly-ai-transcriber-failed",
        "pipeline-error-assembly-ai-returning-400-insufficent-funds",
        "pipeline-error-assembly-ai-returning-400-paid-only-feature",
        "pipeline-error-assembly-ai-returning-401-invalid-credentials",
        "pipeline-error-assembly-ai-returning-500-invalid-schema",
        "pipeline-error-assembly-ai-returning-500-word-boost-parsing-failed",
        "call.in-progress.error-vapifault-assembly-ai-transcriber-failed",
        "call.in-progress.error-vapifault-assembly-ai-returning-400-insufficent-funds",
        "call.in-progress.error-vapifault-assembly-ai-returning-400-paid-only-feature",
        "call.in-progress.error-vapifault-assembly-ai-returning-401-invalid-credentials",
        "call.in-progress.error-vapifault-assembly-ai-returning-500-invalid-schema",
        "call.in-progress.error-vapifault-assembly-ai-returning-500-word-boost-parsing-failed",
        "pipeline-error-talkscriber-transcriber-failed",
        "call.in-progress.error-vapifault-talkscriber-transcriber-failed",
        "pipeline-error-azure-speech-transcriber-failed",
        "call.in-progress.error-vapifault-azure-speech-transcriber-failed",
        "call.in-progress.error-pipeline-no-available-llm-model",
        "worker-shutdown",
        "unknown-error",
        "vonage-disconnected",
        "vonage-failed-to-connect-call",
        "vonage-completed",
        "phone-call-provider-bypass-enabled-but-no-call-received",
        "call.in-progress.error-vapifault-transport-never-connected",
        "call.in-progress.error-vapifault-transport-connected-but-call-not-active",
        "call.in-progress.error-vapifault-call-started-but-connection-to-transport-missing",
        "call.in-progress.error-vapifault-openai-llm-failed",
        "call.in-progress.error-vapifault-azure-openai-llm-failed",
        "call.in-progress.error-vapifault-groq-llm-failed",
        "call.in-progress.error-vapifault-google-llm-failed",
        "call.in-progress.error-vapifault-xai-llm-failed",
        "call.in-progress.error-vapifault-mistral-llm-failed",
        "call.in-progress.error-vapifault-inflection-ai-llm-failed",
        "call.in-progress.error-vapifault-cerebras-llm-failed",
        "call.in-progress.error-vapifault-deep-seek-llm-failed",
        "pipeline-error-openai-400-bad-request-validation-failed",
        "pipeline-error-openai-401-unauthorized",
        "pipeline-error-openai-401-incorrect-api-key",
        "pipeline-error-openai-401-account-not-in-organization",
        "pipeline-error-openai-403-model-access-denied",
        "pipeline-error-openai-429-exceeded-quota",
        "pipeline-error-openai-429-rate-limit-reached",
        "pipeline-error-openai-500-server-error",
        "pipeline-error-openai-503-server-overloaded-error",
        "pipeline-error-openai-llm-failed",
        "call.in-progress.error-vapifault-openai-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-openai-401-unauthorized",
        "call.in-progress.error-vapifault-openai-401-incorrect-api-key",
        "call.in-progress.error-vapifault-openai-401-account-not-in-organization",
        "call.in-progress.error-vapifault-openai-403-model-access-denied",
        "call.in-progress.error-vapifault-openai-429-exceeded-quota",
        "call.in-progress.error-vapifault-openai-429-rate-limit-reached",
        "call.in-progress.error-providerfault-openai-500-server-error",
        "call.in-progress.error-providerfault-openai-503-server-overloaded-error",
        "pipeline-error-azure-openai-400-bad-request-validation-failed",
        "pipeline-error-azure-openai-401-unauthorized",
        "pipeline-error-azure-openai-403-model-access-denied",
        "pipeline-error-azure-openai-429-exceeded-quota",
        "pipeline-error-azure-openai-500-server-error",
        "pipeline-error-azure-openai-503-server-overloaded-error",
        "pipeline-error-azure-openai-llm-failed",
        "call.in-progress.error-vapifault-azure-openai-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-azure-openai-401-unauthorized",
        "call.in-progress.error-vapifault-azure-openai-403-model-access-denied",
        "call.in-progress.error-vapifault-azure-openai-429-exceeded-quota",
        "call.in-progress.error-providerfault-azure-openai-500-server-error",
        "call.in-progress.error-providerfault-azure-openai-503-server-overloaded-error",
        "pipeline-error-google-400-bad-request-validation-failed",
        "pipeline-error-google-401-unauthorized",
        "pipeline-error-google-403-model-access-denied",
        "pipeline-error-google-429-exceeded-quota",
        "pipeline-error-google-500-server-error",
        "pipeline-error-google-503-server-overloaded-error",
        "pipeline-error-google-llm-failed",
        "call.in-progress.error-vapifault-google-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-google-401-unauthorized",
        "call.in-progress.error-vapifault-google-403-model-access-denied",
        "call.in-progress.error-vapifault-google-429-exceeded-quota",
        "call.in-progress.error-providerfault-google-500-server-error",
        "call.in-progress.error-providerfault-google-503-server-overloaded-error",
        "pipeline-error-xai-400-bad-request-validation-failed",
        "pipeline-error-xai-401-unauthorized",
        "pipeline-error-xai-403-model-access-denied",
        "pipeline-error-xai-429-exceeded-quota",
        "pipeline-error-xai-500-server-error",
        "pipeline-error-xai-503-server-overloaded-error",
        "pipeline-error-xai-llm-failed",
        "call.in-progress.error-vapifault-xai-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-xai-401-unauthorized",
        "call.in-progress.error-vapifault-xai-403-model-access-denied",
        "call.in-progress.error-vapifault-xai-429-exceeded-quota",
        "call.in-progress.error-providerfault-xai-500-server-error",
        "call.in-progress.error-providerfault-xai-503-server-overloaded-error",
        "pipeline-error-mistral-400-bad-request-validation-failed",
        "pipeline-error-mistral-401-unauthorized",
        "pipeline-error-mistral-403-model-access-denied",
        "pipeline-error-mistral-429-exceeded-quota",
        "pipeline-error-mistral-500-server-error",
        "pipeline-error-mistral-503-server-overloaded-error",
        "pipeline-error-mistral-llm-failed",
        "call.in-progress.error-vapifault-mistral-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-mistral-401-unauthorized",
        "call.in-progress.error-vapifault-mistral-403-model-access-denied",
        "call.in-progress.error-vapifault-mistral-429-exceeded-quota",
        "call.in-progress.error-providerfault-mistral-500-server-error",
        "call.in-progress.error-providerfault-mistral-503-server-overloaded-error",
        "pipeline-error-inflection-ai-400-bad-request-validation-failed",
        "pipeline-error-inflection-ai-401-unauthorized",
        "pipeline-error-inflection-ai-403-model-access-denied",
        "pipeline-error-inflection-ai-429-exceeded-quota",
        "pipeline-error-inflection-ai-500-server-error",
        "pipeline-error-inflection-ai-503-server-overloaded-error",
        "pipeline-error-inflection-ai-llm-failed",
        "call.in-progress.error-vapifault-inflection-ai-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-inflection-ai-401-unauthorized",
        "call.in-progress.error-vapifault-inflection-ai-403-model-access-denied",
        "call.in-progress.error-vapifault-inflection-ai-429-exceeded-quota",
        "call.in-progress.error-providerfault-inflection-ai-500-server-error",
        "call.in-progress.error-providerfault-inflection-ai-503-server-overloaded-error",
        "pipeline-error-deep-seek-400-bad-request-validation-failed",
        "pipeline-error-deep-seek-401-unauthorized",
        "pipeline-error-deep-seek-403-model-access-denied",
        "pipeline-error-deep-seek-429-exceeded-quota",
        "pipeline-error-deep-seek-500-server-error",
        "pipeline-error-deep-seek-503-server-overloaded-error",
        "pipeline-error-deep-seek-llm-failed",
        "call.in-progress.error-vapifault-deep-seek-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-deep-seek-401-unauthorized",
        "call.in-progress.error-vapifault-deep-seek-403-model-access-denied",
        "call.in-progress.error-vapifault-deep-seek-429-exceeded-quota",
        "call.in-progress.error-providerfault-deep-seek-500-server-error",
        "call.in-progress.error-providerfault-deep-seek-503-server-overloaded-error",
        "pipeline-error-groq-400-bad-request-validation-failed",
        "pipeline-error-groq-401-unauthorized",
        "pipeline-error-groq-403-model-access-denied",
        "pipeline-error-groq-429-exceeded-quota",
        "pipeline-error-groq-500-server-error",
        "pipeline-error-groq-503-server-overloaded-error",
        "pipeline-error-groq-llm-failed",
        "call.in-progress.error-vapifault-groq-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-groq-401-unauthorized",
        "call.in-progress.error-vapifault-groq-403-model-access-denied",
        "call.in-progress.error-vapifault-groq-429-exceeded-quota",
        "call.in-progress.error-providerfault-groq-500-server-error",
        "call.in-progress.error-providerfault-groq-503-server-overloaded-error",
        "pipeline-error-cerebras-400-bad-request-validation-failed",
        "pipeline-error-cerebras-401-unauthorized",
        "pipeline-error-cerebras-403-model-access-denied",
        "pipeline-error-cerebras-429-exceeded-quota",
        "pipeline-error-cerebras-500-server-error",
        "pipeline-error-cerebras-503-server-overloaded-error",
        "pipeline-error-cerebras-llm-failed",
        "call.in-progress.error-vapifault-cerebras-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-cerebras-401-unauthorized",
        "call.in-progress.error-vapifault-cerebras-403-model-access-denied",
        "call.in-progress.error-vapifault-cerebras-429-exceeded-quota",
        "call.in-progress.error-providerfault-cerebras-500-server-error",
        "call.in-progress.error-providerfault-cerebras-503-server-overloaded-error",
        "pipeline-error-anthropic-400-bad-request-validation-failed",
        "pipeline-error-anthropic-401-unauthorized",
        "pipeline-error-anthropic-403-model-access-denied",
        "pipeline-error-anthropic-429-exceeded-quota",
        "pipeline-error-anthropic-500-server-error",
        "pipeline-error-anthropic-503-server-overloaded-error",
        "pipeline-error-anthropic-llm-failed",
        "call.in-progress.error-vapifault-anthropic-llm-failed",
        "call.in-progress.error-vapifault-anthropic-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-anthropic-401-unauthorized",
        "call.in-progress.error-vapifault-anthropic-403-model-access-denied",
        "call.in-progress.error-vapifault-anthropic-429-exceeded-quota",
        "call.in-progress.error-providerfault-anthropic-500-server-error",
        "call.in-progress.error-providerfault-anthropic-503-server-overloaded-error",
        "pipeline-error-together-ai-400-bad-request-validation-failed",
        "pipeline-error-together-ai-401-unauthorized",
        "pipeline-error-together-ai-403-model-access-denied",
        "pipeline-error-together-ai-429-exceeded-quota",
        "pipeline-error-together-ai-500-server-error",
        "pipeline-error-together-ai-503-server-overloaded-error",
        "pipeline-error-together-ai-llm-failed",
        "call.in-progress.error-vapifault-together-ai-llm-failed",
        "call.in-progress.error-vapifault-together-ai-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-together-ai-401-unauthorized",
        "call.in-progress.error-vapifault-together-ai-403-model-access-denied",
        "call.in-progress.error-vapifault-together-ai-429-exceeded-quota",
        "call.in-progress.error-providerfault-together-ai-500-server-error",
        "call.in-progress.error-providerfault-together-ai-503-server-overloaded-error",
        "pipeline-error-anyscale-400-bad-request-validation-failed",
        "pipeline-error-anyscale-401-unauthorized",
        "pipeline-error-anyscale-403-model-access-denied",
        "pipeline-error-anyscale-429-exceeded-quota",
        "pipeline-error-anyscale-500-server-error",
        "pipeline-error-anyscale-503-server-overloaded-error",
        "pipeline-error-anyscale-llm-failed",
        "call.in-progress.error-vapifault-anyscale-llm-failed",
        "call.in-progress.error-vapifault-anyscale-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-anyscale-401-unauthorized",
        "call.in-progress.error-vapifault-anyscale-403-model-access-denied",
        "call.in-progress.error-vapifault-anyscale-429-exceeded-quota",
        "call.in-progress.error-providerfault-anyscale-500-server-error",
        "call.in-progress.error-providerfault-anyscale-503-server-overloaded-error",
        "pipeline-error-openrouter-400-bad-request-validation-failed",
        "pipeline-error-openrouter-401-unauthorized",
        "pipeline-error-openrouter-403-model-access-denied",
        "pipeline-error-openrouter-429-exceeded-quota",
        "pipeline-error-openrouter-500-server-error",
        "pipeline-error-openrouter-503-server-overloaded-error",
        "pipeline-error-openrouter-llm-failed",
        "call.in-progress.error-vapifault-openrouter-llm-failed",
        "call.in-progress.error-vapifault-openrouter-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-openrouter-401-unauthorized",
        "call.in-progress.error-vapifault-openrouter-403-model-access-denied",
        "call.in-progress.error-vapifault-openrouter-429-exceeded-quota",
        "call.in-progress.error-providerfault-openrouter-500-server-error",
        "call.in-progress.error-providerfault-openrouter-503-server-overloaded-error",
        "pipeline-error-perplexity-ai-400-bad-request-validation-failed",
        "pipeline-error-perplexity-ai-401-unauthorized",
        "pipeline-error-perplexity-ai-403-model-access-denied",
        "pipeline-error-perplexity-ai-429-exceeded-quota",
        "pipeline-error-perplexity-ai-500-server-error",
        "pipeline-error-perplexity-ai-503-server-overloaded-error",
        "pipeline-error-perplexity-ai-llm-failed",
        "call.in-progress.error-vapifault-perplexity-ai-llm-failed",
        "call.in-progress.error-vapifault-perplexity-ai-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-perplexity-ai-401-unauthorized",
        "call.in-progress.error-vapifault-perplexity-ai-403-model-access-denied",
        "call.in-progress.error-vapifault-perplexity-ai-429-exceeded-quota",
        "call.in-progress.error-providerfault-perplexity-ai-500-server-error",
        "call.in-progress.error-providerfault-perplexity-ai-503-server-overloaded-error",
        "pipeline-error-deepinfra-400-bad-request-validation-failed",
        "pipeline-error-deepinfra-401-unauthorized",
        "pipeline-error-deepinfra-403-model-access-denied",
        "pipeline-error-deepinfra-429-exceeded-quota",
        "pipeline-error-deepinfra-500-server-error",
        "pipeline-error-deepinfra-503-server-overloaded-error",
        "pipeline-error-deepinfra-llm-failed",
        "call.in-progress.error-vapifault-deepinfra-llm-failed",
        "call.in-progress.error-vapifault-deepinfra-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-deepinfra-401-unauthorized",
        "call.in-progress.error-vapifault-deepinfra-403-model-access-denied",
        "call.in-progress.error-vapifault-deepinfra-429-exceeded-quota",
        "call.in-progress.error-providerfault-deepinfra-500-server-error",
        "call.in-progress.error-providerfault-deepinfra-503-server-overloaded-error",
        "pipeline-error-runpod-400-bad-request-validation-failed",
        "pipeline-error-runpod-401-unauthorized",
        "pipeline-error-runpod-403-model-access-denied",
        "pipeline-error-runpod-429-exceeded-quota",
        "pipeline-error-runpod-500-server-error",
        "pipeline-error-runpod-503-server-overloaded-error",
        "pipeline-error-runpod-llm-failed",
        "call.in-progress.error-vapifault-runpod-llm-failed",
        "call.in-progress.error-vapifault-runpod-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-runpod-401-unauthorized",
        "call.in-progress.error-vapifault-runpod-403-model-access-denied",
        "call.in-progress.error-vapifault-runpod-429-exceeded-quota",
        "call.in-progress.error-providerfault-runpod-500-server-error",
        "call.in-progress.error-providerfault-runpod-503-server-overloaded-error",
        "pipeline-error-custom-llm-400-bad-request-validation-failed",
        "pipeline-error-custom-llm-401-unauthorized",
        "pipeline-error-custom-llm-403-model-access-denied",
        "pipeline-error-custom-llm-429-exceeded-quota",
        "pipeline-error-custom-llm-500-server-error",
        "pipeline-error-custom-llm-503-server-overloaded-error",
        "pipeline-error-custom-llm-llm-failed",
        "call.in-progress.error-vapifault-custom-llm-llm-failed",
        "call.in-progress.error-vapifault-custom-llm-400-bad-request-validation-failed",
        "call.in-progress.error-vapifault-custom-llm-401-unauthorized",
        "call.in-progress.error-vapifault-custom-llm-403-model-access-denied",
        "call.in-progress.error-vapifault-custom-llm-429-exceeded-quota",
        "call.in-progress.error-providerfault-custom-llm-500-server-error",
        "call.in-progress.error-providerfault-custom-llm-503-server-overloaded-error",
        "pipeline-error-custom-voice-failed",
        "pipeline-error-cartesia-socket-hang-up",
        "pipeline-error-cartesia-requested-payment",
        "pipeline-error-cartesia-500-server-error",
        "pipeline-error-cartesia-503-server-error",
        "pipeline-error-cartesia-522-server-error",
        "call.in-progress.error-vapifault-cartesia-socket-hang-up",
        "call.in-progress.error-vapifault-cartesia-requested-payment",
        "call.in-progress.error-providerfault-cartesia-500-server-error",
        "call.in-progress.error-providerfault-cartesia-503-server-error",
        "call.in-progress.error-providerfault-cartesia-522-server-error",
        "pipeline-error-eleven-labs-voice-not-found",
        "pipeline-error-eleven-labs-quota-exceeded",
        "pipeline-error-eleven-labs-unauthorized-access",
        "pipeline-error-eleven-labs-unauthorized-to-access-model",
        "pipeline-error-eleven-labs-professional-voices-only-for-creator-plus",
        "pipeline-error-eleven-labs-blocked-free-plan-and-requested-upgrade",
        "pipeline-error-eleven-labs-blocked-concurrent-requests-and-requested-upgrade",
        "pipeline-error-eleven-labs-blocked-using-instant-voice-clone-and-requested-upgrade",
        "pipeline-error-eleven-labs-system-busy-and-requested-upgrade",
        "pipeline-error-eleven-labs-voice-not-fine-tuned",
        "pipeline-error-eleven-labs-invalid-api-key",
        "pipeline-error-eleven-labs-invalid-voice-samples",
        "pipeline-error-eleven-labs-voice-disabled-by-owner",
        "pipeline-error-eleven-labs-blocked-account-in-probation",
        "pipeline-error-eleven-labs-blocked-content-against-their-policy",
        "pipeline-error-eleven-labs-missing-samples-for-voice-clone",
        "pipeline-error-eleven-labs-voice-not-fine-tuned-and-cannot-be-used",
        "pipeline-error-eleven-labs-voice-not-allowed-for-free-users",
        "pipeline-error-eleven-labs-max-character-limit-exceeded",
        "pipeline-error-eleven-labs-blocked-voice-potentially-against-terms-of-service-and-awaiting-verification",
        "pipeline-error-eleven-labs-500-server-error",
        "call.in-progress.error-vapifault-eleven-labs-voice-not-found",
        "call.in-progress.error-vapifault-eleven-labs-quota-exceeded",
        "call.in-progress.error-vapifault-eleven-labs-unauthorized-access",
        "call.in-progress.error-vapifault-eleven-labs-unauthorized-to-access-model",
        "call.in-progress.error-vapifault-eleven-labs-professional-voices-only-for-creator-plus",
        "call.in-progress.error-vapifault-eleven-labs-blocked-free-plan-and-requested-upgrade",
        "call.in-progress.error-vapifault-eleven-labs-blocked-concurrent-requests-and-requested-upgrade",
        "call.in-progress.error-vapifault-eleven-labs-blocked-using-instant-voice-clone-and-requested-upgrade",
        "call.in-progress.error-vapifault-eleven-labs-system-busy-and-requested-upgrade",
        "call.in-progress.error-vapifault-eleven-labs-voice-not-fine-tuned",
        "call.in-progress.error-vapifault-eleven-labs-invalid-api-key",
        "call.in-progress.error-vapifault-eleven-labs-invalid-voice-samples",
        "call.in-progress.error-vapifault-eleven-labs-voice-disabled-by-owner",
        "call.in-progress.error-vapifault-eleven-labs-blocked-account-in-probation",
        "call.in-progress.error-vapifault-eleven-labs-blocked-content-against-their-policy",
        "call.in-progress.error-vapifault-eleven-labs-missing-samples-for-voice-clone",
        "call.in-progress.error-vapifault-eleven-labs-voice-not-fine-tuned-and-cannot-be-used",
        "call.in-progress.error-vapifault-eleven-labs-voice-not-allowed-for-free-users",
        "call.in-progress.error-vapifault-eleven-labs-max-character-limit-exceeded",
        "call.in-progress.error-vapifault-eleven-labs-blocked-voice-potentially-against-terms-of-service-and-awaiting-verification",
        "call.in-progress.error-providerfault-eleven-labs-500-server-error",
        "pipeline-error-playht-request-timed-out",
        "pipeline-error-playht-invalid-voice",
        "pipeline-error-playht-unexpected-error",
        "pipeline-error-playht-out-of-credits",
        "pipeline-error-playht-invalid-emotion",
        "pipeline-error-playht-voice-must-be-a-valid-voice-manifest-uri",
        "pipeline-error-playht-401-unauthorized",
        "pipeline-error-playht-403-forbidden-out-of-characters",
        "pipeline-error-playht-403-forbidden-api-access-not-available",
        "pipeline-error-playht-429-exceeded-quota",
        "pipeline-error-playht-502-gateway-error",
        "pipeline-error-playht-504-gateway-error",
        "call.in-progress.error-vapifault-playht-request-timed-out",
        "call.in-progress.error-vapifault-playht-invalid-voice",
        "call.in-progress.error-vapifault-playht-unexpected-error",
        "call.in-progress.error-vapifault-playht-out-of-credits",
        "call.in-progress.error-vapifault-playht-invalid-emotion",
        "call.in-progress.error-vapifault-playht-voice-must-be-a-valid-voice-manifest-uri",
        "call.in-progress.error-vapifault-playht-401-unauthorized",
        "call.in-progress.error-vapifault-playht-403-forbidden-out-of-characters",
        "call.in-progress.error-vapifault-playht-403-forbidden-api-access-not-available",
        "call.in-progress.error-vapifault-playht-429-exceeded-quota",
        "call.in-progress.error-providerfault-playht-502-gateway-error",
        "call.in-progress.error-providerfault-playht-504-gateway-error",
        "pipeline-error-custom-transcriber-failed",
        "call.in-progress.error-vapifault-custom-transcriber-failed",
        "pipeline-error-11labs-transcriber-failed",
        "call.in-progress.error-vapifault-11labs-transcriber-failed",
        "pipeline-error-deepgram-returning-400-no-such-model-language-tier-combination",
        "pipeline-error-deepgram-returning-401-invalid-credentials",
        "pipeline-error-deepgram-returning-403-model-access-denied",
        "pipeline-error-deepgram-returning-404-not-found",
        "pipeline-error-deepgram-returning-500-invalid-json",
        "pipeline-error-deepgram-returning-502-network-error",
        "pipeline-error-deepgram-returning-502-bad-gateway-ehostunreach",
        "call.in-progress.error-vapifault-deepgram-returning-400-no-such-model-language-tier-combination",
        "call.in-progress.error-vapifault-deepgram-returning-401-invalid-credentials",
        "call.in-progress.error-vapifault-deepgram-returning-404-not-found",
        "call.in-progress.error-vapifault-deepgram-returning-403-model-access-denied",
        "call.in-progress.error-providerfault-deepgram-returning-500-invalid-json",
        "call.in-progress.error-providerfault-deepgram-returning-502-network-error",
        "call.in-progress.error-providerfault-deepgram-returning-502-bad-gateway-ehostunreach",
        "pipeline-error-google-transcriber-failed",
        "call.in-progress.error-vapifault-google-transcriber-failed",
        "pipeline-error-openai-transcriber-failed",
        "call.in-progress.error-vapifault-openai-transcriber-failed",
        "assistant-ended-call",
        "assistant-said-end-call-phrase",
        "assistant-ended-call-with-hangup-task",
        "assistant-ended-call-after-message-spoken",
        "assistant-forwarded-call",
        "assistant-join-timed-out",
        "call.in-progress.error-assistant-did-not-receive-customer-audio",
        "customer-busy",
        "customer-ended-call",
        "customer-did-not-answer",
        "customer-did-not-give-microphone-permission",
        "exceeded-max-duration",
        "manually-canceled",
        "phone-call-provider-closed-websocket",
        "silence-timed-out",
        "call.in-progress.error-sip-telephony-provider-failed-to-connect-call",
        "twilio-failed-to-connect-call",
        "twilio-reported-customer-misdialed",
        "vonage-rejected",
        "voicemail",
    ],
    typing.Any,
]
