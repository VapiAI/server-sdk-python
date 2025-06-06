# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .artifact_plan_recording_format import ArtifactPlanRecordingFormat
from .transcript_plan import TranscriptPlan


class ArtifactPlan(UncheckedBaseModel):
    recording_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="recordingEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    This determines whether assistant's calls are recorded. Defaults to true.
    
    Usage:
    - If you don't want to record the calls, set this to false.
    - If you want to record the calls when `assistant.hipaaEnabled` (deprecated) or `assistant.compliancePlan.hipaaEnabled` explicity set this to true and make sure to provide S3 or GCP credentials on the Provider Credentials page in the Dashboard.
    
    You can find the recording at `call.artifact.recordingUrl` and `call.artifact.stereoRecordingUrl` after the call is ended.
    
    @default true
    """

    recording_format: typing_extensions.Annotated[
        typing.Optional[ArtifactPlanRecordingFormat], FieldMetadata(alias="recordingFormat")
    ] = pydantic.Field(default=None)
    """
    This determines the format of the recording. Defaults to `wav;l16`.
    
    @default 'wav;l16'
    """

    video_recording_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="videoRecordingEnabled")
    ] = pydantic.Field(default=None)
    """
    This determines whether the video is recorded during the call. Defaults to false. Only relevant for `webCall` type.
    
    You can find the video recording at `call.artifact.videoRecordingUrl` after the call is ended.
    
    @default false
    """

    pcap_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="pcapEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    This determines whether the SIP packet capture is enabled. Defaults to true. Only relevant for `phone` type calls where phone number's provider is `vapi` or `byo-phone-number`.
    
    You can find the packet capture at `call.artifact.pcapUrl` after the call is ended.
    
    @default true
    """

    pcap_s_3_path_prefix: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pcapS3PathPrefix")] = (
        pydantic.Field(default=None)
    )
    """
    This is the path where the SIP packet capture will be uploaded. This is only used if you have provided S3 or GCP credentials on the Provider Credentials page in the Dashboard.
    
    If credential.s3PathPrefix or credential.bucketPlan.path is set, this will append to it.
    
    Usage:
    - If you want to upload the packet capture to a specific path, set this to the path. Example: `/my-assistant-captures`.
    - If you want to upload the packet capture to the root of the bucket, set this to `/`.
    
    @default '/'
    """

    transcript_plan: typing_extensions.Annotated[
        typing.Optional[TranscriptPlan], FieldMetadata(alias="transcriptPlan")
    ] = pydantic.Field(default=None)
    """
    This is the plan for `call.artifact.transcript`. To disable, set `transcriptPlan.enabled` to false.
    """

    recording_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="recordingPath")] = (
        pydantic.Field(default=None)
    )
    """
    This is the path where the recording will be uploaded. This is only used if you have provided S3 or GCP credentials on the Provider Credentials page in the Dashboard.
    
    If credential.s3PathPrefix or credential.bucketPlan.path is set, this will append to it.
    
    Usage:
    - If you want to upload the recording to a specific path, set this to the path. Example: `/my-assistant-recordings`.
    - If you want to upload the recording to the root of the bucket, set this to `/`.
    
    @default '/'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
