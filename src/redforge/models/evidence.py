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

    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(primary_key=True)

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id")
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    evidence_type: Mapped[str] = mapped_column(
        String(50)
    )

    file_path: Mapped[str] = mapped_column(
        Text
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    engagement: Mapped["Engagement"] = relationship(
        "Engagement",
        back_populates="evidence",
    )