# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.unchecked_base_model import construct_type
from ..types.test_suite_tests_paginated_response import TestSuiteTestsPaginatedResponse
from .types.test_suite_test_controller_create_request import TestSuiteTestControllerCreateRequest
from .types.test_suite_test_controller_create_response import TestSuiteTestControllerCreateResponse
from .types.test_suite_test_controller_find_all_paginated_request_sort_order import (
    TestSuiteTestControllerFindAllPaginatedRequestSortOrder,
)
from .types.test_suite_test_controller_find_one_response import TestSuiteTestControllerFindOneResponse
from .types.test_suite_test_controller_remove_response import TestSuiteTestControllerRemoveResponse
from .types.test_suite_test_controller_update_request import TestSuiteTestControllerUpdateRequest
from .types.test_suite_test_controller_update_response import TestSuiteTestControllerUpdateResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawTestSuiteTestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def test_suite_test_controller_find_all_paginated(
        self,
        test_suite_id: str,
        *,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[TestSuiteTestControllerFindAllPaginatedRequestSortOrder] = None,
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
    ) -> HttpResponse[TestSuiteTestsPaginatedResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[TestSuiteTestControllerFindAllPaginatedRequestSortOrder]
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
        HttpResponse[TestSuiteTestsPaginatedResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test",
            method="GET",
            params={
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
                _data = typing.cast(
                    TestSuiteTestsPaginatedResponse,
                    construct_type(
                        type_=TestSuiteTestsPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def test_suite_test_controller_create(
        self,
        test_suite_id: str,
        *,
        request: TestSuiteTestControllerCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TestSuiteTestControllerCreateResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        request : TestSuiteTestControllerCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestSuiteTestControllerCreateResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TestSuiteTestControllerCreateRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerCreateResponse,
                    construct_type(
                        type_=TestSuiteTestControllerCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def test_suite_test_controller_find_one(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestSuiteTestControllerFindOneResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestSuiteTestControllerFindOneResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerFindOneResponse,
                    construct_type(
                        type_=TestSuiteTestControllerFindOneResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def test_suite_test_controller_remove(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestSuiteTestControllerRemoveResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestSuiteTestControllerRemoveResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerRemoveResponse,
                    construct_type(
                        type_=TestSuiteTestControllerRemoveResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def test_suite_test_controller_update(
        self,
        test_suite_id: str,
        id: str,
        *,
        request: TestSuiteTestControllerUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TestSuiteTestControllerUpdateResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request : TestSuiteTestControllerUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestSuiteTestControllerUpdateResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TestSuiteTestControllerUpdateRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerUpdateResponse,
                    construct_type(
                        type_=TestSuiteTestControllerUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTestSuiteTestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def test_suite_test_controller_find_all_paginated(
        self,
        test_suite_id: str,
        *,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[TestSuiteTestControllerFindAllPaginatedRequestSortOrder] = None,
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
    ) -> AsyncHttpResponse[TestSuiteTestsPaginatedResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[TestSuiteTestControllerFindAllPaginatedRequestSortOrder]
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
        AsyncHttpResponse[TestSuiteTestsPaginatedResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test",
            method="GET",
            params={
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
                _data = typing.cast(
                    TestSuiteTestsPaginatedResponse,
                    construct_type(
                        type_=TestSuiteTestsPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def test_suite_test_controller_create(
        self,
        test_suite_id: str,
        *,
        request: TestSuiteTestControllerCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TestSuiteTestControllerCreateResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        request : TestSuiteTestControllerCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestSuiteTestControllerCreateResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TestSuiteTestControllerCreateRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerCreateResponse,
                    construct_type(
                        type_=TestSuiteTestControllerCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def test_suite_test_controller_find_one(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestSuiteTestControllerFindOneResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestSuiteTestControllerFindOneResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerFindOneResponse,
                    construct_type(
                        type_=TestSuiteTestControllerFindOneResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def test_suite_test_controller_remove(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestSuiteTestControllerRemoveResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestSuiteTestControllerRemoveResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerRemoveResponse,
                    construct_type(
                        type_=TestSuiteTestControllerRemoveResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def test_suite_test_controller_update(
        self,
        test_suite_id: str,
        id: str,
        *,
        request: TestSuiteTestControllerUpdateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TestSuiteTestControllerUpdateResponse]:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request : TestSuiteTestControllerUpdateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestSuiteTestControllerUpdateResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=TestSuiteTestControllerUpdateRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestSuiteTestControllerUpdateResponse,
                    construct_type(
                        type_=TestSuiteTestControllerUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
