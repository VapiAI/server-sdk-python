# Reference
## Calls
<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.calls.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — This is the unique identifier for the call.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This will return calls with the specified assistantId.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` 

This is the phone number that will be used for the call. To use a transient number, use `phoneNumber` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.calls.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customers:** `typing.Optional[typing.Sequence[CreateCustomerDto]]` 

This is used to issue batch calls to multiple customers.

Only relevant for `outboundPhoneCall`. To call a single customer, use `customer` instead.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the call. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**schedule_plan:** `typing.Optional[SchedulePlan]` — This is the schedule plan of the call.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — This is the transport of the call.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` 

This is the assistant ID that will be used for the call. To use a transient assistant, use `assistant` instead.

To start a call with:
- Assistant, use `assistantId` or `assistant`
- Squad, use `squadId` or `squad`
- Workflow, use `workflowId` or `workflow`
    
</dd>
</dl>

<dl>
<dd>

**assistant:** `typing.Optional[CreateAssistantDto]` 

This is the assistant that will be used for the call. To use an existing assistant, use `assistantId` instead.

To start a call with:
- Assistant, use `assistant`
- Squad, use `squad`
- Workflow, use `workflow`
    
</dd>
</dl>

<dl>
<dd>

**assistant_overrides:** `typing.Optional[AssistantOverrides]` — These are the overrides for the `assistant` or `assistantId`'s settings and template variables.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` 

This is the squad that will be used for the call. To use a transient squad, use `squad` instead.

To start a call with:
- Assistant, use `assistant` or `assistantId`
- Squad, use `squad` or `squadId`
- Workflow, use `workflow` or `workflowId`
    
</dd>
</dl>

<dl>
<dd>

**squad:** `typing.Optional[CreateSquadDto]` 

This is a squad that will be used for the call. To use an existing squad, use `squadId` instead.

To start a call with:
- Assistant, use `assistant` or `assistantId`
- Squad, use `squad` or `squadId`
- Workflow, use `workflow` or `workflowId`
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` 

[BETA] This feature is in active development. The API and behavior are subject to change as we refine it based on user feedback.

This is the workflow that will be used for the call. To use a transient workflow, use `workflow` instead.

To start a call with:
- Assistant, use `assistant` or `assistantId`
- Squad, use `squad` or `squadId`
- Workflow, use `workflow` or `workflowId`
    
</dd>
</dl>

<dl>
<dd>

**workflow:** `typing.Optional[CreateWorkflowDto]` 

[BETA] This feature is in active development. The API and behavior are subject to change as we refine it based on user feedback.

This is a workflow that will be used for the call. To use an existing workflow, use `workflowId` instead.

To start a call with:
- Assistant, use `assistant` or `assistantId`
- Squad, use `squad` or `squadId`
- Workflow, use `workflow` or `workflowId`
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` 

This is the phone number that will be used for the call. To use a transient number, use `phoneNumber` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[ImportTwilioPhoneNumberDto]` 

This is the phone number that will be used for the call. To use an existing number, use `phoneNumberId` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

This is the customer that will be called. To call a transient customer , use `customer` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[CreateCustomerDto]` 

