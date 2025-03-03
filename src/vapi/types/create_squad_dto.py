# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing
import pydantic
from .squad_member_dto import SquadMemberDto
import typing_extensions
from .assistant_overrides import AssistantOverrides
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class CreateSquadDto(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the squad.
    """

    members: typing.List[SquadMemberDto] = pydantic.Field()
    """
    This is the list of assistants that make up the squad.
    
    The call will start with the first assistant in the list.
    """

    members_overrides: typing_extensions.Annotated[
        typing.Optional[AssistantOverrides], FieldMetadata(alias="membersOverrides")
    ] = pydantic.Field(default=None)
    """
    This can be used to override all the assistants' settings and provide values for their template variables.
    
    Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CallbackStep, CreateSquadDto=CreateSquadDto)
update_forward_refs(CreateWorkflowBlockDto, CreateSquadDto=CreateSquadDto)
update_forward_refs(HandoffStep, CreateSquadDto=CreateSquadDto)
