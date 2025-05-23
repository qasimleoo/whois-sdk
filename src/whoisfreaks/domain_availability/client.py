# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDomainAvailabilityClient, RawDomainAvailabilityClient
from .types.bulk_domain_availability_response import BulkDomainAvailabilityResponse
from .types.domain_availability_response import DomainAvailabilityResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DomainAvailabilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDomainAvailabilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDomainAvailabilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDomainAvailabilityClient
        """
        return self._raw_client

    def domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain: str,
        sug: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DomainAvailabilityResponse:
        """
        Check availability of a Domain Name

        Parameters
        ----------
        api_key : str

        domain : str

        sug : typing.Optional[bool]

        count : typing.Optional[int]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DomainAvailabilityResponse

        Examples
        --------
        from whoisfreaks import WhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        client.domain_availability.domain_availability_lookup(api_key='YOUR_API_KEY', domain='whoisfreaks.com', sug=True, count=10, )
        """
        _response = self._raw_client.domain_availability_lookup(
            api_key=api_key, domain=domain, sug=sug, count=count, format=format, request_options=request_options
        )
        return _response.data

    def bulk_domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain_names: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkDomainAvailabilityResponse:
        """
        Check availability of multiple Domain Names

        Parameters
        ----------
        api_key : str

        domain_names : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkDomainAvailabilityResponse

        Examples
        --------
        from whoisfreaks import WhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        client.domain_availability.bulk_domain_availability_lookup(api_key='YOUR_API_KEY', domain_names=['whoisfreaks.com', 'jfreaks.com'], )
        """
        _response = self._raw_client.bulk_domain_availability_lookup(
            api_key=api_key, domain_names=domain_names, format=format, request_options=request_options
        )
        return _response.data

    def bulk_domain_availability_lookup_with_custom_tl_ds(
        self,
        *,
        api_key: str,
        domain: str,
        tld: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkDomainAvailabilityResponse:
        """
        Check availability of multiple Domain Names with custom TLDs

        Parameters
        ----------
        api_key : str

        domain : str

        tld : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkDomainAvailabilityResponse

        Examples
        --------
        from whoisfreaks import WhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        client.domain_availability.bulk_domain_availability_lookup_with_custom_tl_ds(api_key='YOUR_API_KEY', domain='whoisfreaks.com', tld=['us', 'pk'], )
        """
        _response = self._raw_client.bulk_domain_availability_lookup_with_custom_tl_ds(
            api_key=api_key, domain=domain, tld=tld, format=format, request_options=request_options
        )
        return _response.data


class AsyncDomainAvailabilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDomainAvailabilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDomainAvailabilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDomainAvailabilityClient
        """
        return self._raw_client

    async def domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain: str,
        sug: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DomainAvailabilityResponse:
        """
        Check availability of a Domain Name

        Parameters
        ----------
        api_key : str

        domain : str

        sug : typing.Optional[bool]

        count : typing.Optional[int]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DomainAvailabilityResponse

        Examples
        --------
        from whoisfreaks import AsyncWhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        import asyncio
        client = AsyncWhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        async def main() -> None:
            await client.domain_availability.domain_availability_lookup(api_key='YOUR_API_KEY', domain='whoisfreaks.com', sug=True, count=10, )
        asyncio.run(main())
        """
        _response = await self._raw_client.domain_availability_lookup(
            api_key=api_key, domain=domain, sug=sug, count=count, format=format, request_options=request_options
        )
        return _response.data

    async def bulk_domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain_names: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkDomainAvailabilityResponse:
        """
        Check availability of multiple Domain Names

        Parameters
        ----------
        api_key : str

        domain_names : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkDomainAvailabilityResponse

        Examples
        --------
        from whoisfreaks import AsyncWhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        import asyncio
        client = AsyncWhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        async def main() -> None:
            await client.domain_availability.bulk_domain_availability_lookup(api_key='YOUR_API_KEY', domain_names=['whoisfreaks.com', 'jfreaks.com'], )
        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_domain_availability_lookup(
            api_key=api_key, domain_names=domain_names, format=format, request_options=request_options
        )
        return _response.data

    async def bulk_domain_availability_lookup_with_custom_tl_ds(
        self,
        *,
        api_key: str,
        domain: str,
        tld: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkDomainAvailabilityResponse:
        """
        Check availability of multiple Domain Names with custom TLDs

        Parameters
        ----------
        api_key : str

        domain : str

        tld : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkDomainAvailabilityResponse

        Examples
        --------
        from whoisfreaks import AsyncWhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        import asyncio
        client = AsyncWhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        async def main() -> None:
            await client.domain_availability.bulk_domain_availability_lookup_with_custom_tl_ds(api_key='YOUR_API_KEY', domain='whoisfreaks.com', tld=['us', 'pk'], )
        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_domain_availability_lookup_with_custom_tl_ds(
            api_key=api_key, domain=domain, tld=tld, format=format, request_options=request_options
        )
        return _response.data
