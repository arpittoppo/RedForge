from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from redforge.database.base import Base
from redforge.database.mixins import TimestampMixin

if TYPE_CHECKING:
    from .engagement import Engagement


class Evidence(Base, TimestampMixin):
    """
    Stores a single evidence item for an engagement.
    """

    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id"),
    )

    title: Mapped[str] = mapped_column(
        String(255),
        default="",
    )

    evidence_type: Mapped[str] = mapped_column(
        String(100),
        default="Other",
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        default="",
    )

    notes: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    engagement: Mapped["Engagement"] = relationship(
        "Engagement",
        back_populates="evidence",
    )