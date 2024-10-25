# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import datetime as dt
from ..core.request_options import RequestOptions
from .types.blocks_list_response_item import BlocksListResponseItem
from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.blocks_create_request import BlocksCreateRequest
from .types.blocks_create_response import BlocksCreateResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.blocks_get_response import BlocksGetResponse
from ..core.jsonable_encoder import jsonable_encoder
from .types.blocks_delete_response import BlocksDeleteResponse
from .types.update_block_dto_messages_item import UpdateBlockDtoMessagesItem
from ..types.json_schema import JsonSchema
from .types.update_block_dto_tool import UpdateBlockDtoTool
from .types.update_block_dto_steps_item import UpdateBlockDtoStepsItem
from .types.blocks_update_response import BlocksUpdateResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BlocksListResponseItem]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BlocksListResponseItem]


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.blocks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "block",
            method="GET",
            params={
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[BlocksListResponseItem],
                    parse_obj_as(
                        type_=typing.List[BlocksListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: BlocksCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> BlocksCreateResponse:
        """
        Parameters
        ----------
        request : BlocksCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksCreateResponse


        Examples
        --------
        from vapi import CreateConversationBlockDto, Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.blocks.create(
            request=CreateConversationBlockDto(
                instruction="instruction",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "block",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=BlocksCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksCreateResponse,
                    parse_obj_as(
                        type_=BlocksCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BlocksGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksGetResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.blocks.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"block/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksGetResponse,
                    parse_obj_as(
                        type_=BlocksGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BlocksDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksDeleteResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.blocks.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"block/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksDeleteResponse,
                    parse_obj_as(
                        type_=BlocksDeleteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: str,
        *,
        messages: typing.Optional[typing.Sequence[UpdateBlockDtoMessagesItem]] = OMIT,
        input_schema: typing.Optional[JsonSchema] = OMIT,
        output_schema: typing.Optional[JsonSchema] = OMIT,
        tool: typing.Optional[UpdateBlockDtoTool] = OMIT,
        steps: typing.Optional[typing.Sequence[UpdateBlockDtoStepsItem]] = OMIT,
        name: typing.Optional[str] = OMIT,
        instruction: typing.Optional[str] = OMIT,
        tool_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BlocksUpdateResponse:
        """
        Parameters
        ----------
        id : str

        messages : typing.Optional[typing.Sequence[UpdateBlockDtoMessagesItem]]
            These are the pre-configured messages that will be spoken to the user while the block is running.

        input_schema : typing.Optional[JsonSchema]
            This is the input schema for the block. This is the input the block needs to run. It's given to the block as `steps[0].input`

            These are accessible as variables:
            - ({{input.propertyName}}) in context of the block execution (step)
            - ({{stepName.input.propertyName}}) in context of the workflow

        output_schema : typing.Optional[JsonSchema]
            This is the output schema for the block. This is the output the block will return to the workflow (`{{stepName.output}}`).

            These are accessible as variables:
            - ({{output.propertyName}}) in context of the block execution (step)
            - ({{stepName.output.propertyName}}) in context of the workflow (read caveat #1)
            - ({{blockName.output.propertyName}}) in context of the workflow (read caveat #2)

            Caveats:
            1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output.propertyName}} will reference the latest usage of the step.
            2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.

        tool : typing.Optional[UpdateBlockDtoTool]
            This is the tool that the block will call. To use an existing tool, use `toolId`.

        steps : typing.Optional[typing.Sequence[UpdateBlockDtoStepsItem]]
            These are the steps in the workflow.

        name : typing.Optional[str]
            This is the name of the block. This is just for your reference.

        instruction : typing.Optional[str]
            This is the instruction to the model.

            You can reference any variable in the context of the current block execution (step):
            - "{{input.your-property-name}}" for the current step's input
            - "{{your-step-name.output.your-property-name}}" for another step's output (in the same workflow; read caveat #1)
            - "{{your-step-name.input.your-property-name}}" for another step's input (in the same workflow; read caveat #1)
            - "{{your-block-name.output.your-property-name}}" for another block's output (in the same workflow; read caveat #2)
            - "{{your-block-name.input.your-property-name}}" for another block's input (in the same workflow; read caveat #2)
            - "{{workflow.input.your-property-name}}" for the current workflow's input
            - "{{global.your-property-name}}" for the global context

            This can be as simple or as complex as you want it to be.
            - "say hello and ask the user about their day!"
            - "collect the user's first and last name"
            - "user is {{input.firstName}} {{input.lastName}}. their age is {{input.age}}. ask them about their salary and if they might be interested in buying a house. we offer {{input.offer}}"

            Caveats:
            1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output/input.propertyName}} will reference the latest usage of the step.
            2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output/input.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.

        tool_id : typing.Optional[str]
            This is the id of the tool that the block will call. To use a transient tool, use `tool`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksUpdateResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.blocks.update(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"block/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[UpdateBlockDtoMessagesItem], direction="write"
                ),
                "inputSchema": convert_and_respect_annotation_metadata(
                    object_=input_schema, annotation=JsonSchema, direction="write"
                ),
                "outputSchema": convert_and_respect_annotation_metadata(
                    object_=output_schema, annotation=JsonSchema, direction="write"
                ),
                "tool": convert_and_respect_annotation_metadata(
                    object_=tool, annotation=UpdateBlockDtoTool, direction="write"
                ),
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[UpdateBlockDtoStepsItem], direction="write"
                ),
                "name": name,
                "instruction": instruction,
                "toolId": tool_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksUpdateResponse,
                    parse_obj_as(
                        type_=BlocksUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BlocksListResponseItem]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BlocksListResponseItem]


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "block",
            method="GET",
            params={
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[BlocksListResponseItem],
                    parse_obj_as(
                        type_=typing.List[BlocksListResponseItem],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: BlocksCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> BlocksCreateResponse:
        """
        Parameters
        ----------
        request : BlocksCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksCreateResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi, CreateConversationBlockDto

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.create(
                request=CreateConversationBlockDto(
                    instruction="instruction",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "block",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=BlocksCreateRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksCreateResponse,
                    parse_obj_as(
                        type_=BlocksCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BlocksGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksGetResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"block/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksGetResponse,
                    parse_obj_as(
                        type_=BlocksGetResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BlocksDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksDeleteResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"block/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksDeleteResponse,
                    parse_obj_as(
                        type_=BlocksDeleteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: str,
        *,
        messages: typing.Optional[typing.Sequence[UpdateBlockDtoMessagesItem]] = OMIT,
        input_schema: typing.Optional[JsonSchema] = OMIT,
        output_schema: typing.Optional[JsonSchema] = OMIT,
        tool: typing.Optional[UpdateBlockDtoTool] = OMIT,
        steps: typing.Optional[typing.Sequence[UpdateBlockDtoStepsItem]] = OMIT,
        name: typing.Optional[str] = OMIT,
        instruction: typing.Optional[str] = OMIT,
        tool_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BlocksUpdateResponse:
        """
        Parameters
        ----------
        id : str

        messages : typing.Optional[typing.Sequence[UpdateBlockDtoMessagesItem]]
            These are the pre-configured messages that will be spoken to the user while the block is running.

        input_schema : typing.Optional[JsonSchema]
            This is the input schema for the block. This is the input the block needs to run. It's given to the block as `steps[0].input`

            These are accessible as variables:
            - ({{input.propertyName}}) in context of the block execution (step)
            - ({{stepName.input.propertyName}}) in context of the workflow

        output_schema : typing.Optional[JsonSchema]
            This is the output schema for the block. This is the output the block will return to the workflow (`{{stepName.output}}`).

            These are accessible as variables:
            - ({{output.propertyName}}) in context of the block execution (step)
            - ({{stepName.output.propertyName}}) in context of the workflow (read caveat #1)
            - ({{blockName.output.propertyName}}) in context of the workflow (read caveat #2)

            Caveats:
            1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output.propertyName}} will reference the latest usage of the step.
            2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.

        tool : typing.Optional[UpdateBlockDtoTool]
            This is the tool that the block will call. To use an existing tool, use `toolId`.

        steps : typing.Optional[typing.Sequence[UpdateBlockDtoStepsItem]]
            These are the steps in the workflow.

        name : typing.Optional[str]
            This is the name of the block. This is just for your reference.

        instruction : typing.Optional[str]
            This is the instruction to the model.

            You can reference any variable in the context of the current block execution (step):
            - "{{input.your-property-name}}" for the current step's input
            - "{{your-step-name.output.your-property-name}}" for another step's output (in the same workflow; read caveat #1)
            - "{{your-step-name.input.your-property-name}}" for another step's input (in the same workflow; read caveat #1)
            - "{{your-block-name.output.your-property-name}}" for another block's output (in the same workflow; read caveat #2)
            - "{{your-block-name.input.your-property-name}}" for another block's input (in the same workflow; read caveat #2)
            - "{{workflow.input.your-property-name}}" for the current workflow's input
            - "{{global.your-property-name}}" for the global context

            This can be as simple or as complex as you want it to be.
            - "say hello and ask the user about their day!"
            - "collect the user's first and last name"
            - "user is {{input.firstName}} {{input.lastName}}. their age is {{input.age}}. ask them about their salary and if they might be interested in buying a house. we offer {{input.offer}}"

            Caveats:
            1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output/input.propertyName}} will reference the latest usage of the step.
            2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output/input.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.

        tool_id : typing.Optional[str]
            This is the id of the tool that the block will call. To use a transient tool, use `tool`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BlocksUpdateResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.blocks.update(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"block/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[UpdateBlockDtoMessagesItem], direction="write"
                ),
                "inputSchema": convert_and_respect_annotation_metadata(
                    object_=input_schema, annotation=JsonSchema, direction="write"
                ),
                "outputSchema": convert_and_respect_annotation_metadata(
                    object_=output_schema, annotation=JsonSchema, direction="write"
                ),
                "tool": convert_and_respect_annotation_metadata(
                    object_=tool, annotation=UpdateBlockDtoTool, direction="write"
                ),
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[UpdateBlockDtoStepsItem], direction="write"
                ),
                "name": name,
                "instruction": instruction,
                "toolId": tool_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BlocksUpdateResponse,
                    parse_obj_as(
                        type_=BlocksUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
