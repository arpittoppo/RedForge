from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from redforge.database.base import Base
from redforge.database.mixins import TimestampMixin

if TYPE_CHECKING:
    from .engagement import Engagement


class Report(Base, TimestampMixin):

    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(primary_key=True)

    engagement_id: Mapped[int] = mapped_column(ForeignKey("engagements.id"))

    title: Mapped[str] = mapped_column(String(255))

    content: Mapped[str] = mapped_column(Text,default="",)

    engagement: Mapped["Engagement"] = relationship(
        "Engagement",
        back_populates="reports",
    )