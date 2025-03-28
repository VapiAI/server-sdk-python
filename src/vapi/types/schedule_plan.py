# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import datetime as dt
from ..core.serialization import FieldMetadata
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SchedulePlan(UncheckedBaseModel):
    earliest_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="earliestAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of the earliest time the call can be scheduled.
    """

    latest_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="latestAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ISO 8601 date-time string of the latest time the call can be scheduled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