This is the customer that will be called. To call an existing customer, use `customerId` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.calls.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.calls.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.calls.update(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the call. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assistants
<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.assistants.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.assistants.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcriber:** `typing.Optional[CreateAssistantDtoTranscriber]` — These are the options for the assistant's transcriber.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[CreateAssistantDtoModel]` — These are the options for the assistant's LLM.
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[CreateAssistantDtoVoice]` — These are the options for the assistant's voice.
    
</dd>
</dl>

<dl>
<dd>

**first_message:** `typing.Optional[str]` 

This is the first message that the assistant will say. This can also be a URL to a containerized audio file (mp3, wav, etc.).

If unspecified, assistant will wait for user to speak and use the model to respond once they speak.
    
</dd>
</dl>

<dl>
<dd>

**first_message_interruptions_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**first_message_mode:** `typing.Optional[CreateAssistantDtoFirstMessageMode]` 

This is the mode for the first message. Default is 'assistant-speaks-first'.

Use:
- 'assistant-speaks-first' to have the assistant speak first.
- 'assistant-waits-for-user' to have the assistant wait for the user to speak first.
- 'assistant-speaks-first-with-model-generated-message' to have the assistant speak first with a message generated by the model based on the conversation state. (`assistant.model.messages` at call start, `call.messages` at squad transfer points).

@default 'assistant-speaks-first'
    
</dd>
</dl>

<dl>
<dd>

**voicemail_detection:** `typing.Optional[CreateAssistantDtoVoicemailDetection]` 

These are the settings to configure or disable voicemail detection. Alternatively, voicemail detection can be configured using the model.tools=[VoicemailTool].
This uses Twilio's built-in detection while the VoicemailTool relies on the model to detect if a voicemail was reached.
You can use neither of them, one of them, or both of them. By default, Twilio built-in detection is enabled while VoicemailTool is not.
    
</dd>
</dl>

<dl>
<dd>

**client_messages:** `typing.Optional[typing.Sequence[CreateAssistantDtoClientMessagesItem]]` — These are the messages that will be sent to your Client SDKs. Default is conversation-update,function-call,hang,model-output,speech-update,status-update,transfer-update,transcript,tool-calls,user-interrupted,voice-input,workflow.node.started. You can check the shape of the messages in ClientMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**server_messages:** `typing.Optional[typing.Sequence[CreateAssistantDtoServerMessagesItem]]` — These are the messages that will be sent to your Server URL. Default is conversation-update,end-of-call-report,function-call,hang,speech-update,status-update,tool-calls,transfer-destination-request,user-interrupted. You can check the shape of the messages in ServerMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**silence_timeout_seconds:** `typing.Optional[float]` 

How many seconds of silence to wait before ending the call. Defaults to 30.

@default 30
    
</dd>
</dl>

<dl>
<dd>

**max_duration_seconds:** `typing.Optional[float]` 

This is the maximum number of seconds that the call will last. When the call reaches this duration, it will be ended.

@default 600 (10 minutes)
    
</dd>
</dl>

<dl>
<dd>

**background_sound:** `typing.Optional[CreateAssistantDtoBackgroundSound]` 

This is the background sound in the call. Default for phone calls is 'office' and default for web calls is 'off'.
You can also provide a custom sound by providing a URL to an audio file.
    
</dd>
</dl>

<dl>
<dd>

**background_denoising_enabled:** `typing.Optional[bool]` 

This enables filtering of noise and background speech while the user is talking.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**model_output_in_messages_enabled:** `typing.Optional[bool]` 

This determines whether the model's output is used in conversation history rather than the transcription of assistant's speech.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**transport_configurations:** `typing.Optional[typing.Sequence[TransportConfigurationTwilio]]` — These are the configurations to be passed to the transport providers of assistant's calls, like Twilio. You can store multiple configurations for different transport providers. For a call, only the configuration matching the call transport provider is used.
    
</dd>
</dl>

<dl>
<dd>

**observability_plan:** `typing.Optional[LangfuseObservabilityPlan]` 

This is the plan for observability configuration of assistant's calls.
Currently supports Langfuse for tracing and monitoring.
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `typing.Optional[typing.Sequence[CreateAssistantDtoCredentialsItem]]` — These are dynamic credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can supplement an additional credentials using this. Dynamic credentials override existing credentials.
    
</dd>
</dl>

<dl>
<dd>

**hooks:** `typing.Optional[typing.Sequence[CreateAssistantDtoHooksItem]]` — This is a set of actions that will be performed on certain events.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

This is the name of the assistant.

This is required when you want to transfer between assistants in a call.
    
</dd>
</dl>

<dl>
<dd>

**voicemail_message:** `typing.Optional[str]` 

This is the message that the assistant will say if the call is forwarded to voicemail.

If unspecified, it will hang up.
    
</dd>
</dl>

<dl>
<dd>

**end_call_message:** `typing.Optional[str]` 

This is the message that the assistant will say if it ends the call.

If unspecified, it will hang up without saying anything.
    
</dd>
</dl>

<dl>
<dd>

**end_call_phrases:** `typing.Optional[typing.Sequence[str]]` — This list contains phrases that, if spoken by the assistant, will trigger the call to be hung up. Case insensitive.
    
</dd>
</dl>

<dl>
<dd>

**compliance_plan:** `typing.Optional[CompliancePlan]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — This is for metadata you want to store on the assistant.
    
</dd>
</dl>

<dl>
<dd>

**analysis_plan:** `typing.Optional[AnalysisPlan]` — This is the plan for analysis of assistant's calls. Stored in `call.analysis`.
    
</dd>
</dl>

<dl>
<dd>

**artifact_plan:** `typing.Optional[ArtifactPlan]` 

This is the plan for artifacts generated during assistant's calls. Stored in `call.artifact`.

Note: `recordingEnabled` is currently at the root level. It will be moved to `artifactPlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**message_plan:** `typing.Optional[MessagePlan]` 

This is the plan for static predefined messages that can be spoken by the assistant during the call, like `idleMessages`.

Note: `firstMessage`, `voicemailMessage`, and `endCallMessage` are currently at the root level. They will be moved to `messagePlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**start_speaking_plan:** `typing.Optional[StartSpeakingPlan]` 

This is the plan for when the assistant should start talking.

You should configure this if you're running into these issues:
- The assistant is too slow to start talking after the customer is done speaking.
- The assistant is too fast to start talking after the customer is done speaking.
- The assistant is so fast that it's actually interrupting the customer.
    
</dd>
</dl>

<dl>
<dd>

**stop_speaking_plan:** `typing.Optional[StopSpeakingPlan]` 

This is the plan for when assistant should stop talking on customer interruption.

You should configure this if you're running into these issues:
- The assistant is too slow to recognize customer's interruption.
- The assistant is too fast to recognize customer's interruption.
- The assistant is getting interrupted by phrases that are just acknowledgments.
- The assistant is getting interrupted by background noises.
- The assistant is not properly stopping -- it starts talking right after getting interrupted.
    
</dd>
</dl>

<dl>
<dd>

**monitor_plan:** `typing.Optional[MonitorPlan]` 

This is the plan for real-time monitoring of the assistant's calls.

Usage:
- To enable live listening of the assistant's calls, set `monitorPlan.listenEnabled` to `true`.
- To enable live control of the assistant's calls, set `monitorPlan.controlEnabled` to `true`.

Note, `serverMessages`, `clientMessages`, `serverUrl` and `serverUrlSecret` are currently at the root level but will be moved to `monitorPlan` in the future. Will remain backwards compatible
    
</dd>
</dl>

<dl>
<dd>

**credential_ids:** `typing.Optional[typing.Sequence[str]]` — These are the credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can provide a subset using this.
    
</dd>
</dl>

<dl>
<dd>

**server:** `typing.Optional[Server]` 

This is where Vapi will send webhooks. You can find all webhooks available along with their shape in ServerMessage schema.

The order of precedence is:

1. assistant.server.url
2. phoneNumber.serverUrl
3. org.serverUrl
    
</dd>
</dl>

<dl>
<dd>

**keypad_input_plan:** `typing.Optional[KeypadInputPlan]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.assistants.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.assistants.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.assistants.update(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transcriber:** `typing.Optional[UpdateAssistantDtoTranscriber]` — These are the options for the assistant's transcriber.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[UpdateAssistantDtoModel]` — These are the options for the assistant's LLM.
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[UpdateAssistantDtoVoice]` — These are the options for the assistant's voice.
    
</dd>
</dl>

<dl>
<dd>

**first_message:** `typing.Optional[str]` 

This is the first message that the assistant will say. This can also be a URL to a containerized audio file (mp3, wav, etc.).

If unspecified, assistant will wait for user to speak and use the model to respond once they speak.
    
</dd>
</dl>

<dl>
<dd>

**first_message_interruptions_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**first_message_mode:** `typing.Optional[UpdateAssistantDtoFirstMessageMode]` 

This is the mode for the first message. Default is 'assistant-speaks-first'.

Use:
- 'assistant-speaks-first' to have the assistant speak first.
- 'assistant-waits-for-user' to have the assistant wait for the user to speak first.
- 'assistant-speaks-first-with-model-generated-message' to have the assistant speak first with a message generated by the model based on the conversation state. (`assistant.model.messages` at call start, `call.messages` at squad transfer points).

@default 'assistant-speaks-first'
    
</dd>
</dl>

<dl>
<dd>

**voicemail_detection:** `typing.Optional[UpdateAssistantDtoVoicemailDetection]` 

These are the settings to configure or disable voicemail detection. Alternatively, voicemail detection can be configured using the model.tools=[VoicemailTool].
This uses Twilio's built-in detection while the VoicemailTool relies on the model to detect if a voicemail was reached.
You can use neither of them, one of them, or both of them. By default, Twilio built-in detection is enabled while VoicemailTool is not.
    
</dd>
</dl>

<dl>
<dd>

**client_messages:** `typing.Optional[typing.Sequence[UpdateAssistantDtoClientMessagesItem]]` — These are the messages that will be sent to your Client SDKs. Default is conversation-update,function-call,hang,model-output,speech-update,status-update,transfer-update,transcript,tool-calls,user-interrupted,voice-input,workflow.node.started. You can check the shape of the messages in ClientMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**server_messages:** `typing.Optional[typing.Sequence[UpdateAssistantDtoServerMessagesItem]]` — These are the messages that will be sent to your Server URL. Default is conversation-update,end-of-call-report,function-call,hang,speech-update,status-update,tool-calls,transfer-destination-request,user-interrupted. You can check the shape of the messages in ServerMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**silence_timeout_seconds:** `typing.Optional[float]` 

How many seconds of silence to wait before ending the call. Defaults to 30.

@default 30
    
</dd>
</dl>

<dl>
<dd>

**max_duration_seconds:** `typing.Optional[float]` 

This is the maximum number of seconds that the call will last. When the call reaches this duration, it will be ended.

@default 600 (10 minutes)
    
</dd>
</dl>

<dl>
<dd>

**background_sound:** `typing.Optional[UpdateAssistantDtoBackgroundSound]` 

This is the background sound in the call. Default for phone calls is 'office' and default for web calls is 'off'.
You can also provide a custom sound by providing a URL to an audio file.
    
</dd>
</dl>

<dl>
<dd>

**background_denoising_enabled:** `typing.Optional[bool]` 

This enables filtering of noise and background speech while the user is talking.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**model_output_in_messages_enabled:** `typing.Optional[bool]` 

This determines whether the model's output is used in conversation history rather than the transcription of assistant's speech.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**transport_configurations:** `typing.Optional[typing.Sequence[TransportConfigurationTwilio]]` — These are the configurations to be passed to the transport providers of assistant's calls, like Twilio. You can store multiple configurations for different transport providers. For a call, only the configuration matching the call transport provider is used.
    
</dd>
</dl>

<dl>
<dd>

**observability_plan:** `typing.Optional[LangfuseObservabilityPlan]` 

This is the plan for observability configuration of assistant's calls.
Currently supports Langfuse for tracing and monitoring.
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `typing.Optional[typing.Sequence[UpdateAssistantDtoCredentialsItem]]` — These are dynamic credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can supplement an additional credentials using this. Dynamic credentials override existing credentials.
    
</dd>
</dl>

<dl>
<dd>

**hooks:** `typing.Optional[typing.Sequence[UpdateAssistantDtoHooksItem]]` — This is a set of actions that will be performed on certain events.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

This is the name of the assistant.

This is required when you want to transfer between assistants in a call.
    
</dd>
</dl>

<dl>
<dd>

**voicemail_message:** `typing.Optional[str]` 

This is the message that the assistant will say if the call is forwarded to voicemail.

If unspecified, it will hang up.
    
</dd>
</dl>

<dl>
<dd>

**end_call_message:** `typing.Optional[str]` 

This is the message that the assistant will say if it ends the call.

If unspecified, it will hang up without saying anything.
    
</dd>
</dl>

<dl>
<dd>

**end_call_phrases:** `typing.Optional[typing.Sequence[str]]` — This list contains phrases that, if spoken by the assistant, will trigger the call to be hung up. Case insensitive.
    
</dd>
</dl>

<dl>
<dd>

**compliance_plan:** `typing.Optional[CompliancePlan]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — This is for metadata you want to store on the assistant.
    
</dd>
</dl>

<dl>
<dd>

**analysis_plan:** `typing.Optional[AnalysisPlan]` — This is the plan for analysis of assistant's calls. Stored in `call.analysis`.
    
</dd>
</dl>

<dl>
<dd>

**artifact_plan:** `typing.Optional[ArtifactPlan]` 

This is the plan for artifacts generated during assistant's calls. Stored in `call.artifact`.

Note: `recordingEnabled` is currently at the root level. It will be moved to `artifactPlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**message_plan:** `typing.Optional[MessagePlan]` 

This is the plan for static predefined messages that can be spoken by the assistant during the call, like `idleMessages`.

Note: `firstMessage`, `voicemailMessage`, and `endCallMessage` are currently at the root level. They will be moved to `messagePlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**start_speaking_plan:** `typing.Optional[StartSpeakingPlan]` 

This is the plan for when the assistant should start talking.

You should configure this if you're running into these issues:
- The assistant is too slow to start talking after the customer is done speaking.
- The assistant is too fast to start talking after the customer is done speaking.
- The assistant is so fast that it's actually interrupting the customer.
    
</dd>
</dl>

<dl>
<dd>

**stop_speaking_plan:** `typing.Optional[StopSpeakingPlan]` 

This is the plan for when assistant should stop talking on customer interruption.

You should configure this if you're running into these issues:
- The assistant is too slow to recognize customer's interruption.
- The assistant is too fast to recognize customer's interruption.
- The assistant is getting interrupted by phrases that are just acknowledgments.
- The assistant is getting interrupted by background noises.
- The assistant is not properly stopping -- it starts talking right after getting interrupted.
    
</dd>
</dl>

<dl>
<dd>

**monitor_plan:** `typing.Optional[MonitorPlan]` 

This is the plan for real-time monitoring of the assistant's calls.

Usage:
- To enable live listening of the assistant's calls, set `monitorPlan.listenEnabled` to `true`.
- To enable live control of the assistant's calls, set `monitorPlan.controlEnabled` to `true`.

Note, `serverMessages`, `clientMessages`, `serverUrl` and `serverUrlSecret` are currently at the root level but will be moved to `monitorPlan` in the future. Will remain backwards compatible
    
</dd>
</dl>

<dl>
<dd>

**credential_ids:** `typing.Optional[typing.Sequence[str]]` — These are the credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can provide a subset using this.
    
</dd>
</dl>

<dl>
<dd>

**server:** `typing.Optional[Server]` 

This is where Vapi will send webhooks. You can find all webhooks available along with their shape in ServerMessage schema.

The order of precedence is:

1. assistant.server.url
2. phoneNumber.serverUrl
3. org.serverUrl
    
</dd>
</dl>

<dl>
<dd>

**keypad_input_plan:** `typing.Optional[KeypadInputPlan]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PhoneNumbers
<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.phone_numbers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import CreateByoPhoneNumberDto
client = Vapi(token="YOUR_TOKEN", )
client.phone_numbers.create(request=CreateByoPhoneNumberDto(credential_id='credentialId', ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PhoneNumbersCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.phone_numbers.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.phone_numbers.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import UpdateByoPhoneNumberDto
client = Vapi(token="YOUR_TOKEN", )
client.phone_numbers.update(id='id', request=UpdateByoPhoneNumberDto(), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `PhoneNumbersUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tools
<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.tools.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import CreateDtmfToolDto
client = Vapi(token="YOUR_TOKEN", )
client.tools.create(request=CreateDtmfToolDto(), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ToolsCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.tools.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.tools.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import UpdateDtmfToolDto
client = Vapi(token="YOUR_TOKEN", )
client.tools.update(id='id', request=UpdateDtmfToolDto(), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ToolsUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/vapi/files/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.files.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.files.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations
core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.files.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.files.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.files.update(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the file. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## KnowledgeBases
<details><summary><code>client.knowledge_bases.<a href="src/vapi/knowledge_bases/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.knowledge_bases.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.<a href="src/vapi/knowledge_bases/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import CreateTrieveKnowledgeBaseDto
client = Vapi(token="YOUR_TOKEN", )
client.knowledge_bases.create(request=CreateTrieveKnowledgeBaseDto(), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `KnowledgeBasesCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.<a href="src/vapi/knowledge_bases/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.knowledge_bases.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.<a href="src/vapi/knowledge_bases/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.knowledge_bases.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge_bases.<a href="src/vapi/knowledge_bases/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import UpdateTrieveKnowledgeBaseDto
client = Vapi(token="YOUR_TOKEN", )
client.knowledge_bases.update(id='id', request=UpdateTrieveKnowledgeBaseDto(), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `KnowledgeBasesUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Workflow
<details><summary><code>client.workflow.<a href="src/vapi/workflow/client.py">workflow_controller_find_all</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.workflow.workflow_controller_find_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflow.<a href="src/vapi/workflow/client.py">workflow_controller_create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import ConversationNode
from vapi import Edge
client = Vapi(token="YOUR_TOKEN", )
client.workflow.workflow_controller_create(nodes=[ConversationNode(name='name', )], name='name', edges=[Edge(from_='from', to='to', )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nodes:** `typing.Sequence[CreateWorkflowDtoNodesItem]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**edges:** `typing.Sequence[Edge]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[CreateWorkflowDtoModel]` — These are the options for the workflow's LLM.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflow.<a href="src/vapi/workflow/client.py">workflow_controller_find_one</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.workflow.workflow_controller_find_one(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflow.<a href="src/vapi/workflow/client.py">workflow_controller_delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.workflow.workflow_controller_delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.workflow.<a href="src/vapi/workflow/client.py">workflow_controller_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.workflow.workflow_controller_update(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**nodes:** `typing.Optional[typing.Sequence[UpdateWorkflowDtoNodesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[UpdateWorkflowDtoModel]` — These are the options for the workflow's LLM.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**edges:** `typing.Optional[typing.Sequence[Edge]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Squads
<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.squads.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import SquadMemberDto
client = Vapi(token="YOUR_TOKEN", )
client.squads.create(members=[SquadMemberDto()], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**members:** `typing.Sequence[SquadMemberDto]` 

This is the list of assistants that make up the squad.

The call will start with the first assistant in the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the squad.
    
</dd>
</dl>

<dl>
<dd>

**members_overrides:** `typing.Optional[AssistantOverrides]` 

This can be used to override all the assistants' settings and provide values for their template variables.

Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.squads.get(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.squads.delete(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import SquadMemberDto
client = Vapi(token="YOUR_TOKEN", )
client.squads.update(id='id', members=[SquadMemberDto()], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.Sequence[SquadMemberDto]` 

This is the list of assistants that make up the squad.

The call will start with the first assistant in the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the squad.
    
</dd>
</dl>

<dl>
<dd>

**members_overrides:** `typing.Optional[AssistantOverrides]` 

This can be used to override all the assistants' settings and provide values for their template variables.

Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TestSuites
<details><summary><code>client.test_suites.<a href="src/vapi/test_suites/client.py">test_suite_controller_find_all_paginated</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suites.test_suite_controller_find_all_paginated()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[TestSuiteControllerFindAllPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suites.<a href="src/vapi/test_suites/client.py">test_suite_controller_create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suites.test_suite_controller_create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the test suite.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — This is the phone number ID associated with this test suite.
    
</dd>
</dl>

<dl>
<dd>

**tester_plan:** `typing.Optional[TesterPlan]` 

Override the default tester plan by providing custom assistant configuration for the test agent.

We recommend only using this if you are confident, as we have already set sensible defaults on the tester plan.
    
</dd>
</dl>

<dl>
<dd>

**target_plan:** `typing.Optional[TargetPlan]` — These are the configuration for the assistant / phone number that is being tested.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suites.<a href="src/vapi/test_suites/client.py">test_suite_controller_find_one</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suites.test_suite_controller_find_one(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suites.<a href="src/vapi/test_suites/client.py">test_suite_controller_remove</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suites.test_suite_controller_remove(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suites.<a href="src/vapi/test_suites/client.py">test_suite_controller_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suites.test_suite_controller_update(id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the test suite.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — This is the phone number ID associated with this test suite.
    
</dd>
</dl>

<dl>
<dd>

**tester_plan:** `typing.Optional[TesterPlan]` 

Override the default tester plan by providing custom assistant configuration for the test agent.

We recommend only using this if you are confident, as we have already set sensible defaults on the tester plan.
    
</dd>
</dl>

<dl>
<dd>

**target_plan:** `typing.Optional[TargetPlan]` — These are the configuration for the assistant / phone number that is being tested.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TestSuiteTests
<details><summary><code>client.test_suite_tests.<a href="src/vapi/test_suite_tests/client.py">test_suite_test_controller_find_all_paginated</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_tests.test_suite_test_controller_find_all_paginated(test_suite_id='testSuiteId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[TestSuiteTestControllerFindAllPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_tests.<a href="src/vapi/test_suite_tests/client.py">test_suite_test_controller_create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import CreateTestSuiteTestVoiceDto
from vapi import TestSuiteTestScorerAi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_tests.test_suite_test_controller_create(test_suite_id='testSuiteId', request=CreateTestSuiteTestVoiceDto(scorers=[TestSuiteTestScorerAi(rubric='rubric', )], script='script', ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TestSuiteTestControllerCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_tests.<a href="src/vapi/test_suite_tests/client.py">test_suite_test_controller_find_one</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_tests.test_suite_test_controller_find_one(test_suite_id='testSuiteId', id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_tests.<a href="src/vapi/test_suite_tests/client.py">test_suite_test_controller_remove</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_tests.test_suite_test_controller_remove(test_suite_id='testSuiteId', id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_tests.<a href="src/vapi/test_suite_tests/client.py">test_suite_test_controller_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import UpdateTestSuiteTestVoiceDto
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_tests.test_suite_test_controller_update(test_suite_id='testSuiteId', id='id', request=UpdateTestSuiteTestVoiceDto(), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `TestSuiteTestControllerUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TestSuiteRuns
<details><summary><code>client.test_suite_runs.<a href="src/vapi/test_suite_runs/client.py">test_suite_run_controller_find_all_paginated</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_runs.test_suite_run_controller_find_all_paginated(test_suite_id='testSuiteId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[TestSuiteRunControllerFindAllPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_runs.<a href="src/vapi/test_suite_runs/client.py">test_suite_run_controller_create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_runs.test_suite_run_controller_create(test_suite_id='testSuiteId', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the test suite run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_runs.<a href="src/vapi/test_suite_runs/client.py">test_suite_run_controller_find_one</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_runs.test_suite_run_controller_find_one(test_suite_id='testSuiteId', id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_runs.<a href="src/vapi/test_suite_runs/client.py">test_suite_run_controller_remove</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_runs.test_suite_run_controller_remove(test_suite_id='testSuiteId', id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.test_suite_runs.<a href="src/vapi/test_suite_runs/client.py">test_suite_run_controller_update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.test_suite_runs.test_suite_run_controller_update(test_suite_id='testSuiteId', id='id', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**test_suite_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the test suite run.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Analytics
<details><summary><code>client.analytics.<a href="src/vapi/analytics/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi import AnalyticsQuery
from vapi import AnalyticsOperation
client = Vapi(token="YOUR_TOKEN", )
client.analytics.get(queries=[AnalyticsQuery(table="call", name='name', operations=[AnalyticsOperation(operation="sum", column="id", )], )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queries:** `typing.Sequence[AnalyticsQuery]` — This is the list of metric queries you want to perform.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Logs
<details><summary><code>client.logs.<a href="src/vapi/logs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
response = client.logs.get()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[LogsGetRequestType]` — This is the type of the log.
    
</dd>
</dl>

<dl>
<dd>

**webhook_type:** `typing.Optional[str]` — This is the type of the webhook, given the log is from a webhook.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the ID of the assistant.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — This is the ID of the phone number.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — This is the ID of the customer.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the ID of the squad.
    
</dd>
</dl>

<dl>
<dd>

**call_id:** `typing.Optional[str]` — This is the ID of the call.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[LogsGetRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.logs.<a href="src/vapi/logs/client.py">logging_controller_logs_delete_query</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
client = Vapi(token="YOUR_TOKEN", )
client.logs.logging_controller_logs_delete_query()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[LoggingControllerLogsDeleteQueryRequestType]` — This is the type of the log.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — This is the ID of the phone number.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — This is the ID of the customer.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the ID of the squad.
    
</dd>
</dl>

<dl>
<dd>

**call_id:** `typing.Optional[str]` — This is the ID of the call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

