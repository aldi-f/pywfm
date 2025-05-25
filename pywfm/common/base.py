import msgspec
from typing import Any, Generic, Optional, TypeVar

T = TypeVar('T')

class BaseResponseModel(msgspec.Struct, Generic[T]):
    """Base model for all Warframe Market API responses."""
    api_version: str = msgspec.field(name="apiVersion")
    data: T
    error: Optional[Any] = None