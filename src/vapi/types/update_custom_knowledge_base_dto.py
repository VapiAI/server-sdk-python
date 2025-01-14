# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .server import Server
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateCustomKnowledgeBaseDto(UniversalBaseModel):
    server: typing.Optional[Server] = pydantic.Field(default=None)
    """
    /**
    This is where the knowledge base request will be sent.
    
    Request Example:
    
    POST https://{server.url}
    Content-Type: application/json
    
    {
      "messsage": {
        "type": "knowledge-base-request",
        "messages": [
          {
            "role": "user",
            "content": "Why is ocean blue?"
          }
        ],
        ...other metadata about the call...
      }
    }
    
    Response Expected:
    ```
    {
      "message": {
         "role": "assistant",
         "content": "The ocean is blue because water absorbs everything but blue.",
      }, // YOU CAN RETURN THE EXACT RESPONSE TO SPEAK
      "documents": [
        {
          "content": "The ocean is blue primarily because water absorbs colors in the red part of the light spectrum and scatters the blue light, making it more visible to our eyes.",
          "similarity": 1
        },
        {
          "content": "Blue light is scattered more by the water molecules than other colors, enhancing the blue appearance of the ocean.",
          "similarity": .5
        }
      ] // OR, YOU CAN RETURN AN ARRAY OF DOCUMENTS THAT WILL BE SENT TO THE MODEL
    }
    ```
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow