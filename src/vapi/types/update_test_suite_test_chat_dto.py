# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .test_suite_test_scorer_ai import TestSuiteTestScorerAi
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateTestSuiteTestChatDto(UncheckedBaseModel):
    scorers: typing.Optional[typing.List[TestSuiteTestScorerAi]] = pydantic.Field(default=None)
    """
    These are the scorers used to evaluate the test.
    """

    type: typing.Literal["chat"] = "chat"
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the test.
    """

    script: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the script to be used for the chat test.
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
