from pydantic import BaseModel, Field
from ..common.options import LanguageCode


class LocationI18N(BaseModel):
    """Localization data for a location."""
    node_name: str = Field(alias="nodeName")
    system_name: str | None = Field(default=None, alias="systemName")
    icon: str
    thumb: str


class Location(BaseModel):
    """Model for locations."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    faction: str | None = None
    min_level: int | None = Field(default=None, alias="minLevel")
    max_level: int | None = Field(default=None, alias="maxLevel")
    i18n: dict[LanguageCode, LocationI18N] = Field(default_factory=dict)