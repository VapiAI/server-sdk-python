# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import datetime as dt
from ..core.request_options import RequestOptions
from ..types.squad import Squad
from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.squad_member_dto import SquadMemberDto
from ..types.assistant_overrides import AssistantOverrides
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SquadsClient:
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
    ) -> typing.List[Squad]:
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
        typing.List[Squad]


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.squads.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "squad",
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
                    typing.List[Squad],
                    parse_obj_as(
                        type_=typing.List[Squad],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        members: typing.Sequence[SquadMemberDto],
        name: typing.Optional[str] = OMIT,
        members_overrides: typing.Optional[AssistantOverrides] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Squad:
        """
        Parameters
        ----------
        members : typing.Sequence[SquadMemberDto]
            This is the list of assistants that make up the squad.

            The call will start with the first assistant in the list.

        name : typing.Optional[str]
            This is the name of the squad.

        members_overrides : typing.Optional[AssistantOverrides]
            This can be used to override all the assistants' settings and provide values for their template variables.

            Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        from vapi import SquadMemberDto, Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.squads.create(
            members=[SquadMemberDto()],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "squad",
            method="POST",
            json={
                "name": name,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Sequence[SquadMemberDto], direction="write"
                ),
                "membersOverrides": convert_and_respect_annotation_metadata(
                    object_=members_overrides, annotation=AssistantOverrides, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Squad:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.squads.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"squad/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Squad:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.squads.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"squad/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
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
        members: typing.Sequence[SquadMemberDto],
        name: typing.Optional[str] = OMIT,
        members_overrides: typing.Optional[AssistantOverrides] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Squad:
        """
        Parameters
        ----------
        id : str

        members : typing.Sequence[SquadMemberDto]
            This is the list of assistants that make up the squad.

            The call will start with the first assistant in the list.

        name : typing.Optional[str]
            This is the name of the squad.

        members_overrides : typing.Optional[AssistantOverrides]
            This can be used to override all the assistants' settings and provide values for their template variables.

            Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        from vapi import SquadMemberDto, Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.squads.update(
            id="id",
            members=[SquadMemberDto()],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"squad/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Sequence[SquadMemberDto], direction="write"
                ),
                "membersOverrides": convert_and_respect_annotation_metadata(
                    object_=members_overrides, annotation=AssistantOverrides, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSquadsClient:
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
    ) -> typing.List[Squad]:
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
        typing.List[Squad]


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.squads.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "squad",
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
                    typing.List[Squad],
                    parse_obj_as(
                        type_=typing.List[Squad],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        members: typing.Sequence[SquadMemberDto],
        name: typing.Optional[str] = OMIT,
        members_overrides: typing.Optional[AssistantOverrides] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Squad:
        """
        Parameters
        ----------
        members : typing.Sequence[SquadMemberDto]
            This is the list of assistants that make up the squad.

            The call will start with the first assistant in the list.

        name : typing.Optional[str]
            This is the name of the squad.

        members_overrides : typing.Optional[AssistantOverrides]
            This can be used to override all the assistants' settings and provide values for their template variables.

            Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi, SquadMemberDto

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.squads.create(
                members=[SquadMemberDto()],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "squad",
            method="POST",
            json={
                "name": name,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Sequence[SquadMemberDto], direction="write"
                ),
                "membersOverrides": convert_and_respect_annotation_metadata(
                    object_=members_overrides, annotation=AssistantOverrides, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Squad:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.squads.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"squad/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Squad:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.squads.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"squad/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
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
        members: typing.Sequence[SquadMemberDto],
        name: typing.Optional[str] = OMIT,
        members_overrides: typing.Optional[AssistantOverrides] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Squad:
        """
        Parameters
        ----------
        id : str

        members : typing.Sequence[SquadMemberDto]
            This is the list of assistants that make up the squad.

            The call will start with the first assistant in the list.

        name : typing.Optional[str]
            This is the name of the squad.

        members_overrides : typing.Optional[AssistantOverrides]
            This can be used to override all the assistants' settings and provide values for their template variables.

            Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Squad


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi, SquadMemberDto

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.squads.update(
                id="id",
                members=[SquadMemberDto()],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"squad/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Sequence[SquadMemberDto], direction="write"
                ),
                "membersOverrides": convert_and_respect_annotation_metadata(
                    object_=members_overrides, annotation=AssistantOverrides, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Squad,
                    parse_obj_as(
                        type_=Squad,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
