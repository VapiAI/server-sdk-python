# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from .trieve_knowledge_base_vector_store_search_plan import TrieveKnowledgeBaseVectorStoreSearchPlan
from ..core.serialization import FieldMetadata
from .trieve_knowledge_base_vector_store_create_plan import TrieveKnowledgeBaseVectorStoreCreatePlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrieveKnowledgeBase(UniversalBaseModel):
    provider: typing.Literal["trieve"] = "trieve"
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the knowledge base.
    """

    vector_store_search_plan: typing_extensions.Annotated[
        TrieveKnowledgeBaseVectorStoreSearchPlan, FieldMetadata(alias="vectorStoreSearchPlan")
    ] = pydantic.Field()
    """
    This is the plan on how to search the vector store while a call is going on.
    """

    vector_store_create_plan: typing_extensions.Annotated[
        typing.Optional[TrieveKnowledgeBaseVectorStoreCreatePlan], FieldMetadata(alias="vectorStoreCreatePlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan if you want us to create a new vector store on your behalf. To use an existing vector store from your account, use `vectoreStoreProviderId`
    """

    vector_store_provider_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="vectorStoreProviderId")
    ] = pydantic.Field(default=None)
    """
    This is an vector store that you already have on your account with the provider. To create a new vector store, use vectorStoreCreatePlan.
    
    Usage:
    - To bring your own vector store from Trieve, go to https://trieve.ai
    - Create a dataset, and use the datasetId here.
    """

    id: str = pydantic.Field()
    """
    This is the id of the knowledge base.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the org id of the knowledge base.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
