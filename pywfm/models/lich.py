from pydantic import BaseModel, Field
from ..common.options import LanguageCode


# Lich Weapon
class LichWeaponI18N(BaseModel):
    """Localization data for a Lich weapon."""
    name: str = Field(alias="itemName")  # Changed to match Go struct's json tag
    wiki_link: str | None = Field(default=None, alias="wikiLink")
    icon: str
    thumb: str

class LichWeapon(BaseModel):
    """Model for Kuva/Sister Lich weapons."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    req_mastery_rank: int = Field(alias="reqMasteryRank")
    i18n: dict[LanguageCode, LichWeaponI18N] = Field(default_factory=dict)


# Lich Ephemera
class LichEphemeraI18N(BaseModel):
    """Localization data for a Lich ephemera."""
    name: str = Field(alias="itemName")
    icon: str
    thumb: str

class LichEphemera(BaseModel):
    """Model for Kuva/Sister Lich ephemeras."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    animation: str
    element: str
    i18n: dict[LanguageCode, LichEphemeraI18N] = Field(default_factory=dict)


# Lich Quirk
class LichQuirkI18N(BaseModel):
    """Localization data for a Lich quirk."""
    name: str = Field(alias="itemName")
    description: str | None = Field(default=None)
    icon: str | None = Field(default=None)
    thumb: str | None = Field(default=None)


class LichQuirk(BaseModel):
    """Model for Kuva/Sister Lich quirks."""
    id: str
    slug: str
    group: str | None = None
    i18n: dict[LanguageCode, LichQuirkI18N] = Field(default_factory=dict)