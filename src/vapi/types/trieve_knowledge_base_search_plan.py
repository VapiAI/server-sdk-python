# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .trieve_knowledge_base_search_plan_search_type import TrieveKnowledgeBaseSearchPlanSearchType


class TrieveKnowledgeBaseSearchPlan(UncheckedBaseModel):
    top_k: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="topK")] = pydantic.Field(
        default=None
    )
    """
    Specifies the number of top chunks to return. This corresponds to the `page_size` parameter in Trieve.
    """

    remove_stop_words: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="removeStopWords")] = (
        pydantic.Field(default=None)
    )
    """
    If true, stop words (specified in server/src/stop-words.txt in the git repo) will be removed. This will preserve queries that are entirely stop words.
    """

    score_threshold: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="scoreThreshold")] = (
        pydantic.Field(default=None)
    )
    """
    This is the score threshold to filter out chunks with a score below the threshold for cosine distance metric. For Manhattan Distance, Euclidean Distance, and Dot Product, it will filter out scores above the threshold distance. This threshold applies before weight and bias modifications. If not specified, this defaults to no threshold. A threshold of 0 will default to no threshold.
    """

    search_type: typing_extensions.Annotated[
        TrieveKnowledgeBaseSearchPlanSearchType, FieldMetadata(alias="searchType")
    ] = pydantic.Field()
    """
    This is the search method used when searching for relevant chunks from the vector store.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
