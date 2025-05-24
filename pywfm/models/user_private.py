from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from .activity import Activity
from .user import UserShort
from .achievement import Achievement


class Role(str, Enum):
    """User roles in the system."""
    USER = "user"
    MODERATOR = "moderator"
    # Add other roles as needed


class Tier(str, Enum):
    """Subscription tiers."""
    # none, bronze, silver, gold, diamond
    NONE = "none"
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    DIAMOND = "diamond"

class LinkedAccounts(BaseModel):
    """Model for linked external accounts."""
    pass


class UserPrivate(UserShort):
    """
    Private user profile with full details and sensitive information.
    
    Attributes:
        role: Assigned user role (e.g., moderator, user)
        about: Optional HTML-formatted description
        about_raw: Optional raw markdown description
        mastery_rank: In-game mastery level
        credits: In-game currency balance
        theme: Preferred UI color scheme
        achievement_showcase: List of showcased achievements
        verification: Account verification status
        check_code: Unique verification code
        tier: Subscription tier level
        subscription: Active subscription status
        warned: Whether user has been warned
        warn_message: Warning message if any
        banned: Whether user is banned
        ban_until: Ban expiration date if any
        ban_message: Ban reason if any
        reviews_left: Remaining reviews for today
        unread_messages: Count of unread messages
        ignore_list: List of ignored user IDs
        delete_in_progress: Whether account deletion is pending
        delete_at: Scheduled deletion date if any
        linked_accounts: Connected external accounts
        has_email: Whether email is verified
        created_at: Account creation timestamp
    """
    role: Role
    about: Optional[str] = None
    about_raw: Optional[str] = Field(default=None, alias="aboutRaw")
    mastery_rank: int = Field(alias="masteryRank")
    credits: int
    theme: str
    achievement_showcase: List[Achievement] = Field(default_factory=list, alias="achievementShowcase")
    verification: bool
    check_code: str = Field(alias="checkCode")
    tier: Tier
    subscription: bool
    warned: Optional[bool] = None
    warn_message: Optional[str] = Field(default=None, alias="warnMessage")
    banned: Optional[bool] = None
    ban_until: Optional[str] = Field(default=None, alias="banUntil")
    ban_message: Optional[str] = Field(default=None, alias="banMessage")
    reviews_left: int = Field(alias="reviewsLeft")
    unread_messages: int = Field(alias="unreadMessages")
    ignore_list: List[str] = Field(default_factory=list, alias="ignoreList")
    delete_in_progress: Optional[bool] = Field(default=None, alias="deleteInProgress")
    delete_at: Optional[str] = Field(default=None, alias="deleteAt")
    linked_accounts: LinkedAccounts = Field(alias="linkedAccounts")
    has_email: bool = Field(alias="hasEmail")
    created_at: str = Field(alias="createdAt")