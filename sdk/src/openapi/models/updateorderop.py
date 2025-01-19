"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .orderupdate import OrderUpdate, OrderUpdateTypedDict
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class UpdateOrderRequestTypedDict(TypedDict):
    order_update: OrderUpdateTypedDict
    order_id: int


class UpdateOrderRequest(BaseModel):
    order_update: Annotated[
        OrderUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    order_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
