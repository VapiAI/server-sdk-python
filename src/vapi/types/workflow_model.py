# This file was auto-generated by Fern from our API Definition.

import typing

from .workflow_anthropic_model import WorkflowAnthropicModel
from .workflow_open_ai_model import WorkflowOpenAiModel

WorkflowModel = typing.Union[WorkflowOpenAiModel, WorkflowAnthropicModel]
