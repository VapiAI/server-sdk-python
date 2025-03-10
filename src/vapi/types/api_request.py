# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .api_request_method import ApiRequestMethod
import pydantic
from .json_schema import JsonSchema
from .api_request_mode import ApiRequestMode
from .hook import Hook
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ApiRequest(UncheckedBaseModel):
    type: typing.Literal["apiRequest"] = "apiRequest"
    method: ApiRequestMethod
    url: str = pydantic.Field()
    """
    Api endpoint to send requests to.
    """

    headers: typing.Optional[JsonSchema] = pydantic.Field(default=None)
    """
    These are the custom headers to include in the Api Request sent.
    
    Each key-value pair represents a header name and its value.
    """

    body: typing.Optional[JsonSchema] = pydantic.Field(default=None)
    """
    This defined the JSON body of your Api Request. For example, if `body_schema`
    included "my_field": "my_gather_statement.user_age", then the json body sent to the server would have that particular value assign to it.
    Right now, only data from gather statements are supported.
    """

    mode: ApiRequestMode = pydantic.Field()
    """
    This is the mode of the Api Request.
    We only support BLOCKING and BACKGROUND for now.
    """

    hooks: typing.Optional[typing.List[Hook]] = pydantic.Field(default=None)
    """
    This is a list of hooks for a task.
    Each hook is a list of tasks to run on a trigger (such as on start, on failure, etc).
    Only Say is supported for now.
    """

    output: typing.Optional[JsonSchema] = pydantic.Field(default=None)
    """
    This is the schema for the outputs of the Api Request.
    """

    name: str
    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    This is for metadata you want to store on the task.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
