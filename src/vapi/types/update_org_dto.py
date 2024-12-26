# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .update_org_dto_channel import UpdateOrgDtoChannel
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateOrgDto(UniversalBaseModel):
    hipaa_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="hipaaEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    When this is enabled, no logs, recordings, or transcriptions will be stored. At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults to false.
    When HIPAA is enabled, only OpenAI/Custom LLM or Azure Providers will be available for LLM and Voice respectively.
    This is due to the compliance requirements of HIPAA. Other providers may not meet these requirements.
    """

    subscription_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="subscriptionId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ID of the subscription the org belongs to.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the org. This is just for your own reference.
    """

    channel: typing.Optional[UpdateOrgDtoChannel] = pydantic.Field(default=None)
    """
    This is the channel of the org. There is the cluster the API traffic for the org will be directed.
    """

    billing_limit: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="billingLimit")] = (
        pydantic.Field(default=None)
    )
    """
    This is the monthly billing limit for the org. To go beyond $1000/mo, please contact us at support@vapi.ai.
    """

    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = pydantic.Field(
        default=None
    )
    """
    This is the URL Vapi will communicate with via HTTP GET and POST Requests. This is used for retrieving context, function calling, and end-of-call reports.
    
    All requests will be sent with the call object among other things relevant to that message. You can find more details in the Server URL documentation.
    """

    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = (
        pydantic.Field(default=None)
    )
    """
    This is the secret you can set that Vapi will send with every request to your server. Will be sent as a header called x-vapi-secret.
    """

    concurrency_limit: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="concurrencyLimit")] = (
        pydantic.Field(default=None)
    )
    """
    This is the concurrency limit for the org. This is the maximum number of calls that can be active at any given time. To go beyond 10, please contact us at support@vapi.ai.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
