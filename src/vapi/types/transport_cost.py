# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .transport_cost_provider import TransportCostProvider
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TransportCost(UniversalBaseModel):
    type: typing.Literal["transport"] = pydantic.Field(default="transport")
    """
    This is the type of cost, always 'transport' for this class.
    """

    provider: typing.Optional[TransportCostProvider] = None
    minutes: float = pydantic.Field()
    """
    This is the minutes of `transport` usage. This should match `call.endedAt` - `call.startedAt`.
    """

    cost: float = pydantic.Field()
    """
    This is the cost of the component in USD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
