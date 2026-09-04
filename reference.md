# Reference
## Assistants
<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">list</a>(...) -> typing.List[Assistant]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns assistants for the authenticated organization. Filter results by creation or update timestamps and limit the number returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

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

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">create</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a reusable assistant configuration containing the model, voice, transcriber, tools, prompts, and call behavior.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

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

**request:** `CreateAssistantDto` 
    
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

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">assistant_controller_validate_background_sound_url</a>(...) -> BackgroundSoundUrlValidationResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.assistants.assistant_controller_validate_background_sound_url(
    url="https://example.com/my-sound.mp3",
)

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

**url:** `str` — This is the background sound URL to validate. The server performs a ranged request and checks that the URL serves a live media file.
    
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

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">get</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the assistant identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.assistants.get(
    id="id",
)

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

**id:** `str` — The unique identifier of the assistant.
    
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

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">delete</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the assistant identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.assistants.delete(
    id="id",
)

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

**id:** `str` — The unique identifier of the assistant.
    
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

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">update</a>(...) -> Assistant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified fields of the assistant identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.assistants.update(
    id="id",
)

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

**id:** `str` — The unique identifier of the assistant.
    
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

**first_message_interruptions_enabled:** `typing.Optional[bool]` — Set to `true` to allow the user to interrupt the assistant while it speaks the first message. Default is `false`.
    
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
By default, voicemail detection is disabled.
    
</dd>
</dl>

<dl>
<dd>

**client_messages:** `typing.Optional[typing.List[UpdateAssistantDtoClientMessagesItem]]` — These are the messages that will be sent to your Client SDKs. Default is conversation-update,function-call,hang,model-output,speech-update,status-update,transfer-update,transcript,tool-calls,user-interrupted,voice-input,workflow.node.started,assistant.started. You can check the shape of the messages in ClientMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**server_messages:** `typing.Optional[typing.List[UpdateAssistantDtoServerMessagesItem]]` — These are the messages that will be sent to your Server URL. Default is conversation-update,end-of-call-report,function-call,hang,speech-update,status-update,tool-calls,transfer-destination-request,handoff-destination-request,user-interrupted,assistant.started. You can check the shape of the messages in ServerMessage schema.
    
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

**model_output_in_messages_enabled:** `typing.Optional[bool]` 

This determines whether the model's output is used in conversation history rather than the transcription of assistant's speech.

@default false
    
</dd>
</dl>

<dl>
<dd>

**transport_configurations:** `typing.Optional[typing.List[TransportConfigurationTwilio]]` — These are the configurations to be passed to the transport providers of assistant's calls, like Twilio. You can store multiple configurations for different transport providers. For a call, only the configuration matching the call transport provider is used.
    
</dd>
</dl>

<dl>
<dd>

**observability_plan:** `typing.Optional[LangfuseObservabilityPlan]` 

This is the plan for observability of assistant's calls.

Currently, only Langfuse is supported.
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `typing.Optional[typing.List[UpdateAssistantDtoCredentialsItem]]` — These are dynamic credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can supplement an additional credentials using this. Dynamic credentials override existing credentials.
    
</dd>
</dl>

<dl>
<dd>

**hooks:** `typing.Optional[typing.List[UpdateAssistantDtoHooksItem]]` — This is a set of actions that will be performed on certain events.
    
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

**end_call_phrases:** `typing.Optional[typing.List[str]]` — This list contains phrases that, if spoken by the assistant, will trigger the call to be hung up. Case insensitive.
    
</dd>
</dl>

<dl>
<dd>

**compliance_plan:** `typing.Optional[CompliancePlan]` — Compliance settings for the assistant, including HIPAA and PCI behavior, security filtering, and recording consent.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — This is for metadata you want to store on the assistant.
    
</dd>
</dl>

<dl>
<dd>

**background_speech_denoising_plan:** `typing.Optional[BackgroundSpeechDenoisingPlan]` 

This enables filtering of noise and background speech while the user is talking.

Features:
- Smart denoising using Krisp
- Fourier denoising

Smart denoising can be combined with or used independently of Fourier denoising.

Order of precedence:
- Smart denoising
- Fourier denoising
    
</dd>
</dl>

<dl>
<dd>

**analysis_plan:** `typing.Optional[AnalysisPlan]` — This is the plan for analysis of assistant's calls. Stored in `call.analysis`.
    
</dd>
</dl>

<dl>
<dd>

**artifact_plan:** `typing.Optional[ArtifactPlan]` — This is the plan for artifacts generated during assistant's calls. Stored in `call.artifact`.
    
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
- To attach monitors to the assistant, set `monitorPlan.monitorIds` to the set of monitor ids.
    
</dd>
</dl>

<dl>
<dd>

**credential_ids:** `typing.Optional[typing.List[str]]` — These are the credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can provide a subset using this.
    
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

**keypad_input_plan:** `typing.Optional[KeypadInputPlan]` — Configuration for collecting and processing DTMF keypad input during calls.
    
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
<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">list</a>(...) -> typing.List[Squad]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns squads for the authenticated organization. Filter results by creation or update timestamps and limit the number returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

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

**id_any:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only squads matching the provided ids
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">create</a>(...) -> Squad</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a squad that coordinates multiple assistants and their handoffs during a conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, SquadMemberDto
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.squads.create(
    members=[
        SquadMemberDto()
    ],
)

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

**request:** `CreateSquadDto` 
    
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

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">get</a>(...) -> Squad</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the squad identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.squads.get(
    id="id",
)

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

**id:** `str` — The unique identifier of the squad.
    
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

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">delete</a>(...) -> Squad</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the squad identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.squads.delete(
    id="id",
)

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

**id:** `str` — The unique identifier of the squad.
    
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

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">update</a>(...) -> Squad</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified fields of the squad identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, SquadMemberDto
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.squads.update(
    id="id",
    members=[
        SquadMemberDto()
    ],
)

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

**id:** `str` — The unique identifier of the squad.
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.List[SquadMemberDto]` 

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

## Calls
<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">list</a>(...) -> typing.List[Call]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns calls for the authenticated organization. Filter results by call ID, assistant ID, phone number ID, or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

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

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">create</a>(...) -> CreateCallsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a call using an assistant or squad. The request can reference saved resources or include transient configurations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

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

**assistant_version:** `typing.Optional[str]` 

This is the assistant version to use for this call. Supported only with
direct `assistantId`. Omit to follow the latest version.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[CreateCallDtoTransport]` — This is the transport of the call.
    
</dd>
</dl>

<dl>
<dd>

**customers:** `typing.Optional[typing.List[CreateCustomerDto]]` 

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

**squad_overrides:** `typing.Optional[AssistantOverrides]` 

