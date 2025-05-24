import aiohttp
from typing import Type, TypeVar
from pydantic import BaseModel
from .common import BASE_URL

T = TypeVar('T', bound=BaseModel)

class WarframeMarketClient:
    """Client for making requests to the Warframe Market API."""
    
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
    
    async def get(self, endpoint: str, model_class: Type[T]) -> T:
        """
        Asynchronous GET request to the API and validate the response.
        
        Args:
            endpoint: API endpoint path (without base URL)
            model_class: Pydantic model to validate against
        Returns:
            Validated model instance
        """
        url = f"{self.base_url}{endpoint}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                return model_class.model_validate(data)