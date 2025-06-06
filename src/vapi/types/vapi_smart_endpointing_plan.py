# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .vapi_smart_endpointing_plan_provider import VapiSmartEndpointingPlanProvider


class VapiSmartEndpointingPlan(UncheckedBaseModel):
    provider: VapiSmartEndpointingPlanProvider = pydantic.Field()
    """
    This is the provider for the smart endpointing plan.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
