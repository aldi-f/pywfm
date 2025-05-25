import msgspec
from ..common.options import LanguageCode


class NpcI18N(msgspec.Struct):
    """Localization data for an NPC."""
    name: str
    icon: str
    thumb: str


class Npc(msgspec.Struct):
    """Model for NPCs."""
    id: str
    slug: str
    game_ref: str = msgspec.field(name="gameRef")
    i18n: dict[LanguageCode, NpcI18N] = msgspec.field(default_factory=dict)