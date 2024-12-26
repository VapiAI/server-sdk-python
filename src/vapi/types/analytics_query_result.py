# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from .time_range import TimeRange
from ..core.serialization import FieldMetadata
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AnalyticsQueryResult(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    This is the unique key for the query.
    """

    time_range: typing_extensions.Annotated[TimeRange, FieldMetadata(alias="timeRange")] = pydantic.Field()
    """
    This is the time range for the query.
    """

    result: typing.List[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field()
    """
    This is the result of the query, a list of unique groups with result of their aggregations.
    
    Example:
    "result": [
      { "date": "2023-01-01", "assistantId": "123", "endedReason": "customer-ended-call", "sumDuration": 120, "avgCost": 10.5 },
      { "date": "2023-01-02", "assistantId": "123", "endedReason": "customer-did-not-give-microphone-permission", "sumDuration": 0, "avgCost": 0 },
      // Additional results
    ]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
