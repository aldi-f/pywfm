import msgspec
from typing import Any, Generic, Optional, TypeVar, ClassVar, Type
from ..models.item import ItemShortModel


class BaseData(msgspec.Struct, kw_only=True):
    """Base model for all Warframe Market API calls."""
    pass

T = TypeVar('T', bound=BaseData)

class BaseResponse(msgspec.Struct, Generic[T]):
    """Base model for all Warframe Market API responses."""
    api_version: str = msgspec.field(name="apiVersion")
    data: T
    error: Optional[Any] = None

class BaseRequest(msgspec.Struct):
    """Base model for all Warframe Market API requests."""
    __endpoint__: ClassVar[str]
    __data__: ClassVar[Type]

    @classmethod
    def _decode(cls, response: str) -> BaseResponse[T]:
        """Decode the response string into a BaseResponse object."""
        response_type = cls.__data__ 
        decoder = msgspec.json.Decoder(BaseResponse[response_type])
        return decoder.decode(response)

