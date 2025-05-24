from typing import Any, Generic, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T', bound=BaseModel)

class BaseResponseModel(BaseModel, Generic[T]):
    """Base model for all Warframe Market API responses."""
    api_version: str = Field(alias="apiVersion")
    data: T
    error: Optional[Any] = None