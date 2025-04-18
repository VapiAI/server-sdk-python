# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .fallback_plan_voices_item import FallbackPlanVoicesItem
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackPlan(UncheckedBaseModel):
    voices: typing.List[FallbackPlanVoicesItem] = pydantic.Field()
    """
    This is the list of voices to fallback to in the event that the primary voice provider fails.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
