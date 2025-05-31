import msgspec
from typing import List
from ..common.base import BaseRequest
from ..models.order import OrderModel, OrderWithUserModel


class OrdersRecent(BaseRequest):
    """Get the most recent orders.
    500 max, for the last 4 hours, sorted by createdAt
    """
    __endpoint__ = "/orders/recent"

    data: List[OrderWithUserModel]


class OrdersItem(BaseRequest):
    """Get a list of all orders for an item from users 
    who was online within the last 7 days.

    Requires slug of the item.
    """
    __endpoint__ = "/orders/item/{slug}"

    data: List[OrderWithUserModel]



class _OrdersItemData(msgspec.Struct):
    """Internal model for OrdersItemTop data

    Attributes:
        buy (List[OrderWithUserModel]): List of top buy orders
        sell (List[OrderWithUserModel]): List of top sell orders
    """
    buy: List[OrderWithUserModel]
    sell: List[OrderWithUserModel]

class OrdersItemTop(BaseRequest):
    """This endpoint is designed to fetch the top 5 buy
    and top 5 sell orders for a specific item, exclusively from online users. 
    Orders are sorted by price.

    Requires slug of the item.
    """
    __endpoint__ = "/orders/item/{slug}/top"

    data: _OrdersItemData


class OrdersUser(BaseRequest):
    """Getting public orders from specified user.
    
    Requires user ID (same as slug)
    """
    __endpoint__ = "/orders/user/{slug}"

    data: List[OrderModel]


class OrderId(BaseRequest):
    """Get full info about one, particular order. Requires order ID"""
    __endpoint__ = "/order/{slug}"

    data: OrderWithUserModel