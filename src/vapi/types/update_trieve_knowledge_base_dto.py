# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from .trieve_knowledge_base_search_plan import TrieveKnowledgeBaseSearchPlan
from ..core.serialization import FieldMetadata
from .trieve_knowledge_base_import import TrieveKnowledgeBaseImport
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateTrieveKnowledgeBaseDto(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the knowledge base.
    """

    search_plan: typing_extensions.Annotated[
        typing.Optional[TrieveKnowledgeBaseSearchPlan], FieldMetadata(alias="searchPlan")
    ] = pydantic.Field(default=None)
    """
    This is the searching plan used when searching for relevant chunks from the vector store.
    
    You should configure this if you're running into these issues:
    - Too much unnecessary context is being fed as knowledge base context.
    - Not enough relevant context is being fed as knowledge base context.
    """

    create_plan: typing_extensions.Annotated[
        typing.Optional[TrieveKnowledgeBaseImport], FieldMetadata(alias="createPlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan if you want us to create/import a new vector store using Trieve.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
