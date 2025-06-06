# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.unchecked_base_model import construct_type
from ..types.analytics_query import AnalyticsQuery
from ..types.analytics_query_result import AnalyticsQueryResult

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawAnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, *, queries: typing.Sequence[AnalyticsQuery], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AnalyticsQueryResult]]:
        """
        Parameters
        ----------
        queries : typing.Sequence[AnalyticsQuery]
            This is the list of metric queries you want to perform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AnalyticsQueryResult]]

        """
        _response = self._client_wrapper.httpx_client.request(
            "analytics",
            method="POST",
            json={
                "queries": convert_and_respect_annotation_metadata(
                    object_=queries, annotation=typing.Sequence[AnalyticsQuery], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AnalyticsQueryResult],
                    construct_type(
                        type_=typing.List[AnalyticsQueryResult],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, *, queries: typing.Sequence[AnalyticsQuery], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AnalyticsQueryResult]]:
        """
        Parameters
        ----------
        queries : typing.Sequence[AnalyticsQuery]
            This is the list of metric queries you want to perform.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AnalyticsQueryResult]]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "analytics",
            method="POST",
            json={
                "queries": convert_and_respect_annotation_metadata(
                    object_=queries, annotation=typing.Sequence[AnalyticsQuery], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AnalyticsQueryResult],
                    construct_type(
                        type_=typing.List[AnalyticsQueryResult],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
