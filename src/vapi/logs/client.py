# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawLogsClient
import typing
from .types.logs_get_request_type import LogsGetRequestType
from .types.logs_get_request_sort_order import LogsGetRequestSortOrder
import datetime as dt
from ..core.request_options import RequestOptions
from ..core.pagination import SyncPager
from ..types.log import Log
from ..core.datetime_utils import serialize_datetime
from ..types.logs_paginated_response import LogsPaginatedResponse
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.logging_controller_logs_delete_query_request_type import LoggingControllerLogsDeleteQueryRequestType
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawLogsClient
from ..core.pagination import AsyncPager


class LogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLogsClient
        """
        return self._raw_client

    def get(
        self,
        *,
        type: typing.Optional[LogsGetRequestType] = None,
        webhook_type: typing.Optional[str] = None,
        assistant_id: typing.Optional[str] = None,
        phone_number_id: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        squad_id: typing.Optional[str] = None,
        call_id: typing.Optional[str] = None,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[LogsGetRequestSortOrder] = None,
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
    ) -> SyncPager[Log]:
        """
        Parameters
        ----------
        type : typing.Optional[LogsGetRequestType]
            This is the type of the log.

        webhook_type : typing.Optional[str]
            This is the type of the webhook, given the log is from a webhook.

        assistant_id : typing.Optional[str]
            This is the ID of the assistant.

        phone_number_id : typing.Optional[str]
            This is the ID of the phone number.

        customer_id : typing.Optional[str]
            This is the ID of the customer.

        squad_id : typing.Optional[str]
            This is the ID of the squad.

        call_id : typing.Optional[str]
            This is the ID of the call.

        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[LogsGetRequestSortOrder]
            This is the sort order for pagination. Defaults to 'DESC'.

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
        SyncPager[Log]

        """
        page = page if page is not None else 1
        _response = self._raw_client._client_wrapper.httpx_client.request(
            "logs",
            method="GET",
            params={
                "type": type,
                "webhookType": webhook_type,
                "assistantId": assistant_id,
                "phoneNumberId": phone_number_id,
                "customerId": customer_id,
                "squadId": squad_id,
                "callId": call_id,
                "page": page,
                "sortOrder": sort_order,
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
                _parsed_response = typing.cast(
                    LogsPaginatedResponse,
                    construct_type(
                        type_=LogsPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = True
                _get_next = lambda: self.get(
                    type=type,
                    webhook_type=webhook_type,
                    assistant_id=assistant_id,
                    phone_number_id=phone_number_id,
                    customer_id=customer_id,
                    squad_id=squad_id,
                    call_id=call_id,
                    page=page + 1,
                    sort_order=sort_order,
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
                _items = _parsed_response.results
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def logging_controller_logs_delete_query(
        self,
        *,
        type: typing.Optional[LoggingControllerLogsDeleteQueryRequestType] = None,
        assistant_id: typing.Optional[str] = None,
        phone_number_id: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        squad_id: typing.Optional[str] = None,
        call_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        type : typing.Optional[LoggingControllerLogsDeleteQueryRequestType]
            This is the type of the log.

        assistant_id : typing.Optional[str]

        phone_number_id : typing.Optional[str]
            This is the ID of the phone number.

        customer_id : typing.Optional[str]
            This is the ID of the customer.

        squad_id : typing.Optional[str]
            This is the ID of the squad.

        call_id : typing.Optional[str]
            This is the ID of the call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        response = self._raw_client.logging_controller_logs_delete_query(
            type=type,
            assistant_id=assistant_id,
            phone_number_id=phone_number_id,
            customer_id=customer_id,
            squad_id=squad_id,
            call_id=call_id,
            request_options=request_options,
        )
        return response.data


class AsyncLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLogsClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        type: typing.Optional[LogsGetRequestType] = None,
        webhook_type: typing.Optional[str] = None,
        assistant_id: typing.Optional[str] = None,
        phone_number_id: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        squad_id: typing.Optional[str] = None,
        call_id: typing.Optional[str] = None,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[LogsGetRequestSortOrder] = None,
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
    ) -> AsyncPager[Log]:
        """
        Parameters
        ----------
        type : typing.Optional[LogsGetRequestType]
            This is the type of the log.

        webhook_type : typing.Optional[str]
            This is the type of the webhook, given the log is from a webhook.

        assistant_id : typing.Optional[str]
            This is the ID of the assistant.

        phone_number_id : typing.Optional[str]
            This is the ID of the phone number.

        customer_id : typing.Optional[str]
            This is the ID of the customer.

        squad_id : typing.Optional[str]
            This is the ID of the squad.

        call_id : typing.Optional[str]
            This is the ID of the call.

        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[LogsGetRequestSortOrder]
            This is the sort order for pagination. Defaults to 'DESC'.

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
        AsyncPager[Log]

        """
        page = page if page is not None else 1
        _response = await self._raw_client._client_wrapper.httpx_client.request(
            "logs",
            method="GET",
            params={
                "type": type,
                "webhookType": webhook_type,
                "assistantId": assistant_id,
                "phoneNumberId": phone_number_id,
                "customerId": customer_id,
                "squadId": squad_id,
                "callId": call_id,
                "page": page,
                "sortOrder": sort_order,
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
                _parsed_response = typing.cast(
                    LogsPaginatedResponse,
                    construct_type(
                        type_=LogsPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = True
                _get_next = lambda: self.get(
                    type=type,
                    webhook_type=webhook_type,
                    assistant_id=assistant_id,
                    phone_number_id=phone_number_id,
                    customer_id=customer_id,
                    squad_id=squad_id,
                    call_id=call_id,
                    page=page + 1,
                    sort_order=sort_order,
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
                _items = _parsed_response.results
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def logging_controller_logs_delete_query(
        self,
        *,
        type: typing.Optional[LoggingControllerLogsDeleteQueryRequestType] = None,
        assistant_id: typing.Optional[str] = None,
        phone_number_id: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        squad_id: typing.Optional[str] = None,
        call_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        type : typing.Optional[LoggingControllerLogsDeleteQueryRequestType]
            This is the type of the log.

        assistant_id : typing.Optional[str]

        phone_number_id : typing.Optional[str]
            This is the ID of the phone number.

        customer_id : typing.Optional[str]
            This is the ID of the customer.

        squad_id : typing.Optional[str]
            This is the ID of the squad.

        call_id : typing.Optional[str]
            This is the ID of the call.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        response = await self._raw_client.logging_controller_logs_delete_query(
            type=type,
            assistant_id=assistant_id,
            phone_number_id=phone_number_id,
            customer_id=customer_id,
            squad_id=squad_id,
            call_id=call_id,
            request_options=request_options,
        )
        return response.data
