# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TestSuiteTestScorerAi(UniversalBaseModel):
    type: typing.Literal["ai"] = pydantic.Field(default="ai")
    """
    This is the type of the scorer, which must be AI.
    """

    rubric: str = pydantic.Field()
    """
    This is the rubric used by the AI scorer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
