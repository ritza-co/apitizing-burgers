"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BurgerCreateTypedDict(TypedDict):
    r"""Fields to create a burger"""

    name: str
    r"""The name of the burger"""
    description: NotRequired[str]
    r"""The description of the burger"""


class BurgerCreate(BaseModel):
    r"""Fields to create a burger"""

    name: str
    r"""The name of the burger"""

    description: Optional[str] = ""
    r"""The description of the burger"""
