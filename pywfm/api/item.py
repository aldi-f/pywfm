import msgspec
from typing import List
from ..common.base import BaseRequest
from ..models.item import ItemShortModel, ItemModel


class Items(BaseRequest):
    """Get list of all tradable items"""
    __endpoint__ = "/items"

    data: List[ItemShortModel]


class Item(BaseRequest):
    """Get full info about one, particular item. Requires slug"""
    __endpoint__ = "/item/{slug}"

    data: ItemModel


class _ItemSetData(msgspec.Struct):
    """Internal model for ItemSet data
    
    Attributes:
        id (str): Unique identifier for the item set
        items (List[ItemModel]): List of items in the set
    """
    id: str
    items: List[ItemModel]

class ItemSet(BaseRequest):
    """Retrieve Information on Item Sets. Requires slug"""
    __endpoint__ = "/item/{slug}/set"

    data: _ItemSetData