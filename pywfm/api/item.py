from typing import List
from ..common.base import BaseRequest
from ..models.item import ItemShortModel

class Items(BaseRequest):
    """Request all items"""
    __endpoint__ = "/items"

    data: List[ItemShortModel]

