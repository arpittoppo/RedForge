from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from redforge.database.base import Base
from redforge.database.mixins import TimestampMixin

if TYPE_CHECKING:
    from .engagement import Engagement

class Recon(Base, TimestampMixin):

    __tablename__ = "recon"

    id: Mapped[int] = mapped_column(primary_key=True)

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id")
    )

    recon_type: Mapped[str] = mapped_column(
        String(50)
    )

    value: Mapped[str] = mapped_column(
        Text
    )

    engagement: Mapped["Engagement"] = relationship(
        "Engagement",
        back_populates="recon_entries",
    )