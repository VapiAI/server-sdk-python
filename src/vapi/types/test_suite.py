# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
import typing
from .tester_plan import TesterPlan
from .target_plan import TargetPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TestSuite(UncheckedBaseModel):
    id: str = pydantic.Field()
    """
    This is the unique identifier for the test suite.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this test suite belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the test suite was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the test suite was last updated.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the test suite.
    """

    phone_number_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="phoneNumberId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the phone number ID associated with this test suite.
    """

    tester_plan: typing_extensions.Annotated[typing.Optional[TesterPlan], FieldMetadata(alias="testerPlan")] = (
        pydantic.Field(default=None)
    )
    """
    Override the default tester plan by providing custom assistant configuration for the test agent.
    
    We recommend only using this if you are confident, as we have already set sensible defaults on the tester plan.
    """

    target_plan: typing_extensions.Annotated[typing.Optional[TargetPlan], FieldMetadata(alias="targetPlan")] = (
        pydantic.Field(default=None)
    )
    """
    These are the configuration for the assistant / phone number that is being tested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
