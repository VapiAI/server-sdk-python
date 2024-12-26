# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .server import Server
import typing_extensions
from .chunk_plan import ChunkPlan
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackCustomVoice(UniversalBaseModel):
    provider: typing.Literal["custom-voice"] = pydantic.Field(default="custom-voice")
    """
    This is the voice provider that will be used. Use `custom-voice` for providers that are not natively supported.
    """

    server: Server = pydantic.Field()
    """
    This is where the voice request will be sent.
    
    Request Example:
    
    POST https://{server.url}
    Content-Type: application/json
    
    {
      "message": {
        "type": "voice-request",
        "text": "Hello, world!",
        "sampleRate": 24000,
        ...other metadata about the call...
      }
    }
    
    Response Expected: 1-channel 16-bit raw PCM audio at the sample rate specified in the request. Here is how the response will be piped to the transport:
    ```
    response.on('data', (chunk: Buffer) => {
      outputStream.write(chunk);
    });
    ```
    """

    chunk_plan: typing_extensions.Annotated[typing.Optional[ChunkPlan], FieldMetadata(alias="chunkPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for chunking the model output before it is sent to the voice provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
