# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.target_plan import TargetPlan
from ..types.test_suite import TestSuite
from ..types.test_suites_paginated_response import TestSuitesPaginatedResponse
from ..types.tester_plan import TesterPlan
from .raw_client import AsyncRawTestSuitesClient, RawTestSuitesClient
from .types.test_suite_controller_find_all_paginated_request_sort_order import (
    TestSuiteControllerFindAllPaginatedRequestSortOrder,
)

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestSuitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTestSuitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTestSuitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTestSuitesClient
        """
        return self._raw_client

    def test_suite_controller_find_all_paginated(
        self,
        *,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[TestSuiteControllerFindAllPaginatedRequestSortOrder] = None,
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
    ) -> TestSuitesPaginatedResponse:
        """
        Parameters
        ----------
        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[TestSuiteControllerFindAllPaginatedRequestSortOrder]
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
        TestSuitesPaginatedResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.test_suites.test_suite_controller_find_all_paginated()
        """
        _response = self._raw_client.test_suite_controller_find_all_paginated(
            page=page,
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
        return _response.data

    def test_suite_controller_create(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[str] = OMIT,
        tester_plan: typing.Optional[TesterPlan] = OMIT,
        target_plan: typing.Optional[TargetPlan] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuite:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            This is the name of the test suite.

        phone_number_id : typing.Optional[str]
            This is the phone number ID associated with this test suite.

        tester_plan : typing.Optional[TesterPlan]
            Override the default tester plan by providing custom assistant configuration for the test agent.

            We recommend only using this if you are confident, as we have already set sensible defaults on the tester plan.

        target_plan : typing.Optional[TargetPlan]
            These are the configuration for the assistant / phone number that is being tested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.test_suites.test_suite_controller_create()
        """
        _response = self._raw_client.test_suite_controller_create(
            name=name,
            phone_number_id=phone_number_id,
            tester_plan=tester_plan,
            target_plan=target_plan,
            request_options=request_options,
        )
        return _response.data

    def test_suite_controller_find_one(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuite:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.test_suites.test_suite_controller_find_one(
            id="id",
        )
        """
        _response = self._raw_client.test_suite_controller_find_one(id, request_options=request_options)
        return _response.data

    def test_suite_controller_remove(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuite:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.test_suites.test_suite_controller_remove(
            id="id",
        )
        """
        _response = self._raw_client.test_suite_controller_remove(id, request_options=request_options)
        return _response.data

    def test_suite_controller_update(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[str] = OMIT,
        tester_plan: typing.Optional[TesterPlan] = OMIT,
        target_plan: typing.Optional[TargetPlan] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuite:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]
            This is the name of the test suite.

        phone_number_id : typing.Optional[str]
            This is the phone number ID associated with this test suite.

        tester_plan : typing.Optional[TesterPlan]
            Override the default tester plan by providing custom assistant configuration for the test agent.

            We recommend only using this if you are confident, as we have already set sensible defaults on the tester plan.

        target_plan : typing.Optional[TargetPlan]
            These are the configuration for the assistant / phone number that is being tested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.test_suites.test_suite_controller_update(
            id="id",
        )
        """
        _response = self._raw_client.test_suite_controller_update(
            id,
            name=name,
            phone_number_id=phone_number_id,
            tester_plan=tester_plan,
            target_plan=target_plan,
            request_options=request_options,
        )
        return _response.data


class AsyncTestSuitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTestSuitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTestSuitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTestSuitesClient
        """
        return self._raw_client

    async def test_suite_controller_find_all_paginated(
        self,
        *,
        page: typing.Optional[float] = None,
        sort_order: typing.Optional[TestSuiteControllerFindAllPaginatedRequestSortOrder] = None,
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
    ) -> TestSuitesPaginatedResponse:
        """
        Parameters
        ----------
        page : typing.Optional[float]
            This is the page number to return. Defaults to 1.

        sort_order : typing.Optional[TestSuiteControllerFindAllPaginatedRequestSortOrder]
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
        TestSuitesPaginatedResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test_suites.test_suite_controller_find_all_paginated()


        asyncio.run(main())
        """
        _response = await self._raw_client.test_suite_controller_find_all_paginated(
            page=page,
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
        return _response.data

    async def test_suite_controller_create(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[str] = OMIT,
        tester_plan: typing.Optional[TesterPlan] = OMIT,
        target_plan: typing.Optional[TargetPlan] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuite:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            This is the name of the test suite.

        phone_number_id : typing.Optional[str]
            This is the phone number ID associated with this test suite.

        tester_plan : typing.Optional[TesterPlan]
            Override the default tester plan by providing custom assistant configuration for the test agent.

            We recommend only using this if you are confident, as we have already set sensible defaults on the tester plan.

        target_plan : typing.Optional[TargetPlan]
            These are the configuration for the assistant / phone number that is being tested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test_suites.test_suite_controller_create()


        asyncio.run(main())
        """
        _response = await self._raw_client.test_suite_controller_create(
            name=name,
            phone_number_id=phone_number_id,
            tester_plan=tester_plan,
            target_plan=target_plan,
            request_options=request_options,
        )
        return _response.data

    async def test_suite_controller_find_one(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuite:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test_suites.test_suite_controller_find_one(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_suite_controller_find_one(id, request_options=request_options)
        return _response.data

    async def test_suite_controller_remove(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TestSuite:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test_suites.test_suite_controller_remove(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_suite_controller_remove(id, request_options=request_options)
        return _response.data

    async def test_suite_controller_update(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        phone_number_id: typing.Optional[str] = OMIT,
        tester_plan: typing.Optional[TesterPlan] = OMIT,
        target_plan: typing.Optional[TargetPlan] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSuite:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]
            This is the name of the test suite.

        phone_number_id : typing.Optional[str]
            This is the phone number ID associated with this test suite.

        tester_plan : typing.Optional[TesterPlan]
            Override the default tester plan by providing custom assistant configuration for the test agent.

            We recommend only using this if you are confident, as we have already set sensible defaults on the tester plan.

        target_plan : typing.Optional[TargetPlan]
            These are the configuration for the assistant / phone number that is being tested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSuite


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.test_suites.test_suite_controller_update(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_suite_controller_update(
            id,
            name=name,
            phone_number_id=phone_number_id,
            tester_plan=tester_plan,
            target_plan=target_plan,
            request_options=request_options,
        )
        return _response.data
