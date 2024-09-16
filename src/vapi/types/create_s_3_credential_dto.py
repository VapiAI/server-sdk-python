# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateS3CredentialDto(UniversalBaseModel):
    provider: typing.Literal["s3"] = pydantic.Field(default="s3")
    """
    Credential provider. Only allowed value is s3
    """

    aws_access_key_id: typing_extensions.Annotated[str, FieldMetadata(alias="awsAccessKeyId")] = pydantic.Field()
    """
    AWS access key ID.
    """

    aws_secret_access_key: typing_extensions.Annotated[str, FieldMetadata(alias="awsSecretAccessKey")] = (
        pydantic.Field()
    )
    """
    AWS access key secret. This is not returned in the API.
    """

    region: str = pydantic.Field()
    """
    AWS region in which the S3 bucket is located.
    """

    s_3_bucket_name: typing_extensions.Annotated[str, FieldMetadata(alias="s3BucketName")] = pydantic.Field()
    """
    AWS S3 bucket name.
    """

    s_3_path_prefix: typing_extensions.Annotated[str, FieldMetadata(alias="s3PathPrefix")] = pydantic.Field()
    """
    The path prefix for the uploaded recording. Ex. "recordings/"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow