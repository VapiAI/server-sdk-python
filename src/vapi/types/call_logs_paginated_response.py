# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .call_log_privileged import CallLogPrivileged
from .pagination_meta import PaginationMeta
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CallLogsPaginatedResponse(UniversalBaseModel):
    results: typing.List[CallLogPrivileged]
    metadata: PaginationMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
