# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .update_tool_template_dto_details import UpdateToolTemplateDtoDetails
import typing_extensions
from .update_tool_template_dto_provider_details import UpdateToolTemplateDtoProviderDetails
from ..core.serialization import FieldMetadata
from .tool_template_metadata import ToolTemplateMetadata
from .update_tool_template_dto_visibility import UpdateToolTemplateDtoVisibility
import pydantic
from .update_tool_template_dto_provider import UpdateToolTemplateDtoProvider
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateToolTemplateDto(UncheckedBaseModel):
    details: typing.Optional[UpdateToolTemplateDtoDetails] = None
    provider_details: typing_extensions.Annotated[
        typing.Optional[UpdateToolTemplateDtoProviderDetails], FieldMetadata(alias="providerDetails")
    ] = None
    metadata: typing.Optional[ToolTemplateMetadata] = None
    visibility: typing.Optional[UpdateToolTemplateDtoVisibility] = None
    type: typing.Literal["tool"] = "tool"
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the template. This is just for your own reference.
    """

    provider: typing.Optional[UpdateToolTemplateDtoProvider] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
