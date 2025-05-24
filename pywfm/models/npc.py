from pydantic import BaseModel, Field
from ..common.options import LanguageCode


class NpcI18N(BaseModel):
    """Localization data for an NPC."""
    name: str
    icon: str
    thumb: str


class Npc(BaseModel):
    """Model for NPCs."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    i18n: dict[LanguageCode, NpcI18N] = Field(default_factory=dict)