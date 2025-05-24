from typing import Literal
from pydantic import BaseModel, Field
from ..common.options import LanguageCode

RivenType = Literal["rifle", "shotgun", "pistol", "melee", "kitgun", "zaw"]

class RivenI18N(BaseModel):
    """Localization data for a Riven mod."""
    name: str = Field(alias="itemName")
    wiki_link: str | None = Field(default=None, alias="wikiLink")
    icon: str
    thumb: str

class RivenAttributeI18N(BaseModel):
    """Localization data for a Riven attribute."""
    name: str = Field(alias="effect")
    icon: str
    thumb: str

class Riven(BaseModel):
    """Model for Riven mods."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    group: str | None = None
    riven_type: str | None = Field(alias="rivenType")
    disposition: float
    req_mastery_rank: int = Field(alias="reqMasteryRank")
    i18n: dict[LanguageCode, RivenI18N] = Field(default_factory=dict)

class RivenAttribute(BaseModel):
    """Model for Riven mod attributes."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    group: str | None = None
    prefix: str
    suffix: str
    exclusive_to: list[str] | None = Field(default=None, alias="exclusiveTo")
    positive_is_negative: bool | None = Field(default=None, alias="positiveIsNegative")
    unit: str | None = None
    positive_only: bool | None = Field(default=None, alias="positiveOnly")
    negative_only: bool | None = Field(default=None, alias="negativeOnly")
    i18n: dict[LanguageCode, RivenAttributeI18N] = Field(default_factory=dict)