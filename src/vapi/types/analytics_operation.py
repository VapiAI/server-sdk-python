# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .analytics_operation_operation import AnalyticsOperationOperation
import pydantic
from .analytics_operation_column import AnalyticsOperationColumn
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AnalyticsOperation(UniversalBaseModel):
    operation: AnalyticsOperationOperation = pydantic.Field()
    """
    This is the aggregation operation you want to perform.
    """

    column: AnalyticsOperationColumn = pydantic.Field()
    """
    This is the columns you want to perform the aggregation operation on.
    """

    alias: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the alias for column name returned. Defaults to `${operation}${column}`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow