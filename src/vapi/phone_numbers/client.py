# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawPhoneNumbersClient
import datetime as dt
from ..core.request_options import RequestOptions
from .types.phone_numbers_list_response_item import PhoneNumbersListResponseItem
from .types.phone_numbers_create_request import PhoneNumbersCreateRequest
from .types.phone_numbers_create_response import PhoneNumbersCreateResponse
from .types.phone_numbers_get_response import PhoneNumbersGetResponse
from .types.phone_numbers_delete_response import PhoneNumbersDeleteResponse
from .types.phone_numbers_update_request import PhoneNumbersUpdateRequest
from .types.phone_numbers_update_response import PhoneNumbersUpdateResponse
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawPhoneNumbersClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PhoneNumbersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPhoneNumbersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPhoneNumbersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPhoneNumbersClient
        """
        return self._raw_client

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
    ) -> typing.List[PhoneNumbersListResponseItem]:
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
        typing.List[PhoneNumbersListResponseItem]

        """
        response = self._raw_client.list(
            limit=limit,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            created_at_ge=created_at_ge,
            created_at_le=created_at_le,
            updated_at_gt=updated_at_gt,
            updated_at_lt=updated_at_lt,
            updated_at_ge=updated_at_ge,
            updated_at_le=updated_at_le,
            request_options=request_options,
        )
        return response.data

    def create(
        self, *, request: PhoneNumbersCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersCreateResponse:
        """
        Parameters
        ----------
        request : PhoneNumbersCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersCreateResponse

        """
        response = self._raw_client.create(request=request, request_options=request_options)
        return response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneNumbersGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersGetResponse

        """
        response = self._raw_client.get(id, request_options=request_options)
        return response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneNumbersDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersDeleteResponse

        """
        response = self._raw_client.delete(id, request_options=request_options)
        return response.data

    def update(
        self, id: str, *, request: PhoneNumbersUpdateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersUpdateResponse:
        """
        Parameters
        ----------
        id : str

        request : PhoneNumbersUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersUpdateResponse

        """
        response = self._raw_client.update(id, request=request, request_options=request_options)
        return response.data


class AsyncPhoneNumbersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPhoneNumbersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPhoneNumbersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPhoneNumbersClient
        """
        return self._raw_client

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
    ) -> typing.List[PhoneNumbersListResponseItem]:
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
        typing.List[PhoneNumbersListResponseItem]

        """
        response = await self._raw_client.list(
            limit=limit,
            created_at_gt=created_at_gt,
            created_at_lt=created_at_lt,
            created_at_ge=created_at_ge,
            created_at_le=created_at_le,
            updated_at_gt=updated_at_gt,
            updated_at_lt=updated_at_lt,
            updated_at_ge=updated_at_ge,
            updated_at_le=updated_at_le,
            request_options=request_options,
        )
        return response.data

    async def create(
        self, *, request: PhoneNumbersCreateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersCreateResponse:
        """
        Parameters
        ----------
        request : PhoneNumbersCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersCreateResponse

        """
        response = await self._raw_client.create(request=request, request_options=request_options)
        return response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PhoneNumbersGetResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersGetResponse

        """
        response = await self._raw_client.get(id, request_options=request_options)
        return response.data

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersDeleteResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersDeleteResponse

        """
        response = await self._raw_client.delete(id, request_options=request_options)
        return response.data

    async def update(
        self, id: str, *, request: PhoneNumbersUpdateRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumbersUpdateResponse:
        """
        Parameters
        ----------
        id : str

        request : PhoneNumbersUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersUpdateResponse

        """
        response = await self._raw_client.update(id, request=request, request_options=request_options)
        return response.data
