# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from ..core.unchecked_base_model import UncheckedBaseModel
from .artifact_messages_item import ArtifactMessagesItem
from .node_artifact import NodeArtifact
from .open_ai_message import OpenAiMessage
from .recording import Recording


class Artifact(UncheckedBaseModel):
    messages: typing.Optional[typing.List[ArtifactMessagesItem]] = pydantic.Field(default=None)
    """
    These are the messages that were spoken during the call.
    """

    messages_open_ai_formatted: typing_extensions.Annotated[
        typing.Optional[typing.List[OpenAiMessage]], FieldMetadata(alias="messagesOpenAIFormatted")
    ] = pydantic.Field(default=None)
    """
    These are the messages that were spoken during the call, formatted for OpenAI.
    """

    recording_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="recordingUrl")] = (
        pydantic.Field(default=None)
    )
    """
    This is the recording url for the call. To enable, set `assistant.artifactPlan.recordingEnabled`.
    """

    stereo_recording_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stereoRecordingUrl")
    ] = pydantic.Field(default=None)
    """
    This is the stereo recording url for the call. To enable, set `assistant.artifactPlan.recordingEnabled`.
    """

    video_recording_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="videoRecordingUrl")] = (
        pydantic.Field(default=None)
    )
    """
    This is video recording url for the call. To enable, set `assistant.artifactPlan.videoRecordingEnabled`.
    """

    video_recording_start_delay_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="videoRecordingStartDelaySeconds")
    ] = pydantic.Field(default=None)
    """
    This is video recording start delay in ms. To enable, set `assistant.artifactPlan.videoRecordingEnabled`. This can be used to align the playback of the recording with artifact.messages timestamps.
    """

    recording: typing.Optional[Recording] = pydantic.Field(default=None)
    """
    This is the recording url for the call. To enable, set `assistant.artifactPlan.recordingEnabled`.
    """

    transcript: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the transcript of the call. This is derived from `artifact.messages` but provided for convenience.
    """

    pcap_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pcapUrl")] = pydantic.Field(
        default=None
    )
    """
    This is the packet capture url for the call. This is only available for `phone` type calls where phone number's provider is `vapi` or `byo-phone-number`.
    """

    nodes: typing.Optional[typing.List[NodeArtifact]] = pydantic.Field(default=None)
    """
    This is the history of workflow nodes that were executed during the call.
    """

    variables: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    This is the state of variables at the end of the workflow execution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
