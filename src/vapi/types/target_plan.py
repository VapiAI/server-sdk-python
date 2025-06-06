# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .assistant_overrides import AssistantOverrides
from .test_suite_phone_number import TestSuitePhoneNumber


class TargetPlan(UncheckedBaseModel):
    phone_number_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="phoneNumberId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the phone number that is being tested.
    During the actual test, it'll be called and the assistant attached to it will pick up and be tested.
    To test an assistant directly, send assistantId instead.
    """

    phone_number: typing_extensions.Annotated[
        typing.Optional[TestSuitePhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This can be any phone number (even not on Vapi).
    During the actual test, it'll be called.
    To test a Vapi number, send phoneNumberId. To test an assistant directly, send assistantId instead.
    """

    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the assistant being tested.
    During the actual test, it'll invoked directly.
    To test the assistant over phone number, send phoneNumberId instead.
    """

    assistant_overrides: typing_extensions.Annotated[
        typing.Optional[AssistantOverrides], FieldMetadata(alias="assistantOverrides")
    ] = pydantic.Field(default=None)
    """
    This is the assistant overrides applied to assistantId before it is tested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
