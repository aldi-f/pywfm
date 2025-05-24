from pydantic import BaseModel, Field
from ..common.options import LanguageCode


class MissionI18N(BaseModel):
    """Localization data for a mission."""
    name: str
    icon: str | None = Field(default=None)
    thumb: str | None = Field(default=None)


class Mission(BaseModel):
    """Model for missions."""
    id: str
    slug: str
    game_ref: str = Field(alias="gameRef")
    i18n: dict[LanguageCode, MissionI18N] = Field(default_factory=dict)