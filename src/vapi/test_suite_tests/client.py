# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .types.test_suite_test_controller_find_all_paginated_request_sort_order import (
    TestSuiteTestControllerFindAllPaginatedRequestSortOrder,
)
import datetime as dt
from ..core.request_options import RequestOptions
from ..types.test_suite_tests_paginated_response import TestSuiteTestsPaginatedResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.datetime_utils import serialize_datetime
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.test_suite_test_scorer_ai import TestSuiteTestScorerAi
from ..types.test_suite_test_voice import TestSuiteTestVoice
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestSuiteTestsClient:
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
    ) -> TestSuiteTestsPaginatedResponse:
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
        TestSuiteTestsPaginatedResponse

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
                return typing.cast(
                    TestSuiteTestsPaginatedResponse,
                    construct_type(
                        type_=TestSuiteTestsPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def test_suite_test_controller_create(
        self,
        test_suite_id: str,
        *,
        scorers: typing.Sequence[TestSuiteTestScorerAi],
        script: str,
        num_attempts: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        scorers : typing.Sequence[TestSuiteTestScorerAi]
            These are the scorers used to evaluate the test.

        script : str
            This is the script to be used for the voice test.

        num_attempts : typing.Optional[float]
            This is the number of attempts allowed for the test.

        name : typing.Optional[str]
            This is the name of the test.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test",
            method="POST",
            json={
                "scorers": convert_and_respect_annotation_metadata(
                    object_=scorers, annotation=typing.Sequence[TestSuiteTestScorerAi], direction="write"
                ),
                "script": script,
                "numAttempts": num_attempts,
                "name": name,
                "type": "voice",
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def test_suite_test_controller_find_one(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def test_suite_test_controller_remove(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def test_suite_test_controller_update(
        self,
        test_suite_id: str,
        id: str,
        *,
        scorers: typing.Optional[typing.Sequence[TestSuiteTestScorerAi]] = OMIT,
        name: typing.Optional[str] = OMIT,
        script: typing.Optional[str] = OMIT,
        num_attempts: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        scorers : typing.Optional[typing.Sequence[TestSuiteTestScorerAi]]
            These are the scorers used to evaluate the test.

        name : typing.Optional[str]
            This is the name of the test.

        script : typing.Optional[str]
            This is the script to be used for the voice test.

        num_attempts : typing.Optional[float]
            This is the number of attempts allowed for the test.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "scorers": convert_and_respect_annotation_metadata(
                    object_=scorers, annotation=typing.Sequence[TestSuiteTestScorerAi], direction="write"
                ),
                "name": name,
                "script": script,
                "numAttempts": num_attempts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTestSuiteTestsClient:
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
    ) -> TestSuiteTestsPaginatedResponse:
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
        TestSuiteTestsPaginatedResponse

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
                return typing.cast(
                    TestSuiteTestsPaginatedResponse,
                    construct_type(
                        type_=TestSuiteTestsPaginatedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def test_suite_test_controller_create(
        self,
        test_suite_id: str,
        *,
        scorers: typing.Sequence[TestSuiteTestScorerAi],
        script: str,
        num_attempts: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        scorers : typing.Sequence[TestSuiteTestScorerAi]
            These are the scorers used to evaluate the test.

        script : str
            This is the script to be used for the voice test.

        num_attempts : typing.Optional[float]
            This is the number of attempts allowed for the test.

        name : typing.Optional[str]
            This is the name of the test.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test",
            method="POST",
            json={
                "scorers": convert_and_respect_annotation_metadata(
                    object_=scorers, annotation=typing.Sequence[TestSuiteTestScorerAi], direction="write"
                ),
                "script": script,
                "numAttempts": num_attempts,
                "name": name,
                "type": "voice",
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def test_suite_test_controller_find_one(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def test_suite_test_controller_remove(
        self, test_suite_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def test_suite_test_controller_update(
        self,
        test_suite_id: str,
        id: str,
        *,
        scorers: typing.Optional[typing.Sequence[TestSuiteTestScorerAi]] = OMIT,
        name: typing.Optional[str] = OMIT,
        script: typing.Optional[str] = OMIT,
        num_attempts: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuiteTestVoice:
        """
        Parameters
        ----------
        test_suite_id : str

        id : str

        scorers : typing.Optional[typing.Sequence[TestSuiteTestScorerAi]]
            These are the scorers used to evaluate the test.

        name : typing.Optional[str]
            This is the name of the test.

        script : typing.Optional[str]
            This is the script to be used for the voice test.

        num_attempts : typing.Optional[float]
            This is the number of attempts allowed for the test.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuiteTestVoice

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"test-suite/{jsonable_encoder(test_suite_id)}/test/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "scorers": convert_and_respect_annotation_metadata(
                    object_=scorers, annotation=typing.Sequence[TestSuiteTestScorerAi], direction="write"
                ),
                "name": name,
                "script": script,
                "numAttempts": num_attempts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TestSuiteTestVoice,
                    construct_type(
                        type_=TestSuiteTestVoice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
