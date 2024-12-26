# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from .regex_option import RegexOption
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BothCustomEndpointingRule(UniversalBaseModel):
    type: typing.Literal["both"] = pydantic.Field(default="both")
    """
    This endpointing rule is based on both the last assistant message and the current customer message as they are speaking.
    
    Flow:
    - Assistant speaks
    - Customer starts speaking
    - Customer transcription comes in
    - This rule is evaluated on the last assistant message and the current customer transcription
    - If assistant message matches `assistantRegex` AND customer message matches `customerRegex`, the endpointing timeout is set to `timeoutSeconds`
    
    Usage:
    - If you want to wait longer while customer is speaking numbers, you can set a longer timeout.
    """

    assistant_regex: typing_extensions.Annotated[str, FieldMetadata(alias="assistantRegex")] = pydantic.Field()
    """
    This is the regex pattern to match the assistant's message.
    
    Note:
    - This works by using the `RegExp.test` method in Node.JS. Eg. `/hello/.test("hello there")` will return `true`.
    
    Hot tip:
    - In JavaScript, escape `\` when sending the regex pattern. Eg. `"hello\sthere"` will be sent over the wire as `"hellosthere"`. Send `"hello\\sthere"` instead.
    - `RegExp.test` does substring matching, so `/cat/.test("I love cats")` will return `true`. To do full string matching, send "^cat$".
    """

    assistant_regex_options: typing_extensions.Annotated[
        typing.Optional[typing.List[RegexOption]], FieldMetadata(alias="assistantRegexOptions")
    ] = pydantic.Field(default=None)
    """
    These are the options for the assistant's message regex match. Defaults to all disabled.
    
    @default []
    """

    customer_regex: typing_extensions.Annotated[str, FieldMetadata(alias="customerRegex")]
    customer_regex_options: typing_extensions.Annotated[
        typing.Optional[typing.List[RegexOption]], FieldMetadata(alias="customerRegexOptions")
    ] = pydantic.Field(default=None)
    """
    These are the options for the customer's message regex match. Defaults to all disabled.
    
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