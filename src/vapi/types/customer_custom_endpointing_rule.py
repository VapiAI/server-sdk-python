# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .regex_option import RegexOption


class CustomerCustomEndpointingRule(UncheckedBaseModel):
    type: typing.Literal["customer"] = pydantic.Field(default="customer")
    """
    This endpointing rule is based on current customer message as they are speaking.
    
    Flow:
    - Assistant speaks
    - Customer starts speaking
    - Customer transcription comes in
    - This rule is evaluated on the current customer transcription
    - If a match is found based on `regex`, the endpointing timeout is set to `timeoutSeconds`
    
    Usage:
    - If you want to wait longer while customer is speaking numbers, you can set a longer timeout.
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
