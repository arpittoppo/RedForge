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


class Recon(Base, TimestampMixin):
    """
    Stores a single recon entry for an engagement.
    """

    __tablename__ = "recons"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id"),
    )

    recon_type: Mapped[str] = mapped_column(
        String(100),
    )

    value: Mapped[str] = mapped_column(
        Text,
        default="",
    )

    engagement: Mapped["Engagement"] = relationship(
        "Engagement",
        back_populates="recon_entries",
    )