## 1.9.0 - 2025-11-19
* feat: add conversation type support for Twilio SMS chat transport
* This update adds conversation type support to TwilioSmsChatTransport and introduces a dial timeout option for TransferPlan. These enhancements provide better control over chat conversation types and transfer call behavior.
* Key changes:
* Add TwilioSmsChatTransportConversationType enum with "chat" literal type
* Add conversation_type field to TwilioSmsChatTransport to specify call type
* Add dial_timeout field to TransferPlan for SIP DIAL operation timeout control
* Update User-Agent header to use version placeholder instead of hardcoded value
* Export new conversation type in module __all__ lists
* 🌿 Generated with Fern

