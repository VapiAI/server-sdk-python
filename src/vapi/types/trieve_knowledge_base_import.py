# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrieveKnowledgeBaseImport(UncheckedBaseModel):
    type: typing.Literal["import"] = pydantic.Field(default="import")
    """
    This is to import an existing dataset from Trieve.
    """

    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId")] = pydantic.Field()
    """
    This is the `datasetId` of the dataset on your Trieve account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
