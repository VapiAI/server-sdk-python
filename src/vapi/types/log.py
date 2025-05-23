# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .error import Error
from .log_request_http_method import LogRequestHttpMethod
from .log_resource import LogResource
from .log_type import LogType


class Log(UncheckedBaseModel):
    time: str = pydantic.Field()
    """
    This is the timestamp at which the log was written.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this log belongs to.
    """

    type: LogType = pydantic.Field()
    """
    This is the type of the log.
    """

    webhook_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="webhookType")] = (
        pydantic.Field(default=None)
    )
    """
    This is the type of the webhook, given the log is from a webhook.
    """

    resource: typing.Optional[LogResource] = pydantic.Field(default=None)
    """
    This is the specific resource, relevant only to API logs.
    """

    request_duration_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="requestDurationSeconds")
    ] = pydantic.Field(default=None)
    """
    'This is how long the request took.
    """

    request_started_at: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestStartedAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the timestamp at which the request began.
    """

    request_finished_at: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestFinishedAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the timestamp at which the request finished.
    """

    request_body: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="requestBody")
    ] = pydantic.Field(default=None)
    """
    This is the body of the request.
    """

    request_http_method: typing_extensions.Annotated[
        typing.Optional[LogRequestHttpMethod], FieldMetadata(alias="requestHttpMethod")
    ] = pydantic.Field(default=None)
    """
    This is the request method.
    """

    request_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestUrl")] = pydantic.Field(
        default=None
    )
    """
    This is the request URL.
    """

    request_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestPath")] = (
        pydantic.Field(default=None)
    )
    """
    This is the request path.
    """

    request_query: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestQuery")] = (
        pydantic.Field(default=None)
    )
    """
    This is the request query.
    """

    response_http_code: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="responseHttpCode")] = (
        pydantic.Field(default=None)
    )
    """
    This the HTTP status code of the response.
    """

    request_ip_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestIpAddress")] = (
        pydantic.Field(default=None)
    )
    """
    This is the request IP address.
    """

    request_origin: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestOrigin")] = (
        pydantic.Field(default=None)
    )
    """
    This is the origin of the request
    """

    response_body: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="responseBody")
    ] = pydantic.Field(default=None)
    """
    This is the body of the response.
    """

    request_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="requestHeaders")
    ] = pydantic.Field(default=None)
    """
    These are the headers of the request.
    """

    error: typing.Optional[Error] = pydantic.Field(default=None)
    """
    This is the error, if one occurred.
    """

    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ID of the assistant.
    """

    phone_number_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="phoneNumberId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ID of the phone number.
    """

    customer_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="customerId")] = pydantic.Field(
        default=None
    )
    """
    This is the ID of the customer.
    """

    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = pydantic.Field(
        default=None
    )
    """
    This is the ID of the squad.
    """

    call_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="callId")] = pydantic.Field(
        default=None
    )
    """
    This is the ID of the call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
