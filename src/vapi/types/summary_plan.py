# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel


class SummaryPlan(UncheckedBaseModel):
    messages: typing.Optional[typing.List[typing.Dict[str, typing.Optional[typing.Any]]]] = pydantic.Field(default=None)
    """
    These are the messages used to generate the summary.
    
    @default: ```
    [
      {
        "role": "system",
        "content": "You are an expert note-taker. You will be given a transcript of a call. Summarize the call in 2-3 sentences. DO NOT return anything except the summary."
      },
      {
        "role": "user",
        "content": "Here is the transcript:\n\n{{transcript}}\n\n. Here is the ended reason of the call:\n\n{{endedReason}}\n\n"
      }
    ]```
    
    You can customize by providing any messages you want.
    
    Here are the template variables available:
    - {{transcript}}: The transcript of the call from `call.artifact.transcript` 
    - {{systemPrompt}}: The system prompt of the call from `assistant.model.messages[type=system].content` 
    - {{endedReason}}: The ended reason of the call from `call.endedReason`
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This determines whether a summary is generated and stored in `call.analysis.summary`. Defaults to true.
    
    Usage:
    - If you want to disable the summary, set this to false.
    
    @default true
    """

    timeout_seconds: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="timeoutSeconds")] = (
        pydantic.Field(default=None)
    )
    """
    This is how long the request is tried before giving up. When request times out, `call.analysis.summary` will be empty.
    
    Usage:
    - To guarantee the summary is generated, set this value high. Note, this will delay the end of call report in cases where model is slow to respond.
    
    @default 5 seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
