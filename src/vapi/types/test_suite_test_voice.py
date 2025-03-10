# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .test_suite_test_scorer_ai import TestSuiteTestScorerAi
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TestSuiteTestVoice(UncheckedBaseModel):
    scorers: typing.List[TestSuiteTestScorerAi] = pydantic.Field()
    """
    These are the scorers used to evaluate the test.
    """

    type: typing.Literal["voice"] = "voice"
    id: str = pydantic.Field()
    """
    This is the unique identifier for the test.
    """

    test_suite_id: typing_extensions.Annotated[str, FieldMetadata(alias="testSuiteId")] = pydantic.Field()
    """
    This is the unique identifier for the test suite this test belongs to.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the organization this test belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the test was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the test was last updated.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the test.
    """

    script: str = pydantic.Field()
    """
    This is the script to be used for the voice test.
    """

    num_attempts: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="numAttempts")] = (
        pydantic.Field(default=None)
    )
    """
    This is the number of attempts allowed for the test.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
