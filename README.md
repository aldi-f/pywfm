# pywfm
Warframe Market API for python



# Installation (Not yet available)
```bash
```

# Usage
```python
import asyncio
from pywfm.client import WarframeMarketClient
from pywfm.api.item import Items
from pywfm.common import Language


async def main():
    async with WarframeMarketClient() as client:
        items = await client.get(Items)
        for item in items.data:
            print(item.i18n["en"].name)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

```
