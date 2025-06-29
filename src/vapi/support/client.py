# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.support_ticket_response import SupportTicketResponse
from .raw_client import AsyncRawSupportClient, RawSupportClient
from .types.create_support_ticket_dto_bug_subcategory import CreateSupportTicketDtoBugSubcategory
from .types.create_support_ticket_dto_category import CreateSupportTicketDtoCategory

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SupportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSupportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSupportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSupportClient
        """
        return self._raw_client

    def support_controller_create_ticket(
        self,
        *,
        category: CreateSupportTicketDtoCategory,
        subject: str,
        message: str,
        bug_subcategory: typing.Optional[CreateSupportTicketDtoBugSubcategory] = OMIT,
        call_details: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SupportTicketResponse:
        """
        Parameters
        ----------
        category : CreateSupportTicketDtoCategory
            The category of the support request

        subject : str
            The subject/title of the support request

        message : str
            Detailed description of the issue or request

        bug_subcategory : typing.Optional[CreateSupportTicketDtoBugSubcategory]
            The subcategory for bug reports

        call_details : typing.Optional[str]
            Call IDs and recording URLs if applicable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SupportTicketResponse


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.support.support_controller_create_ticket(
            category="bug-report",
            subject="subject",
            message="message",
        )
        """
        _response = self._raw_client.support_controller_create_ticket(
            category=category,
            subject=subject,
            message=message,
            bug_subcategory=bug_subcategory,
            call_details=call_details,
            request_options=request_options,
        )
        return _response.data


class AsyncSupportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSupportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSupportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSupportClient
        """
        return self._raw_client

    async def support_controller_create_ticket(
        self,
        *,
        category: CreateSupportTicketDtoCategory,
        subject: str,
        message: str,
        bug_subcategory: typing.Optional[CreateSupportTicketDtoBugSubcategory] = OMIT,
        call_details: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SupportTicketResponse:
        """
        Parameters
        ----------
        category : CreateSupportTicketDtoCategory
            The category of the support request

        subject : str
            The subject/title of the support request

        message : str
            Detailed description of the issue or request

        bug_subcategory : typing.Optional[CreateSupportTicketDtoBugSubcategory]
            The subcategory for bug reports

        call_details : typing.Optional[str]
            Call IDs and recording URLs if applicable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SupportTicketResponse


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.support.support_controller_create_ticket(
                category="bug-report",
                subject="subject",
                message="message",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.support_controller_create_ticket(
            category=category,
            subject=subject,
            message=message,
            bug_subcategory=bug_subcategory,
            call_details=call_details,
            request_options=request_options,
        )
        return _response.data