These are the overrides for the `squad` or `squadId`'s member settings and template variables.
This will apply to all members of the squad.
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` 

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

This is a workflow that will be used for the call. To use an existing workflow, use `workflowId` instead.

To start a call with:
- Assistant, use `assistant` or `assistantId`
- Squad, use `squad` or `squadId`
- Workflow, use `workflow` or `workflowId`
    
</dd>
</dl>

<dl>
<dd>

**workflow_overrides:** `typing.Optional[WorkflowOverrides]` — These are the overrides for the `workflow` or `workflowId`'s settings and template variables.
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">get</a>(...) -> Call</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the call identified by its ID, including its status, configuration, and available call data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.get(
    id="id",
)

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

**id:** `str` — The unique identifier of the call.
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">delete</a>(...) -> Call</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the call identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.delete(
    id="id",
)

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

**ids:** `typing.Optional[typing.List[str]]` 

These are the Call IDs to be bulk deleted.
If provided, the call ID if any in the request query will be ignored
When requesting a bulk delete, updates when a call is deleted will be sent as a webhook to the server URL configured in the Org settings.
It may take up to a few hours to complete the bulk delete, and will be asynchronous.
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">update</a>(...) -> Call</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the call identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.update(
    id="id",
)

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

**id:** `str` — The unique identifier of the call.
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">call_artifact_controller_mono_recording_download</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.call_artifact_controller_mono_recording_download(
    id="id",
)

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

**id:** `str` — Call ID
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">call_artifact_controller_stereo_recording_download</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.call_artifact_controller_stereo_recording_download(
    id="id",
)

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

**id:** `str` — Call ID
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">call_artifact_controller_video_recording_download</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.call_artifact_controller_video_recording_download(
    id="id",
)

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

**id:** `str` — Call ID
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">call_artifact_controller_customer_recording_download</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.call_artifact_controller_customer_recording_download(
    id="id",
)

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

**id:** `str` — Call ID
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">call_artifact_controller_assistant_recording_download</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.call_artifact_controller_assistant_recording_download(
    id="id",
)

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

**id:** `str` — Call ID
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">call_artifact_controller_pcap_download</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.call_artifact_controller_pcap_download(
    id="id",
)

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

**id:** `str` — Call ID
    
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

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">call_artifact_controller_call_logs_download</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.calls.call_artifact_controller_call_logs_download(
    id="id",
)

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

**id:** `str` — Call ID
    
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

## Chats
<details><summary><code>client.chats.<a href="src/vapi/chats/client.py">list</a>(...) -> ChatPaginatedResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.chats.list(
    assistant_id_any="assistant-1,assistant-2,assistant-3",
)

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

**id:** `typing.Optional[str]` — This is the unique identifier for the chat to filter by.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the unique identifier for the assistant that will be used for the chat.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id_any:** `typing.Optional[str]` — Filter by multiple assistant IDs. Provide as comma-separated values.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the unique identifier for the squad that will be used for the chat.
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — This is the unique identifier for the session that will be used for the chat.
    
</dd>
</dl>

<dl>
<dd>

**previous_chat_id:** `typing.Optional[str]` — This is the unique identifier for the previous chat to filter by.
    
</dd>
</dl>

<dl>
<dd>

**id_any:** `typing.Optional[str]` — Filter by multiple chat IDs. Provide as comma-separated values.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListChatsRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListChatsRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.chats.<a href="src/vapi/chats/client.py">create</a>(...) -> CreateChatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new chat with optional SMS delivery via transport field. Requires at least one of: assistantId/assistant, sessionId, or previousChatId. Note: sessionId and previousChatId are mutually exclusive. Transport field enables SMS delivery with two modes: (1) New conversation - provide transport.phoneNumberId and transport.customer to create a new session, (2) Existing conversation - provide sessionId to use existing session data. Cannot specify both sessionId and transport fields together. The transport.useLLMGeneratedMessageForOutbound flag controls whether input is processed by LLM (true, default) or forwarded directly as SMS (false).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.chats.create(
    input="input",
)

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

**input:** `CreateChatDtoInput` 

This is the input text for the chat.
Can be a string or an array of chat messages.
This field is REQUIRED for chat creation.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.
    
</dd>
</dl>

<dl>
<dd>

**assistant:** `typing.Optional[CreateAssistantDto]` — This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.
    
</dd>
</dl>

<dl>
<dd>

**assistant_overrides:** `typing.Optional[AssistantOverrides]` 

These are the variable values that will be used to replace template variables in the assistant messages.
Only variable substitution is supported in chat contexts - other assistant properties cannot be overridden.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the squad that will be used for the chat. To use a transient squad, use `squad` instead.
    
</dd>
</dl>

<dl>
<dd>

**squad:** `typing.Optional[CreateSquadDto]` — This is the squad that will be used for the chat. To use an existing squad, use `squadId` instead.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the chat. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 

This is the ID of the session that will be used for the chat.
Mutually exclusive with previousChatId.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` 

This is a flag that determines whether the response should be streamed.
When true, the response will be sent as chunks of text.
    
</dd>
</dl>

<dl>
<dd>

**previous_chat_id:** `typing.Optional[str]` 

This is the ID of the chat that will be used as context for the new chat.
The messages from the previous chat will be used as context.
Mutually exclusive with sessionId.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[TwilioSmsChatTransport]` 

This is used to send the chat through a transport like SMS.
If transport.phoneNumberId and transport.customer are provided, creates a new session.
If sessionId is provided without transport fields, uses existing session data.
Cannot specify both sessionId and transport fields (phoneNumberId/customer) together.
    
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

<details><summary><code>client.chats.<a href="src/vapi/chats/client.py">get</a>(...) -> Chat</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.chats.get(
    id="id",
)

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

<details><summary><code>client.chats.<a href="src/vapi/chats/client.py">delete</a>(...) -> Chat</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.chats.delete(
    id="id",
)

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

<details><summary><code>client.chats.<a href="src/vapi/chats/client.py">create_response</a>(...) -> CreateResponseChatsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.chats.create_response(
    input="input",
)

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

**input:** `OpenAiResponsesRequestInput` 

This is the input text for the chat.
Can be a string or an array of chat messages.
This field is REQUIRED for chat creation.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.
    
</dd>
</dl>

<dl>
<dd>

**assistant:** `typing.Optional[CreateAssistantDto]` — This is the assistant that will be used for the chat. To use an existing assistant, use `assistantId` instead.
    
</dd>
</dl>

<dl>
<dd>

**assistant_overrides:** `typing.Optional[AssistantOverrides]` 

These are the variable values that will be used to replace template variables in the assistant messages.
Only variable substitution is supported in chat contexts - other assistant properties cannot be overridden.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the squad that will be used for the chat. To use a transient squad, use `squad` instead.
    
</dd>
</dl>

<dl>
<dd>

**squad:** `typing.Optional[CreateSquadDto]` — This is the squad that will be used for the chat. To use an existing squad, use `squadId` instead.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the chat. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 

This is the ID of the session that will be used for the chat.
Mutually exclusive with previousChatId.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Optional[bool]` — Whether to stream the response or not.
    
</dd>
</dl>

<dl>
<dd>

**previous_chat_id:** `typing.Optional[str]` 

