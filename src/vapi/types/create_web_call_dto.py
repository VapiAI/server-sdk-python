# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .create_assistant_dto import CreateAssistantDto
from .assistant_overrides import AssistantOverrides
from .create_squad_dto import CreateSquadDto
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateWebCallDto(UncheckedBaseModel):
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the assistant that will be used for the call. To use a transient assistant, use `assistant` instead.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that will be used for the call. To use an existing assistant, use `assistantId` instead.
    """

    assistant_overrides: typing_extensions.Annotated[
        typing.Optional[AssistantOverrides], FieldMetadata(alias="assistantOverrides")
    ] = pydantic.Field(default=None)
    """
    These are the overrides for the `assistant` or `assistantId`'s settings and template variables.
    """

    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = pydantic.Field(
        default=None
    )
    """
    This is the squad that will be used for the call. To use a transient squad, use `squad` instead.
    """

    squad: typing.Optional[CreateSquadDto] = pydantic.Field(default=None)
    """
    This is a squad that will be used for the call. To use an existing squad, use `squadId` instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
