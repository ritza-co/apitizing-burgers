"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import orderoutput as shared_orderoutput
from typing import Optional



@dataclasses.dataclass
class CreateOrderResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    order_output: Optional[shared_orderoutput.OrderOutput] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

