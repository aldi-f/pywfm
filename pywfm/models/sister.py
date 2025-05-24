from pydantic import BaseModel, Field
from ..common.options import LanguageCode


class SisterWeaponI18N(BaseModel):
    """Localization data for a Sister weapon."""
    name: str = Field(alias="itemName")
    wiki_link: str | None = Field(default=None, alias="wikiLink")
    icon: str
    thumb: str


class SisterWeapon(BaseModel):
    """Model for Sister weapons."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    req_mastery_rank: int = Field(alias="reqMasteryRank")
    i18n: dict[LanguageCode, SisterWeaponI18N] = Field(default_factory=dict)


class SisterEphemeraI18N(BaseModel):
    """Localization data for a Sister ephemera."""
    name: str = Field(alias="itemName")
    icon: str
    thumb: str


class SisterEphemera(BaseModel):
    """Model for Sister ephemeras."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    animation: str
    element: str
    i18n: dict[LanguageCode, SisterEphemeraI18N] = Field(default_factory=dict)


class SisterQuirkI18N(BaseModel):
    """Localization data for a Sister quirk."""
    name: str = Field(alias="itemName")
    description: str | None = Field(default=None)
    icon: str
    thumb: str


class SisterQuirk(BaseModel):
    """Model for Sister quirks."""
    id: str
    slug: str
    group: str | None = None
    i18n: dict[LanguageCode, SisterQuirkI18N] = Field(default_factory=dict)