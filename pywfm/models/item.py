from pydantic import BaseModel, Field
from ..common.options import LanguageCode


class ItemI18N(BaseModel):
    """Localization data for an item."""
    name: str
    description: str | None = None
    wiki_link: str | None = Field(default=None, alias="wikiLink")
    icon: str
    thumb: str
    sub_icon: str | None = Field(default=None, alias="subIcon")

class ItemShort(BaseModel):
    """Short form item data model."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    tags: list[str] = Field(default_factory=list)
    i18n: dict[LanguageCode, ItemI18N] = Field(default_factory=dict)
    max_rank: int | None = Field(default=None, alias="maxRank")
    max_charges: int | None = Field(default=None, alias="maxCharges")
    vaulted: bool | None = None
    ducats: int | None = None
    amber_stars: int | None = Field(default=None, alias="amberStars")
    cyan_stars: int | None = Field(default=None, alias="cyanStars")
    base_endo: int | None = Field(default=None, alias="baseEndo")
    endo_multiplier: float | None = Field(default=None, alias="endoMultiplier")
    subtypes: list[str] = Field(default_factory=list)

class Item(ItemShort):
    """Full item data model that extends ItemShort."""
    tradable: bool | None = None
    set_root: bool | None = Field(default=None, alias="setRoot")
    set_parts: list[str] | None = Field(default=None, alias="setParts")
    quantity_in_set: int | None = Field(default=None, alias="quantityInSet")
    rarity: str | None = None
    bulk_tradable: bool | None = Field(default=None, alias="bulkTradable")
    max_amber_stars: int | None = Field(default=None, alias="maxAmberStars")
    max_cyan_stars: int | None = Field(default=None, alias="maxCyanStars")
    req_mastery_rank: int | None = Field(default=None, alias="reqMasteryRank")
    trading_tax: int | None = Field(default=None, alias="tradingTax")
    vosfor: int | None = None