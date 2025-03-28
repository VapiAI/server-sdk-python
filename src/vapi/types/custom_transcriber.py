# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .server import Server
import typing_extensions
from .fallback_transcriber_plan import FallbackTranscriberPlan
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CustomTranscriber(UncheckedBaseModel):
    provider: typing.Literal["custom-transcriber"] = pydantic.Field(default="custom-transcriber")
    """
    This is the transcription provider that will be used. Use `custom-transcriber` for providers that are not natively supported.
    """

    server: Server = pydantic.Field()
    """
    This is where the transcription request will be sent.
    
    Usage:
    1. Vapi will initiate a websocket connection with `server.url`.
    
    2. Vapi will send an initial text frame with the sample rate. Format:
    ```
        {
          "type": "start",
          "encoding": "linear16", // 16-bit raw PCM format
          "container": "raw",
          "sampleRate": {{sampleRate}},
          "channels": 2 // customer is channel 0, assistant is channel 1
        }
    ```
    
    3. Vapi will send the audio data in 16-bit raw PCM format as binary frames.
    
    4. You can read the messages something like this:
    ```
    ws.on('message', (data, isBinary) => {
      if (isBinary) {
        pcmBuffer = Buffer.concat([pcmBuffer, data]);
        console.log(`Received PCM data, buffer size: ${pcmBuffer.length}`);
      } else {
        console.log('Received message:', JSON.parse(data.toString()));
      }
    });
    ```
    
    5. You will respond with transcriptions as you have them. Format:
    ```
     {
        "type": "transcriber-response",
        "transcription": "Hello, world!",
        "channel": "customer" | "assistant"
     }
    ```
    """

    fallback_plan: typing_extensions.Annotated[
        typing.Optional[FallbackTranscriberPlan], FieldMetadata(alias="fallbackPlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan for voice provider fallbacks in the event that the primary voice provider fails.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
