# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .knowledge_base_response_document import KnowledgeBaseResponseDocument
import pydantic
from .custom_message import CustomMessage
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ServerMessageResponseKnowledgeBaseRequest(UniversalBaseModel):
    documents: typing.Optional[typing.List[KnowledgeBaseResponseDocument]] = pydantic.Field(default=None)
    """
    This is the list of documents that will be sent to the model alongside the `messages` to generate a response.
    """

    message: typing.Optional[CustomMessage] = pydantic.Field(default=None)
    """
    This can be used to skip the model output generation and speak a custom message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
