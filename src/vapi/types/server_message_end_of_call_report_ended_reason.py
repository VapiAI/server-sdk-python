# This file was auto-generated by Fern from our API Definition.

import typing

ServerMessageEndOfCallReportEndedReason = typing.Union[
    typing.Literal[
        "pipeline-error-openai-voice-failed",
        "pipeline-error-cartesia-voice-failed",
        "pipeline-error-deepgram-voice-failed",
        "pipeline-error-eleven-labs-voice-failed",
        "pipeline-error-playht-voice-failed",
        "pipeline-error-lmnt-voice-failed",
        "pipeline-error-azure-voice-failed",
        "pipeline-error-rime-ai-voice-failed",
        "pipeline-error-neets-voice-failed",
        "db-error",
        "assistant-not-found",
        "license-check-failed",
        "pipeline-error-vapi-llm-failed",
        "pipeline-error-vapi-400-bad-request-validation-failed",
        "pipeline-error-vapi-401-unauthorized",
        "pipeline-error-vapi-403-model-access-denied",
        "pipeline-error-vapi-429-exceeded-quota",
        "pipeline-error-vapi-500-server-error",
        "pipeline-no-available-model",
        "worker-shutdown",
        "unknown-error",
        "vonage-disconnected",
        "vonage-failed-to-connect-call",
        "phone-call-provider-bypass-enabled-but-no-call-received",
        "vapifault-phone-call-worker-setup-socket-error",
        "vapifault-phone-call-worker-worker-setup-socket-timeout",
        "vapifault-phone-call-worker-could-not-find-call",
        "vapifault-transport-never-connected",
        "vapifault-web-call-worker-setup-failed",
        "vapifault-transport-connected-but-call-not-active",
        "vapifault-call-started-but-connection-to-transport-missing",
        "pipeline-error-deepgram-transcriber-failed",
        "pipeline-error-gladia-transcriber-failed",
        "pipeline-error-assembly-ai-transcriber-failed",
        "pipeline-error-openai-llm-failed",
        "pipeline-error-azure-openai-llm-failed",
        "pipeline-error-groq-llm-failed",
        "pipeline-error-google-llm-failed",
        "pipeline-error-xai-llm-failed",
        "pipeline-error-inflection-ai-llm-failed",
        "assistant-not-invalid",
        "assistant-not-provided",
        "call-start-error-neither-assistant-nor-server-set",
        "assistant-request-failed",
        "assistant-request-returned-error",
        "assistant-request-returned-unspeakable-error",
        "assistant-request-returned-invalid-assistant",
        "assistant-request-returned-no-assistant",
        "assistant-request-returned-forwarding-phone-number",
        "assistant-ended-call",
        "assistant-said-end-call-phrase",
        "assistant-forwarded-call",
        "assistant-join-timed-out",
        "customer-busy",
        "customer-ended-call",
        "customer-did-not-answer",
        "customer-did-not-give-microphone-permission",
        "assistant-said-message-with-end-call-enabled",
        "exceeded-max-duration",
        "manually-canceled",
        "phone-call-provider-closed-websocket",
        "pipeline-error-openai-400-bad-request-validation-failed",
        "pipeline-error-openai-401-unauthorized",
        "pipeline-error-openai-403-model-access-denied",
        "pipeline-error-openai-429-exceeded-quota",
        "pipeline-error-openai-500-server-error",
        "pipeline-error-google-400-bad-request-validation-failed",
        "pipeline-error-google-401-unauthorized",
        "pipeline-error-google-403-model-access-denied",
        "pipeline-error-google-429-exceeded-quota",
        "pipeline-error-google-500-server-error",
        "pipeline-error-xai-400-bad-request-validation-failed",
        "pipeline-error-xai-401-unauthorized",
        "pipeline-error-xai-403-model-access-denied",
        "pipeline-error-xai-429-exceeded-quota",
        "pipeline-error-xai-500-server-error",
        "pipeline-error-inflection-ai-400-bad-request-validation-failed",
        "pipeline-error-inflection-ai-401-unauthorized",
        "pipeline-error-inflection-ai-403-model-access-denied",
        "pipeline-error-inflection-ai-429-exceeded-quota",
        "pipeline-error-inflection-ai-500-server-error",
        "pipeline-error-azure-openai-400-bad-request-validation-failed",
        "pipeline-error-azure-openai-401-unauthorized",
        "pipeline-error-azure-openai-403-model-access-denied",
        "pipeline-error-azure-openai-429-exceeded-quota",
        "pipeline-error-azure-openai-500-server-error",
        "pipeline-error-groq-400-bad-request-validation-failed",
        "pipeline-error-groq-401-unauthorized",
        "pipeline-error-groq-403-model-access-denied",
        "pipeline-error-groq-429-exceeded-quota",
        "pipeline-error-groq-500-server-error",
        "pipeline-error-anthropic-400-bad-request-validation-failed",
        "pipeline-error-anthropic-401-unauthorized",
        "pipeline-error-anthropic-403-model-access-denied",
        "pipeline-error-anthropic-429-exceeded-quota",
        "pipeline-error-anthropic-500-server-error",
        "pipeline-error-anthropic-llm-failed",
        "pipeline-error-together-ai-400-bad-request-validation-failed",
        "pipeline-error-together-ai-401-unauthorized",
        "pipeline-error-together-ai-403-model-access-denied",
        "pipeline-error-together-ai-429-exceeded-quota",
        "pipeline-error-together-ai-500-server-error",
        "pipeline-error-together-ai-llm-failed",
        "pipeline-error-anyscale-400-bad-request-validation-failed",
        "pipeline-error-anyscale-401-unauthorized",
        "pipeline-error-anyscale-403-model-access-denied",
        "pipeline-error-anyscale-429-exceeded-quota",
        "pipeline-error-anyscale-500-server-error",
        "pipeline-error-anyscale-llm-failed",
        "pipeline-error-openrouter-400-bad-request-validation-failed",
        "pipeline-error-openrouter-401-unauthorized",
        "pipeline-error-openrouter-403-model-access-denied",
        "pipeline-error-openrouter-429-exceeded-quota",
        "pipeline-error-openrouter-500-server-error",
        "pipeline-error-openrouter-llm-failed",
        "pipeline-error-perplexity-ai-400-bad-request-validation-failed",
        "pipeline-error-perplexity-ai-401-unauthorized",
        "pipeline-error-perplexity-ai-403-model-access-denied",
        "pipeline-error-perplexity-ai-429-exceeded-quota",
        "pipeline-error-perplexity-ai-500-server-error",
        "pipeline-error-perplexity-ai-llm-failed",
        "pipeline-error-deepinfra-400-bad-request-validation-failed",
        "pipeline-error-deepinfra-401-unauthorized",
        "pipeline-error-deepinfra-403-model-access-denied",
        "pipeline-error-deepinfra-429-exceeded-quota",
        "pipeline-error-deepinfra-500-server-error",
        "pipeline-error-deepinfra-llm-failed",
        "pipeline-error-runpod-400-bad-request-validation-failed",
        "pipeline-error-runpod-401-unauthorized",
        "pipeline-error-runpod-403-model-access-denied",
        "pipeline-error-runpod-429-exceeded-quota",
        "pipeline-error-runpod-500-server-error",
        "pipeline-error-runpod-llm-failed",
        "pipeline-error-custom-llm-400-bad-request-validation-failed",
        "pipeline-error-custom-llm-401-unauthorized",
        "pipeline-error-custom-llm-403-model-access-denied",
        "pipeline-error-custom-llm-429-exceeded-quota",
        "pipeline-error-custom-llm-500-server-error",
        "pipeline-error-custom-llm-llm-failed",
        "pipeline-error-custom-voice-failed",
        "pipeline-error-cartesia-socket-hang-up",
        "pipeline-error-cartesia-requested-payment",
        "pipeline-error-cartesia-500-server-error",
        "pipeline-error-cartesia-503-server-error",
        "pipeline-error-cartesia-522-server-error",
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
        "pipeline-error-eleven-labs-500-server-error",
        "pipeline-error-eleven-labs-max-character-limit-exceeded",
        "pipeline-error-eleven-labs-blocked-voice-potentially-against-terms-of-service-and-awaiting-verification",
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
        "pipeline-error-deepgram-returning-403-model-access-denied",
        "pipeline-error-deepgram-returning-401-invalid-credentials",
        "pipeline-error-deepgram-returning-404-not-found",
        "pipeline-error-deepgram-returning-400-no-such-model-language-tier-combination",
        "pipeline-error-deepgram-returning-500-invalid-json",
        "pipeline-error-deepgram-returning-502-network-error",
        "pipeline-error-deepgram-returning-502-bad-gateway-ehostunreach",
        "pipeline-error-tavus-video-failed",
        "pipeline-error-custom-transcriber-failed",
        "silence-timed-out",
        "sip-gateway-failed-to-connect-call",
        "twilio-failed-to-connect-call",
        "twilio-reported-customer-misdialed",
        "vonage-rejected",
        "voicemail",
    ],
    typing.Any,
]
