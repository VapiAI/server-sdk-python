# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .regex_option import RegexOption


class AssistantCustomEndpointingRule(UncheckedBaseModel):
    type: typing.Literal["assistant"] = pydantic.Field(default="assistant")
    """
    This endpointing rule is based on the last assistant message before customer started speaking.
    
    Flow:
    - Assistant speaks
    - Customer starts speaking
    - Customer transcription comes in
    - This rule is evaluated on the last assistant message
    - If a match is found based on `regex`, the endpointing timeout is set to `timeoutSeconds`
    
    Usage:
    - If you have yes/no questions in your use case like "are you interested in a loan?", you can set a shorter timeout.
    - If you have questions where the customer may pause to look up information like "what's my account number?", you can set a longer timeout.
    """

    regex: str = pydantic.Field()
    """
    This is the regex pattern to match.
    
    Note:
    - This works by using the `RegExp.test` method in Node.JS. Eg. `/hello/.test("hello there")` will return `true`.
    
    Hot tip:
    - In JavaScript, escape `\` when sending the regex pattern. Eg. `"hello\sthere"` will be sent over the wire as `"hellosthere"`. Send `"hello\\sthere"` instead.
    - `RegExp.test` does substring matching, so `/cat/.test("I love cats")` will return `true`. To do full string matching, send "^cat$".
    """

    regex_options: typing_extensions.Annotated[
        typing.Optional[typing.List[RegexOption]], FieldMetadata(alias="regexOptions")
    ] = pydantic.Field(default=None)
    """
    These are the options for the regex match. Defaults to all disabled.
    
    @default []
    """

    timeout_seconds: typing_extensions.Annotated[float, FieldMetadata(alias="timeoutSeconds")] = pydantic.Field()
    """
    This is the endpointing timeout in seconds, if the rule is matched.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
