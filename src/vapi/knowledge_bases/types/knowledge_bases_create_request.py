# This file was auto-generated by Fern from our API Definition.

import typing

from ...types.create_custom_knowledge_base_dto import CreateCustomKnowledgeBaseDto
from ...types.create_trieve_knowledge_base_dto import CreateTrieveKnowledgeBaseDto

KnowledgeBasesCreateRequest = typing.Union[CreateTrieveKnowledgeBaseDto, CreateCustomKnowledgeBaseDto]
