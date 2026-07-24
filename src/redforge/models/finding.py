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


class Finding(Base, TimestampMixin):

    __tablename__ = "findings"

    id: Mapped[int] = mapped_column(primary_key=True)

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id")
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    severity: Mapped[str] = mapped_column(
        String(20)
    )

    status: Mapped[str] = mapped_column(
        String(30)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    engagement: Mapped["Engagement"] = relationship(
        "Engagement",
        back_populates="findings",
    )