# pywfm
Warframe Market API for python



# Installation (Not yet available)
```bash
```

# Usage
```python
import asyncio
from pywfm.client import WarframeMarketClient
from pywfm.api.item import Items, Item

async def main():
    async with WarframeMarketClient() as client:
        # Get all items in English
        items = await client.get(Items)
        for item in items.data:
            print(item.i18n["en"].name)
        
        # Get a single item 
        item = await client.get(Item,"nova_prime_set")
        print(item)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

```
