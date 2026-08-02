from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from redforge.database.base import Base
from redforge.database.mixins import TimestampMixin

if TYPE_CHECKING:
    from .engagement import Engagement


class Note(Base, TimestampMixin):
    """
    Notes document for an engagement.
    """

    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id"),
        unique=True,
    )

    content: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    engagement: Mapped["Engagement"] = relationship(
        "Engagement",
        back_populates="notes",
    )