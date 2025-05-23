# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dns_record import DnsRecord


class DnsLiveResponse(UniversalBaseModel):
    query_time: typing.Optional[str] = None
    domain_name: typing.Optional[str] = None
    ip_address: typing.Optional[str] = None
    dns_types: typing.Optional[typing.Dict[str, int]] = None
    dns_records: typing.Optional[typing.List[DnsRecord]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
