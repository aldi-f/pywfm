from pydantic import BaseModel, Field
from .activity import Activity
from .achievement import Achievement

class UserShort(BaseModel):
    """
    Short form user data model.
    
    Attributes:
        id: Unique identifier of the user
        ingame_name: In-game name of the user
        avatar: Optional avatar image URL
        reputation: Reputation score
        locale: Preferred communication language (e.g., 'en', 'ko', 'es')
        platform: Gaming platform used by the user
        crossplay: Whether the user has crossplay enabled
        status: Current status of the user
        activity: Current activity of the user
        last_seen: Timestamp of the user's last online presence
    """
    id: str
    ingame_name: str = Field(alias="ingameName")
    avatar: str | None = None
    reputation: int
    locale: str
    platform: str
    crossplay: bool
    status: str
    activity: Activity
    last_seen: str = Field(alias="lastSeen")


class User(UserShort):
    """
    Full user profile model that extends UserShort.
    
    Additional Attributes:
        background: Optional profile background image URL
        about: Optional HTML-formatted user description
        mastery_level: Optional in-game mastery level
        achievement_showcase: List of showcased achievements
        banned: Whether the user is currently banned
        ban_until: Optional ban expiration timestamp
        warned: Whether the user has been warned (mod/admin only)
        warn_message: Optional warning message (mod/admin only)
        ban_message: Optional ban reason (mod/admin only)
    """
    background: str | None = None
    about: str | None = None
    mastery_level: int | None = Field(default=None, alias="masteryLevel")
    achievement_showcase: list[Achievement] = Field(
        default_factory=list,
        alias="achievementShowcase"
    )
    banned: bool | None = None
    ban_until: str | None = Field(default=None, alias="banUntil")
    warned: bool | None = None
    warn_message: str | None = Field(default=None, alias="warnMessage")
    ban_message: str | None = Field(default=None, alias="banMessage")

