"""
Scope model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from redforge.database.base import Base
from redforge.database.mixins import TimestampMixin


class Scope(Base, TimestampMixin):
    """
    Stores the scope information for an engagement.
    """

    __tablename__ = "scopes"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id"),
        unique=True,
    )

    in_scope: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    out_scope: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    engagement = relationship(
        "Engagement",
        back_populates="scope",
    )