This is the ID of the chat that will be used as context for the new chat.
The messages from the previous chat will be used as context.
Mutually exclusive with sessionId.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[TwilioSmsChatTransport]` 

This is used to send the chat through a transport like SMS.
If transport.phoneNumberId and transport.customer are provided, creates a new session.
If sessionId is provided without transport fields, uses existing session data.
Cannot specify both sessionId and transport fields (phoneNumberId/customer) together.
    
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

## Campaigns
<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_find_all</a>(...) -> CampaignPaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns outbound calling campaigns for the authenticated organization. Filter results by campaign ID, status, or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_find_all()

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

**id:** `typing.Optional[str]` — Filters campaigns by ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CampaignControllerFindAllRequestStatus]` — Filters campaigns by status.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[CampaignControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[CampaignControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_create</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an outbound calling campaign that calls a set of customers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_create(
    name="Q2 Sales Campaign",
)

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

**request:** `CreateCampaignDto` 
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_find_all_v_2</a>(...) -> CampaignSummaryPaginatedResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_find_all_v_2()

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

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CampaignControllerFindAllV2RequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**include_counters:** `typing.Optional[bool]` 

When true, every campaign in the response includes `contactCounters` and
`callMetrics`. These are aggregate queries over contacts and events —
batched across the page, so the cost is three queries per request rather
than three per campaign, but still opt-in rather than paid for on every
read. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[CampaignControllerFindAllV2RequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[CampaignControllerFindAllV2RequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_create_v_2</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_create_v_2(
    name="Q2 Sales Campaign",
)

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

**request:** `CreateCampaignDto` 
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_find_one_v_2</a>(...) -> CampaignSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_find_one_v_2(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**include_counters:** `typing.Optional[bool]` 

When true, the response includes `contactCounters` and `callMetrics`.
These are aggregate queries over the campaign's contacts and events, so
they are opt-in rather than paid for on every read. Defaults to false.
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_remove_v_2</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_remove_v_2(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_update_v_2</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_update_v_2(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateCampaignDto` 
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_find_one</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the outbound calling campaign identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the campaign.
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_remove</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the outbound calling campaign identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the campaign.
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_update</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the outbound calling campaign identified by its ID. Campaigns can be ended by updating their status to `ended`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateCampaignDto` 
    
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

<details><summary><code>client.campaigns.<a href="src/vapi/campaigns/client.py">campaign_controller_get_campaign_v_2_contacts</a>(...) -> CampaignContactPaginatedResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.campaigns.campaign_controller_get_campaign_v_2_contacts(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[CampaignControllerGetCampaignV2ContactsRequestStatusItem, typing.Sequence[CampaignControllerGetCampaignV2ContactsRequestStatusItem]]]` 

This is the status to filter contacts by. Pass once or multiple times to
filter on any of the provided statuses.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of contacts to return. Defaults to 50.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[CampaignControllerGetCampaignV2ContactsRequestSortBy]` 

This is the column to sort by. Defaults to `position` — the order contacts
were uploaded, which is also dial order.

`status` sorts by the enum's declaration order rather than alphabetically,
which means it reads as a lifecycle: pending, dispatched, completed,
failed, skipped, predial-failed.

Only columns on `campaign_contact` are sortable. Call-level values such as
cost or duration live on the call and are attached after this query, so
sorting by them here would only reorder the current page.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
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

## Sessions
<details><summary><code>client.sessions.<a href="src/vapi/sessions/client.py">list</a>(...) -> SessionPaginatedResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.sessions.list(
    assistant_id_any="assistant-1,assistant-2,assistant-3",
    customer_number_any="+1234567890,+0987654321",
)

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

**id:** `typing.Optional[str]` — This is the unique identifier for the session to filter by.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

This is the name of the customer. This is just for your own reference.

For SIP inbound calls, this is extracted from the `From` SIP header with format `"Display Name" <sip:username@domain>`.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the ID of the assistant to filter sessions by.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id_any:** `typing.Optional[str]` — Filter by multiple assistant IDs. Provide as comma-separated values.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the ID of the squad to filter sessions by.
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` — This is the ID of the workflow to filter sessions by.
    
</dd>
</dl>

<dl>
<dd>

**number_e_164_check_enabled:** `typing.Optional[bool]` 

This is the flag to toggle the E164 check for the `number` field. This is an advanced property which should be used if you know your use case requires it.

Use cases:
- `false`: To allow non-E164 numbers like `+001234567890`, `1234`, or `abc`. This is useful for dialing out to non-E164 numbers on your SIP trunks.
- `true` (default): To allow only E164 numbers like `+14155551234`. This is standard for PSTN calls.

If `false`, the `number` is still required to only contain alphanumeric characters (regex: `/^\+?[a-zA-Z0-9]+$/`).

@default true (E164 check is enabled)
    
</dd>
</dl>

<dl>
<dd>

**extension:** `typing.Optional[str]` — This is the extension that will be dialed after the call is answered.
    
</dd>
</dl>

<dl>
<dd>

**assistant_overrides:** `typing.Optional[str]` 

These are the overrides for the assistant's settings and template variables specific to this customer.
This allows customization of the assistant's behavior for individual customers in batch calls.
    
</dd>
</dl>

<dl>
<dd>

**squad_overrides:** `typing.Optional[str]` 

These are the overrides applied when the call targets a `squadId`. Mirrors
the call-level `squadOverrides` — use this instead of `assistantOverrides`
when the campaign or call is squad-based.
    
</dd>
</dl>

<dl>
<dd>

**number:** `typing.Optional[str]` — This is the number of the customer.
    
</dd>
</dl>

<dl>
<dd>

**sip_uri:** `typing.Optional[str]` — This is the SIP URI of the customer.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — This is the email of the customer.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — This is the external ID of the customer.
    
</dd>
</dl>

<dl>
<dd>

**customer_number_any:** `typing.Optional[str]` — Filter by any of the specified customer phone numbers (comma-separated).
    
</dd>
</dl>

<dl>
<dd>

**id_any:** `typing.Optional[str]` — Filter by multiple session IDs. Provide as comma-separated values.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — This will return sessions with the specified phoneNumberId.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id_any:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — This will return sessions with any of the specified phoneNumberIds.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListSessionsRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListSessionsRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.sessions.<a href="src/vapi/sessions/client.py">create</a>(...) -> Session</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.sessions.create()

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

**name:** `typing.Optional[str]` — This is a user-defined name for the session. Maximum length is 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreateSessionDtoStatus]` — This is the current status of the session. Can be either 'active' or 'completed'.
    
</dd>
</dl>

<dl>
<dd>

**expiration_seconds:** `typing.Optional[float]` — Session expiration time in seconds. Defaults to 24 hours (86400 seconds) if not set.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the ID of the assistant associated with this session. Use this when referencing an existing assistant.
    
</dd>
</dl>

<dl>
<dd>

**assistant:** `typing.Optional[CreateAssistantDto]` 

This is the assistant configuration for this session. Use this when creating a new assistant configuration.
If assistantId is provided, this will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**assistant_overrides:** `typing.Optional[AssistantOverrides]` 

These are the overrides for the assistant configuration.
Use this to provide variable values and other overrides when using assistantId.
Variable substitution will be applied to the assistant's messages and other text-based fields.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the squad ID associated with this session. Use this when referencing an existing squad.
    
</dd>
</dl>

<dl>
<dd>

**squad:** `typing.Optional[CreateSquadDto]` 

This is the squad configuration for this session. Use this when creating a new squad configuration.
If squadId is provided, this will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[CreateSessionDtoMessagesItem]]` — This is an array of chat messages in the session.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[CreateCustomerDto]` — This is the customer information associated with this session.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — This is the customerId of the customer associated with this session.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — This is the ID of the phone number associated with this session.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[ImportTwilioPhoneNumberDto]` — This is the phone number configuration for this session.
    
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

<details><summary><code>client.sessions.<a href="src/vapi/sessions/client.py">get</a>(...) -> Session</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.sessions.get(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.sessions.<a href="src/vapi/sessions/client.py">delete</a>(...) -> Session</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.sessions.delete(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.sessions.<a href="src/vapi/sessions/client.py">update</a>(...) -> Session</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.sessions.update(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the new name for the session. Maximum length is 40 characters.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateSessionDtoStatus]` — This is the new status for the session.
    
</dd>
</dl>

<dl>
<dd>

**expiration_seconds:** `typing.Optional[float]` — Session expiration time in seconds. Defaults to 24 hours (86400 seconds) if not set.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[UpdateSessionDtoMessagesItem]]` — This is the updated array of chat messages.
    
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
<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">list</a>(...) -> typing.List[ListPhoneNumbersResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns phone numbers for the authenticated organization. Filter results by creation or update timestamps and limit the number returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

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

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">create</a>(...) -> CreatePhoneNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Vapi phone number or imports a phone number from a supported provider, including Twilio, Vonage, Telnyx, or a bring-your-own provider.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment
from vapi.phone_numbers import CreatePhoneNumbersRequest_ByoPhoneNumber

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.phone_numbers.create(
    request=CreatePhoneNumbersRequest_ByoPhoneNumber(
        credential_id="credentialId",
    ),
)

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

**request:** `CreatePhoneNumbersRequest` 
    
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

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">phone_number_controller_find_all_paginated</a>(...) -> PhoneNumberPaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of phone numbers for the authenticated organization. Search by name, number, or SIP URI using a partial, case-insensitive match, and filter by creation or update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.phone_numbers.phone_number_controller_find_all_paginated()

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

**search:** `typing.Optional[str]` — This will search phone numbers by name, number, or SIP URI (partial match, case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[PhoneNumberControllerFindAllPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[PhoneNumberControllerFindAllPaginatedRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">get</a>(...) -> GetPhoneNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the phone number resource identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.phone_numbers.get(
    id="id",
)

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

**id:** `str` — The unique identifier of the phone number.
    
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

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">delete</a>(...) -> DeletePhoneNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the phone number resource identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.phone_numbers.delete(
    id="id",
)

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

**id:** `str` — The unique identifier of the phone number.
    
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

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">update</a>(...) -> UpdatePhoneNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified fields of the phone number resource identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment
from vapi.phone_numbers import UpdatePhoneNumbersRequestBody_ByoPhoneNumber

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.phone_numbers.update(
    id="id",
    request=UpdatePhoneNumbersRequestBody_ByoPhoneNumber(),
)

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

**id:** `str` — The unique identifier of the phone number.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdatePhoneNumbersRequestBody` 
    
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
<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">list</a>(...) -> typing.List[ListToolsResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns reusable tools for the authenticated organization. Filter results by creation or update timestamps and limit the number returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

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

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">create</a>(...) -> CreateToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a reusable tool that assistants can invoke during conversations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment
from vapi.tools import CreateToolsRequest_ApiRequest

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.tools.create(
    request=CreateToolsRequest_ApiRequest(
        method="POST",
        url="url",
    ),
)

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

**request:** `CreateToolsRequest` 
    
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

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">get</a>(...) -> GetToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the tool identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.tools.get(
    id="id",
)

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

**id:** `str` — The unique identifier of the tool.
    
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

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">delete</a>(...) -> DeleteToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the tool identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.tools.delete(
    id="id",
)

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

**id:** `str` — The unique identifier of the tool.
    
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

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">update</a>(...) -> UpdateToolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified fields of the tool identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment
from vapi.tools import UpdateToolsRequestBody_ApiRequest

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.tools.update(
    id="id",
    request=UpdateToolsRequestBody_ApiRequest(),
)

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

**id:** `str` — The unique identifier of the tool.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateToolsRequestBody` 
    
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
<details><summary><code>client.files.<a href="src/vapi/files/client.py">list</a>(...) -> typing.List[File]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns files uploaded to the authenticated organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.files.list(
    purpose="purpose",
)

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

**purpose:** `str` 
    
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

<details><summary><code>client.files.<a href="src/vapi/files/client.py">create</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a file for use with a Vapi knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.files.create(
    file="example_file",
)

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

**file:** `core.File` — The file to upload.
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[CreateFilesRequestPurpose]` — Optional product flow that owns the uploaded file.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[str]` — Optional JSON-encoded metadata for multipart uploads.
    
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

<details><summary><code>client.files.<a href="src/vapi/files/client.py">get</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the uploaded file identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.files.get(
    id="id",
)

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

**id:** `str` — The unique identifier of the file.
    
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

<details><summary><code>client.files.<a href="src/vapi/files/client.py">delete</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the uploaded file identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.files.delete(
    id="id",
)

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

**id:** `str` — The unique identifier of the file.
    
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

<details><summary><code>client.files.<a href="src/vapi/files/client.py">update</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the name of the uploaded file identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.files.update(
    id="id",
)

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

**id:** `str` — The unique identifier of the file.
    
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

## KnowledgeBasesV2
<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_find_all</a>(...) -> typing.List[KnowledgeBaseV2]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_find_all()

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

**limit:** `typing.Optional[float]` 
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_create</a>(...) -> KnowledgeBaseV2</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_create(
    name="name",
)

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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_files_get</a>(...) -> typing.List[KnowledgeBaseV2File]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_files_get(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_file_attach</a>(...) -> KnowledgeBaseV2File</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_file_attach(
    id="id",
    file_id="fileId",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` 
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_file_detach</a>(...) -> KnowledgeBaseV2File</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_file_detach(
    id="id",
    file_id="fileId",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` 
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_file_retry</a>(...) -> KnowledgeBaseV2File</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_file_retry(
    id="id",
    file_id="fileId",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` 
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_find_one</a>(...) -> KnowledgeBaseV2WithFiles</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_remove</a>(...) -> KnowledgeBaseV2</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.knowledge_bases_v_2.<a href="src/vapi/knowledge_bases_v_2/client.py">knowledge_base_v_2_controller_update</a>(...) -> KnowledgeBaseV2</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.knowledge_bases_v_2.knowledge_base_v_2_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

## StructuredOutputs
<details><summary><code>client.structured_outputs.<a href="src/vapi/structured_outputs/client.py">structured_output_controller_find_all</a>(...) -> StructuredOutputPaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns structured-output definitions for the authenticated organization. Filter results by ID, name, or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.structured_outputs.structured_output_controller_find_all()

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

**id:** `typing.Optional[str]` — This will return structured outputs where the id matches the specified value.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This will return structured outputs where the name matches the specified value.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[StructuredOutputControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[StructuredOutputControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.structured_outputs.<a href="src/vapi/structured_outputs/client.py">structured_output_controller_create</a>(...) -> StructuredOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a reusable definition for extracting validated data from conversations using an AI model or regular expression.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, JsonSchema
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.structured_outputs.structured_output_controller_create(
    name="name",
    schema=JsonSchema(
        type="string",
    ),
)

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

**request:** `CreateStructuredOutputDto` 
    
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

<details><summary><code>client.structured_outputs.<a href="src/vapi/structured_outputs/client.py">structured_output_controller_find_one</a>(...) -> StructuredOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the structured-output definition identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.structured_outputs.structured_output_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the structured output.
    
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

<details><summary><code>client.structured_outputs.<a href="src/vapi/structured_outputs/client.py">structured_output_controller_remove</a>(...) -> StructuredOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the structured-output definition identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.structured_outputs.structured_output_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the structured output.
    
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

<details><summary><code>client.structured_outputs.<a href="src/vapi/structured_outputs/client.py">structured_output_controller_update</a>(...) -> StructuredOutput</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the structured-output definition identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.structured_outputs.structured_output_controller_update(
    id="id",
    schema_override="schemaOverride",
)

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

**id:** `str` — The unique identifier of the structured output.
    
</dd>
</dl>

<dl>
<dd>

**schema_override:** `str` — Set to the string `true` to allow changing the schema's top-level type. Other values do not enable schema type changes.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateStructuredOutputDtoType]` 

This is the type of structured output.

- 'ai': Uses an LLM to extract structured data from the conversation (default).
- 'regex': Uses a regex pattern to extract data from the transcript without an LLM.
    
</dd>
</dl>

<dl>
<dd>

**regex:** `typing.Optional[str]` 

This is the regex pattern to match against the transcript.

Only used when type is 'regex'. Supports both raw patterns (e.g. '\d+') and
regex literal format (e.g. '/\d+/gi'). Uses RE2 syntax for safety.

The result depends on the schema type:
- boolean: true if the pattern matches, false otherwise
- string: the first match or first capture group
- number/integer: the first match parsed as a number
- array: all matches
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[UpdateStructuredOutputDtoModel]` 

This is the model that will be used to extract the structured output.

To provide your own custom system and user prompts for structured output extraction, populate the messages array with your system and user messages. You can specify liquid templating in your system and user messages.
Between the system or user messages, you must reference either 'transcript' or 'messages' with the `{{}}` syntax to access the conversation history.
Between the system or user messages, you must reference a variation of the structured output with the `{{}}` syntax to access the structured output definition.
i.e.:
`{{structuredOutput}}`
`{{structuredOutput.name}}`
`{{structuredOutput.description}}`
`{{structuredOutput.schema}}`

If model is not specified, GPT-4.1 will be used by default for extraction, utilizing default system and user prompts.
If messages or required fields are not specified, the default system and user prompts will be used.
    
</dd>
</dl>

<dl>
<dd>

**compliance_plan:** `typing.Optional[ComplianceOverride]` — Compliance configuration for this output. Only enable overrides if no sensitive data will be stored.
    
</dd>
</dl>

<dl>
<dd>

**conditions:** `typing.Optional[typing.List[UpdateStructuredOutputDtoConditionsItem]]` — These are the conditions that gate the execution of this structured output. Every condition must pass for the structured output to run (AND semantics). When omitted or empty, no user-defined conditions gate this output. Send null to clear a previously saved gate.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the structured output.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

This is the description of what the structured output extracts.

Use this to provide context about what data will be extracted and how it will be used.
    
</dd>
</dl>

<dl>
<dd>

**assistant_ids:** `typing.Optional[typing.List[str]]` 

These are the assistant IDs that this structured output is linked to.

When linked to assistants, this structured output will be available for extraction during those assistant's calls.
    
</dd>
</dl>

<dl>
<dd>

**workflow_ids:** `typing.Optional[typing.List[str]]` 

These are the workflow IDs that this structured output is linked to.

When linked to workflows, this structured output will be available for extraction during those workflow's execution.
    
</dd>
</dl>

<dl>
<dd>

**schema:** `typing.Optional[JsonSchema]` 

This is the JSON Schema definition for the structured output.

Defines the structure and validation rules for the data that will be extracted. Supports all JSON Schema features including:
- Objects and nested properties
- Arrays and array validation
- String, number, boolean, and null types
- Enums and const values
- Validation constraints (min/max, patterns, etc.)
- Composition with allOf, anyOf, oneOf
    
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

<details><summary><code>client.structured_outputs.<a href="src/vapi/structured_outputs/client.py">structured_output_controller_run</a>(...) -> StructuredOutputControllerRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs a saved or transient structured-output definition against one or more calls, optionally returning a preview without updating call artifacts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.structured_outputs.structured_output_controller_run(
    call_ids=[
        "callIds"
    ],
)

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

**call_ids:** `typing.List[str]` 

This is the array of callIds that will be updated with the new structured output value. If preview is true, this array must be provided and contain exactly 1 callId.
If preview is false, up to 100 callIds may be provided.
    
</dd>
</dl>

<dl>
<dd>

**preview_enabled:** `typing.Optional[bool]` 

This is the preview flag for the re-run. If true, the re-run will be executed and the response will be returned immediately and the call artifact will NOT be updated.
If false (default), the re-run will be executed and the response will be updated in the call artifact.
    
</dd>
</dl>

<dl>
<dd>

**structured_output_id:** `typing.Optional[str]` 

This is the ID of the structured output that will be run. This must be provided unless a transient structured output is provided.
When the re-run is executed, only the value of this structured output will be replaced with the new value, or added if not present.
    
</dd>
</dl>

<dl>
<dd>

**structured_output:** `typing.Optional[CreateStructuredOutputDto]` 

This is the transient structured output that will be run. This must be provided if a structured output ID is not provided.
When the re-run is executed, the structured output value will be added to the existing artifact.
    
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

## SimulationPersonalities
<details><summary><code>client.simulation_personalities.<a href="src/vapi/simulation_personalities/client.py">personality_controller_find_all</a>(...) -> typing.List[Personality]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the personalities for the authenticated organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_personalities.personality_controller_find_all()

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

**sort_order:** `typing.Optional[PersonalityControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[PersonalityControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.simulation_personalities.<a href="src/vapi/simulation_personalities/client.py">personality_controller_create</a>(...) -> Personality</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a personality, the AI tester's configuration used in simulations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, CreateAssistantDto
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_personalities.personality_controller_create(
    name="name",
    assistant=CreateAssistantDto(),
)

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

**request:** `CreatePersonalityDto` 
    
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

<details><summary><code>client.simulation_personalities.<a href="src/vapi/simulation_personalities/client.py">personality_controller_find_one</a>(...) -> Personality</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified personality.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_personalities.personality_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the personality.
    
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

<details><summary><code>client.simulation_personalities.<a href="src/vapi/simulation_personalities/client.py">personality_controller_remove</a>(...) -> Personality</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified personality.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_personalities.personality_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the personality.
    
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

<details><summary><code>client.simulation_personalities.<a href="src/vapi/simulation_personalities/client.py">personality_controller_update</a>(...) -> Personality</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified personality. Changes apply to future runs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_personalities.personality_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier of the personality.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the personality.
    
</dd>
</dl>

<dl>
<dd>

**assistant:** `typing.Optional[CreateAssistantDto]` — This is the full assistant configuration for this personality.
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 

Optional folder path for organizing personalities.
Supports up to 3 levels (e.g., "dept/feature/variant").
Set to null to remove from folder.
    
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

## SimulationScenarios
<details><summary><code>client.simulation_scenarios.<a href="src/vapi/simulation_scenarios/client.py">scenario_controller_find_all</a>(...) -> typing.List[Scenario]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the scenarios for the authenticated organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_scenarios.scenario_controller_find_all()

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

**id_any:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only scenarios matching the provided ids
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Search by scenario name
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ScenarioControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ScenarioControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.simulation_scenarios.<a href="src/vapi/simulation_scenarios/client.py">scenario_controller_create</a>(...) -> Scenario</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a scenario, the AI tester's intent plus the success criteria that score a run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, EvaluationPlanItem
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_scenarios.scenario_controller_create(
    name="Health Enrollment - Eligible Path",
    instructions="You are calling to enroll in the Twin Health program. Confirm your identity when asked.",
    evaluations=[
        EvaluationPlanItem(
            comparator="=",
            value=1.1,
        )
    ],
)

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

**request:** `CreateScenarioDto` 
    
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

<details><summary><code>client.simulation_scenarios.<a href="src/vapi/simulation_scenarios/client.py">scenario_controller_find_one</a>(...) -> Scenario</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified scenario.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_scenarios.scenario_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the scenario.
    
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

<details><summary><code>client.simulation_scenarios.<a href="src/vapi/simulation_scenarios/client.py">scenario_controller_remove</a>(...) -> Scenario</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified scenario.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_scenarios.scenario_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the scenario.
    
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

<details><summary><code>client.simulation_scenarios.<a href="src/vapi/simulation_scenarios/client.py">scenario_controller_update</a>(...) -> Scenario</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified scenario.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_scenarios.scenario_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier of the scenario.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the scenario.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` — This is the script/instructions for the tester to follow during the simulation.
    
</dd>
</dl>

<dl>
<dd>

**evaluations:** `typing.Optional[typing.List[EvaluationPlanItem]]` 

This is the structured output-based evaluation plan for the simulation.
Each item defines a structured output to extract and evaluate against an expected value.
    
</dd>
</dl>

<dl>
<dd>

**hooks:** `typing.Optional[typing.List[UpdateScenarioDtoHooksItem]]` — Hooks to run on simulation lifecycle events
    
</dd>
</dl>

<dl>
<dd>

**target_overrides:** `typing.Optional[AssistantOverrides]` — Overrides to inject into the simulated target assistant or squad
    
</dd>
</dl>

<dl>
<dd>

**tool_mocks:** `typing.Optional[typing.List[ScenarioToolMock]]` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 

Optional folder path for organizing scenarios.
Supports up to 3 levels (e.g., "dept/feature/variant").
Set to null to remove from folder.
    
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

## SimulationRuns
<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_find_all</a>(...) -> SimulationRunControllerFindAllResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the simulation runs for the authenticated organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_find_all()

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

**status:** `typing.Optional[SimulationRunControllerFindAllRequestStatus]` — Filter by status
    
</dd>
</dl>

<dl>
<dd>

**filter_status:** `typing.Optional[SimulationRunControllerFindAllRequestFilterStatus]` — Filter by aggregate run result status
    
</dd>
</dl>

<dl>
<dd>

**target_type:** `typing.Optional[SimulationRunControllerFindAllRequestTargetType]` — Filter by target type
    
</dd>
</dl>

<dl>
<dd>

**target_id:** `typing.Optional[str]` — Filter by target id
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SimulationRunControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SimulationRunControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_create</a>(...) -> CreateSimulationRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a simulation run against a target assistant or squad.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment
from vapi.simulation_runs import CreateSimulationRunDtoSimulationsItem_Simulation, CreateSimulationRunDtoTarget_Assistant

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_create(
    simulations=[
        CreateSimulationRunDtoSimulationsItem_Simulation()
    ],
    target=CreateSimulationRunDtoTarget_Assistant(),
)

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

**simulations:** `typing.List[CreateSimulationRunDtoSimulationsItem]` — Array of simulations and/or suites to run
    
</dd>
</dl>

<dl>
<dd>

**target:** `CreateSimulationRunDtoTarget` — Target to test against
    
</dd>
</dl>

<dl>
<dd>

**iterations:** `typing.Optional[float]` — Number of times to run each simulation (default: 1)
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[SimulationRunTransportConfiguration]` — Transport configuration for the simulation runs
    
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

<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_find_one</a>(...) -> SimulationRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified simulation run, including its status and item counts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation run.
    
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

<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_cancel_group</a>(...) -> SimulationRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels the specified simulation run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_cancel_group(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation run.
    
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

<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_find_items</a>(...) -> typing.List[SimulationRunItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the run items for the specified simulation run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_find_items(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation run.
    
</dd>
</dl>

<dl>
<dd>

**simulation_id:** `typing.Optional[str]` — Filters run items to a specific simulation.
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `typing.Optional[str]` — Filters run items to a specific run.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SimulationRunControllerFindItemsRequestStatus]` — Filters run items by status.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SimulationRunControllerFindItemsRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SimulationRunControllerFindItemsRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_find_item</a>(...) -> SimulationRunItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified run item, including its evaluation results and the ID of the call that ran it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_find_item(
    id="id",
    item_id="itemId",
)

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

**id:** `str` — The unique identifier of the simulation run.
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — The unique identifier of the run item.
    
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

<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_cancel_item</a>(...) -> SimulationRunItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels the specified run item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_cancel_item(
    id="id",
    item_id="itemId",
)

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

**id:** `str` — The unique identifier of the simulation run.
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — The unique identifier of the run item.
    
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

<details><summary><code>client.simulation_runs.<a href="src/vapi/simulation_runs/client.py">simulation_run_controller_generate_suggestions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates AI suggestions for improving the assistant or squad's system prompt, tools, and scenarios, based on the specified run item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_runs.simulation_run_controller_generate_suggestions(
    id="id",
    item_id="itemId",
    force="force",
)

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

**id:** `str` — The unique identifier of the simulation run.
    
</dd>
</dl>

<dl>
<dd>

**item_id:** `str` — The unique identifier of the run item.
    
</dd>
</dl>

<dl>
<dd>

**force:** `str` — Set to the string `true` to regenerate improvement suggestions even if they already exist.
    
</dd>
</dl>

<dl>
<dd>

**persist:** `typing.Optional[str]` 
    
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

## SimulationSuites
<details><summary><code>client.simulation_suites.<a href="src/vapi/simulation_suites/client.py">simulation_suite_controller_find_all</a>(...) -> typing.List[SimulationSuite]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the simulation suites for the authenticated organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_suites.simulation_suite_controller_find_all()

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

**name:** `typing.Optional[str]` — Search by simulation suite name
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SimulationSuiteControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SimulationSuiteControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.simulation_suites.<a href="src/vapi/simulation_suites/client.py">simulation_suite_controller_create</a>(...) -> SimulationSuite</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a simulation suite, a group of simulations that run together.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_suites.simulation_suite_controller_create(
    name="Checkout Flow Tests",
    simulation_ids=[
        "simulationIds"
    ],
)

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

**name:** `str` — The display name of the suite.
    
</dd>
</dl>

<dl>
<dd>

**simulation_ids:** `typing.List[str]` — The IDs of the simulations included in the suite.
    
</dd>
</dl>

<dl>
<dd>

**slack_webhook_url:** `typing.Optional[str]` — A Slack incoming-webhook URL notified when the suite runs.
    
</dd>
</dl>

<dl>
<dd>

**target_assignments:** `typing.Optional[typing.List[SimulationSuiteTargetAssignment]]` — The assistants or squads the suite's simulations run against.
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 

Optional folder path for organizing simulation suites.
Supports up to 3 levels (e.g., "dept/feature/variant").
Maps to GitOps resource folder structure.
    
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

<details><summary><code>client.simulation_suites.<a href="src/vapi/simulation_suites/client.py">simulation_suite_controller_duplicate</a>(...) -> SimulationSuite</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_suites.simulation_suite_controller_duplicate(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.simulation_suites.<a href="src/vapi/simulation_suites/client.py">simulation_suite_controller_find_one</a>(...) -> SimulationSuite</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified simulation suite.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_suites.simulation_suite_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation suite.
    
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

<details><summary><code>client.simulation_suites.<a href="src/vapi/simulation_suites/client.py">simulation_suite_controller_remove</a>(...) -> SimulationSuite</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified simulation suite.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_suites.simulation_suite_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation suite.
    
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

<details><summary><code>client.simulation_suites.<a href="src/vapi/simulation_suites/client.py">simulation_suite_controller_update</a>(...) -> SimulationSuite</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified simulation suite.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulation_suites.simulation_suite_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation suite.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the simulation suite.
    
</dd>
</dl>

<dl>
<dd>

**slack_webhook_url:** `typing.Optional[str]` — This is the Slack webhook URL for notifications.
    
</dd>
</dl>

<dl>
<dd>

**simulation_ids:** `typing.Optional[typing.List[str]]` — This is the list of simulation IDs to include in the suite (replaces existing).
    
</dd>
</dl>

<dl>
<dd>

**target_assignments:** `typing.Optional[typing.List[SimulationSuiteTargetAssignment]]` — Optional assistant or squad assignments (replaces existing).
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 

Optional folder path for organizing simulation suites.
Supports up to 3 levels (e.g., "dept/feature/variant").
Set to null to remove from folder.
    
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

## Simulations
<details><summary><code>client.simulations.<a href="src/vapi/simulations/client.py">simulation_generate_controller_generate</a>(...) -> GenerateScenariosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates scenarios for an assistant or squad by analyzing its configuration with AI.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulations.simulation_generate_controller_generate()

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

**assistant_id:** `typing.Optional[str]` — ID of the assistant to generate scenarios for
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — ID of the squad to generate scenarios for
    
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

<details><summary><code>client.simulations.<a href="src/vapi/simulations/client.py">simulation_controller_find_all</a>(...) -> typing.List[Simulation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the simulations for the authenticated organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulations.simulation_controller_find_all()

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

**id_any:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only simulations matching the provided ids
    
</dd>
</dl>

<dl>
<dd>

**standalone_only:** `typing.Optional[bool]` — Only include simulations that are not part of a suite
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[SimulationControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[SimulationControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.simulations.<a href="src/vapi/simulations/client.py">simulation_controller_create</a>(...) -> Simulation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a simulation by pairing a scenario with a personality.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulations.simulation_controller_create(
    scenario_id="scenarioId",
    personality_id="personalityId",
)

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

**scenario_id:** `str` — The ID of the scenario to run.
    
</dd>
</dl>

<dl>
<dd>

**personality_id:** `str` — The ID of the personality the AI tester uses.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional display name for the simulation.
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 

Optional folder path for organizing simulations.
Supports up to 3 levels (e.g., "dept/feature/variant").
Maps to GitOps resource folder structure.
    
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

<details><summary><code>client.simulations.<a href="src/vapi/simulations/client.py">simulation_controller_find_one</a>(...) -> Simulation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the specified simulation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulations.simulation_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation.
    
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

<details><summary><code>client.simulations.<a href="src/vapi/simulations/client.py">simulation_controller_remove</a>(...) -> Simulation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the specified simulation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulations.simulation_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation.
    
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

<details><summary><code>client.simulations.<a href="src/vapi/simulations/client.py">simulation_controller_update</a>(...) -> Simulation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the specified simulation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulations.simulation_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier of the simulation.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is an optional friendly name for the simulation.
    
</dd>
</dl>

<dl>
<dd>

**scenario_id:** `typing.Optional[str]` — This is the ID of the scenario to use for this simulation.
    
</dd>
</dl>

<dl>
<dd>

**personality_id:** `typing.Optional[str]` — This is the ID of the personality to use for this simulation.
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` 

Optional folder path for organizing simulations.
Supports up to 3 levels (e.g., "dept/feature/variant").
Set to null to remove from folder.
    
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

<details><summary><code>client.simulations.<a href="src/vapi/simulations/client.py">simulation_controller_get_concurrency</a>() -> SimulationConcurrencyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the organization's simulation concurrency limit, the number of active simulations, and how many more can start.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.simulations.simulation_controller_get_concurrency()

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

## Insight
<details><summary><code>client.insight.<a href="src/vapi/insight/client.py">insight_controller_find_all</a>(...) -> InsightPaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns saved reporting insights for the authenticated organization. Filter results by ID or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.insight.insight_controller_find_all()

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

**id:** `typing.Optional[str]` — Filters reporting insights by ID.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[InsightControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[InsightControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.insight.<a href="src/vapi/insight/client.py">insight_controller_create</a>(...) -> InsightControllerCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a saved reporting insight that queries call data and presents the results as a bar chart, pie chart, line chart, or text value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, JsonQueryOnCallTableWithStringTypeColumn
from vapi.environment import VapiEnvironment
from vapi.insight import InsightControllerCreateRequest_Bar

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.insight.insight_controller_create(
    request=InsightControllerCreateRequest_Bar(
        queries=[
            JsonQueryOnCallTableWithStringTypeColumn(
                type="vapiql-json",
                table="call",
                column="id",
                operation="count",
            )
        ],
    ),
)

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

**request:** `InsightControllerCreateRequest` 
    
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

<details><summary><code>client.insight.<a href="src/vapi/insight/client.py">insight_controller_find_one</a>(...) -> InsightControllerFindOneResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the reporting insight identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.insight.insight_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier of the reporting insight.
    
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

<details><summary><code>client.insight.<a href="src/vapi/insight/client.py">insight_controller_remove</a>(...) -> InsightControllerRemoveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the reporting insight identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.insight.insight_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the reporting insight.
    
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

<details><summary><code>client.insight.<a href="src/vapi/insight/client.py">insight_controller_update</a>(...) -> InsightControllerUpdateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the reporting insight identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment
from vapi.insight import InsightControllerUpdateRequestBody_Bar

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.insight.insight_controller_update(
    id="id",
    request=InsightControllerUpdateRequestBody_Bar(),
)

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

**id:** `str` — The unique identifier of the reporting insight.
    
</dd>
</dl>

<dl>
<dd>

**request:** `InsightControllerUpdateRequestBody` 
    
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

<details><summary><code>client.insight.<a href="src/vapi/insight/client.py">insight_controller_run</a>(...) -> InsightRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs a saved reporting insight, optionally overriding its time range and response format.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.insight.insight_controller_run(
    id="id",
)

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

**id:** `str` — The unique identifier of the reporting insight.
    
</dd>
</dl>

<dl>
<dd>

**format_plan:** `typing.Optional[InsightRunFormatPlan]` — Output-formatting instructions applied to the insight run.
    
</dd>
</dl>

<dl>
<dd>

**time_range_override:** `typing.Optional[InsightTimeRangeWithStep]` 

This is the optional time range override for the insight.
If provided, overrides every field in the insight's timeRange.
If this is provided with missing fields, defaults will be used, not the insight's timeRange.
start default - "-7d"
end default - "now"
step default - "day"
For Pie and Text Insights, step will be ignored even if provided.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` 

Optional runtime assistant scope for dashboards.
This is applied to call-table queries without mutating the saved insight.
    
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

<details><summary><code>client.insight.<a href="src/vapi/insight/client.py">insight_controller_preview</a>(...) -> InsightRunResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs an insight definition without first saving it, returning a preview of the resulting chart or text value.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, JsonQueryOnCallTableWithStringTypeColumn
from vapi.environment import VapiEnvironment
from vapi.insight import InsightControllerPreviewRequest_Bar

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.insight.insight_controller_preview(
    request=InsightControllerPreviewRequest_Bar(
        queries=[
            JsonQueryOnCallTableWithStringTypeColumn(
                type="vapiql-json",
                table="call",
                column="id",
                operation="count",
            )
        ],
    ),
)

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

**request:** `InsightControllerPreviewRequest` 
    
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

## Board
<details><summary><code>client.board.<a href="src/vapi/board/client.py">board_controller_find_all</a>(...) -> BoardPaginatedResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.board.board_controller_find_all()

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

**sort_order:** `typing.Optional[BoardControllerFindAllRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[BoardControllerFindAllRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.board.<a href="src/vapi/board/client.py">board_controller_create</a>(...) -> Board</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, BoardLayout
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.board.board_controller_create(
    name="name",
    layout=BoardLayout(
        columns=1.1,
    ),
)

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

**name:** `str` — This is the name of the Board.
    
</dd>
</dl>

<dl>
<dd>

**layout:** `BoardLayout` — This is the layout of the Board.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[CreateBoardDtoItemsItem]]` — This is the contents of the Board, which is an array of objects defining the type, contents, and position of the widgets on the Board.
    
</dd>
</dl>

<dl>
<dd>

**time_range_override:** `typing.Optional[InsightTimeRangeWithStep]` 

This is the timerange override for the board.
By default, individual insights have their own timerange.
This is a global override for the board which will be passed to all insights on the board.
    
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

<details><summary><code>client.board.<a href="src/vapi/board/client.py">board_controller_metrics_overview_ensure</a>() -> Board</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.board.board_controller_metrics_overview_ensure()

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

<details><summary><code>client.board.<a href="src/vapi/board/client.py">board_controller_find_one</a>(...) -> Board</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.board.board_controller_find_one(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.board.<a href="src/vapi/board/client.py">board_controller_remove</a>(...) -> Board</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.board.board_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
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

<details><summary><code>client.board.<a href="src/vapi/board/client.py">board_controller_update</a>(...) -> Board</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.board.board_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier for the resource.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[UpdateBoardDtoItemsItem]]` — This is the contents of the Board, which is an array of objects defining the type, contents, and position of the widgets on the Board.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the Board.
    
</dd>
</dl>

<dl>
<dd>

**layout:** `typing.Optional[BoardLayout]` — This is the layout of the Board.
    
</dd>
</dl>

<dl>
<dd>

**time_range_override:** `typing.Optional[InsightTimeRangeWithStep]` 

This is the timerange override for the board.
By default, individual insights have their own timerange.
This is a global override for the board which will be passed to all insights on the board.
    
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

## Eval
<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_get_paginated</a>(...) -> EvalPaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns eval definitions for the authenticated organization. Filter results by ID or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_get_paginated()

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

**id:** `typing.Optional[str]` — Filters eval definitions by ID.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[EvalControllerGetPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[EvalControllerGetPaginatedRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_create</a>(...) -> Eval</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a reusable eval that defines a mock conversation and checkpoints for evaluating assistant responses and tool calls.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, ChatEvalAssistantMessageMock
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_create(
    messages=[
        ChatEvalAssistantMessageMock(
            role="assistant",
        )
    ],
    type="chat.mockConversation",
)

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

**request:** `CreateEvalDto` 
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_get</a>(...) -> Eval</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the eval definition identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_get(
    id="id",
)

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

**id:** `str` — The unique identifier of the eval definition.
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_remove</a>(...) -> Eval</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the eval definition identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the eval definition.
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_update</a>(...) -> Eval</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the eval definition identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier of the eval definition.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.List[UpdateEvalDtoMessagesItem]]` 

This is the mock conversation that will be used to evaluate the flow of the conversation.

Mock Messages are used to simulate the flow of the conversation

Evaluation Messages are used as checkpoints in the flow where the model's response to previous conversation needs to be evaluated to check the content and tool calls
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

This is the name of the eval.
It helps identify what the eval is checking for.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

This is the description of the eval.
This helps describe the eval and its purpose in detail. It will not be used to evaluate the flow of the conversation.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateEvalDtoType]` 

This is the type of the eval.
Currently it is fixed to `chat.mockConversation`.
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_get_run</a>(...) -> EvalRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the eval run identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_get_run(
    id="id",
)

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

**id:** `str` — The unique identifier of the eval run.
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_remove_run</a>(...) -> EvalRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the eval run identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_remove_run(
    id="id",
)

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

**id:** `str` — The unique identifier of the eval run.
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_get_runs_paginated</a>(...) -> EvalRunPaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns eval runs for the authenticated organization. Filter results by ID or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_get_runs_paginated()

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

**id:** `typing.Optional[str]` — Filters eval runs by ID.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[EvalControllerGetRunsPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[EvalControllerGetRunsPaginatedRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.eval.<a href="src/vapi/eval/client.py">eval_controller_run</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs a saved or transient eval against an assistant or squad and creates an eval-run record containing the results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment
from vapi.eval import CreateEvalRunDtoTarget_Assistant

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.eval.eval_controller_run(
    target=CreateEvalRunDtoTarget_Assistant(),
    type="eval",
)

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

**target:** `CreateEvalRunDtoTarget` — This is the target that will be run against the eval
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateEvalRunDtoType` 

This is the type of the run.
Currently it is fixed to `eval`.
    
</dd>
</dl>

<dl>
<dd>

**eval:** `typing.Optional[CreateEvalDto]` — This is the transient eval that will be run
    
</dd>
</dl>

<dl>
<dd>

**eval_id:** `typing.Optional[str]` — This is the id of the eval that will be run.
    
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

## ObservabilityScorecard
<details><summary><code>client.observability_scorecard.<a href="src/vapi/observability_scorecard/client.py">scorecard_controller_get</a>(...) -> Scorecard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the scorecard identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.observability_scorecard.scorecard_controller_get(
    id="id",
)

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

**id:** `str` — The unique identifier of the scorecard.
    
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

<details><summary><code>client.observability_scorecard.<a href="src/vapi/observability_scorecard/client.py">scorecard_controller_remove</a>(...) -> Scorecard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the scorecard identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.observability_scorecard.scorecard_controller_remove(
    id="id",
)

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

**id:** `str` — The unique identifier of the scorecard.
    
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

<details><summary><code>client.observability_scorecard.<a href="src/vapi/observability_scorecard/client.py">scorecard_controller_update</a>(...) -> Scorecard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the scorecard identified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.observability_scorecard.scorecard_controller_update(
    id="id",
)

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

**id:** `str` — The unique identifier of the scorecard.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the scorecard. It is only for user reference and will not be used for any evaluation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — This is the description of the scorecard. It is only for user reference and will not be used for any evaluation.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.List[ScorecardMetric]]` 

These are the metrics that will be used to evaluate the scorecard.
Each metric will have a set of conditions and points that will be used to generate the score.
    
</dd>
</dl>

<dl>
<dd>

**assistant_ids:** `typing.Optional[typing.List[str]]` 

These are the assistant IDs that this scorecard is linked to.
When linked to assistants, this scorecard will be available for evaluation during those assistants' calls.
    
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

<details><summary><code>client.observability_scorecard.<a href="src/vapi/observability_scorecard/client.py">scorecard_controller_get_paginated</a>(...) -> ScorecardPaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns scorecards for the authenticated organization. Filter results by ID or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.observability_scorecard.scorecard_controller_get_paginated()

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

**id:** `typing.Optional[str]` — Filters scorecards by ID.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ScorecardControllerGetPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ScorecardControllerGetPaginatedRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.observability_scorecard.<a href="src/vapi/observability_scorecard/client.py">scorecard_controller_create</a>(...) -> Scorecard</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a scorecard containing metrics, scoring conditions, and optional links to assistants whose calls should be evaluated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, ScorecardMetric, NumberComparatorScorecardMetricCondition
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.observability_scorecard.scorecard_controller_create(
    metrics=[
        ScorecardMetric(
            conditions=[
                NumberComparatorScorecardMetricCondition(
                    type="comparator",
                    comparator="=",
                    value=1.1,
                    points=1.1,
                )
            ],
            structured_output_id="structuredOutputId",
        )
    ],
)

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

**request:** `CreateScorecardDto` 
    
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

## ProviderResources
<details><summary><code>client.provider_resources.<a href="src/vapi/provider_resources/client.py">provider_resource_controller_get_provider_resources_paginated</a>(...) -> ProviderResourcePaginatedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of provider resources for the authenticated organization. Filter pronunciation dictionaries by provider, resource ID, or creation and update timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.provider_resources.provider_resource_controller_get_provider_resources_paginated(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
)

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

**provider:** `ProviderResourceControllerGetProviderResourcesPaginatedRequestProvider` — The provider (e.g., 11labs)
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `ProviderResourceControllerGetProviderResourcesPaginatedRequestResourceName` — The resource name (e.g., pronunciation-dictionary)
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Filters provider resources by their resource ID.
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[str]` — Filters provider resources by their provider-specific resource ID.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ProviderResourceControllerGetProviderResourcesPaginatedRequestSortOrder]` — This is the sort order for pagination. Defaults to 'DESC'.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ProviderResourceControllerGetProviderResourcesPaginatedRequestSortBy]` — This is the column to sort by. Defaults to 'createdAt'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[datetime.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
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

<details><summary><code>client.provider_resources.<a href="src/vapi/provider_resources/client.py">provider_resource_controller_create_provider_resource</a>(...) -> ProviderResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a pronunciation-dictionary resource for a supported provider, currently Cartesia or ElevenLabs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.provider_resources.provider_resource_controller_create_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
)

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

**provider:** `ProviderResourceControllerCreateProviderResourceRequestProvider` — The provider (e.g., 11labs)
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `ProviderResourceControllerCreateProviderResourceRequestResourceName` — The resource name (e.g., pronunciation-dictionary)
    
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

<details><summary><code>client.provider_resources.<a href="src/vapi/provider_resources/client.py">provider_resource_controller_get_provider_resource</a>(...) -> ProviderResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the provider resource identified by its Vapi resource ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.provider_resources.provider_resource_controller_get_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
    id="id",
)

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

**provider:** `ProviderResourceControllerGetProviderResourceRequestProvider` — The provider (e.g., 11labs)
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `ProviderResourceControllerGetProviderResourceRequestResourceName` — The resource name (e.g., pronunciation-dictionary)
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier of the provider resource.
    
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

<details><summary><code>client.provider_resources.<a href="src/vapi/provider_resources/client.py">provider_resource_controller_delete_provider_resource</a>(...) -> ProviderResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the provider resource identified by its Vapi resource ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.provider_resources.provider_resource_controller_delete_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
    id="id",
)

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

**provider:** `ProviderResourceControllerDeleteProviderResourceRequestProvider` — The provider (e.g., 11labs)
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `ProviderResourceControllerDeleteProviderResourceRequestResourceName` — The resource name (e.g., pronunciation-dictionary)
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier of the provider resource.
    
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

<details><summary><code>client.provider_resources.<a href="src/vapi/provider_resources/client.py">provider_resource_controller_update_provider_resource</a>(...) -> ProviderResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the provider resource identified by its Vapi resource ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.provider_resources.provider_resource_controller_update_provider_resource(
    provider="cartesia",
    resource_name="pronunciation-dictionary",
    id="id",
)

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

**provider:** `ProviderResourceControllerUpdateProviderResourceRequestProvider` — The provider (e.g., 11labs)
    
</dd>
</dl>

<dl>
<dd>

**resource_name:** `ProviderResourceControllerUpdateProviderResourceRequestResourceName` — The resource name (e.g., pronunciation-dictionary)
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier of the provider resource.
    
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
<details><summary><code>client.analytics.<a href="src/vapi/analytics/client.py">get</a>(...) -> typing.List[AnalyticsQueryResult]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs one or more metric queries against call or subscription data using the requested time range, groupings, and aggregate operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi, AnalyticsQuery, AnalyticsOperation
from vapi.environment import VapiEnvironment

client = Vapi(
    token="<token>",
    environment=VapiEnvironment.DEFAULT,
)

client.analytics.get(
    queries=[
        AnalyticsQuery(
            table="call",
            name="name",
            operations=[
                AnalyticsOperation(
                    operation="sum",
                    column="id",
                )
            ],
        )
    ],
)

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

**queries:** `typing.List[AnalyticsQuery]` — This is the list of metric queries you want to perform.
    
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

