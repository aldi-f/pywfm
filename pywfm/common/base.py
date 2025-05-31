import msgspec
from typing import TypeVar, ClassVar, Type, Optional, Any


class Base(msgspec.Struct, kw_only=True):
    """Base model"""
    api_version: str = msgspec.field(name="apiVersion")
    error: Optional[Any] = None

T = TypeVar('T', bound=Base)

class BaseRequest(Base):
    """Base model for all Warframe Market API requests."""
    __endpoint__: ClassVar[str]

    @classmethod
    def _decode(cls: Type[T], response: str) -> T:
        """Decode the response string into a BaseResponse object."""
        return msgspec.json.decode(response, type=cls)
