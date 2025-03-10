# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class KnowledgeBaseResponseDocument(UncheckedBaseModel):
    content: str = pydantic.Field()
    """
    This is the content of the document.
    """

    similarity: float = pydantic.Field()
    """
    This is the similarity score of the document.
    """

    uuid_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uuid")] = pydantic.Field(default=None)
    """
    This is the uuid of the document.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
