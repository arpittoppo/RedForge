from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from redforge.database.base import Base
from redforge.database.mixins import TimestampMixin

if TYPE_CHECKING:
    from .scope import Scope
    from .recon import Recon
    from .note import Note
    from .evidence import Evidence
    from .finding import Finding
    from .report import Report


class Engagement(Base, TimestampMixin):

    __tablename__ = "engagements"

    id: Mapped[int] = mapped_column(primary_key=True)

    program_name: Mapped[str] = mapped_column(String(255))

    platform: Mapped[str] = mapped_column(String(100))

    engagement_type: Mapped[str] = mapped_column(String(100))

    description: Mapped[str] = mapped_column(String(1000))

    last_opened_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # One Scope per Engagement
    scope: Mapped["Scope"] = relationship(
        "Scope",
        back_populates="engagement",
        uselist=False,
        cascade="all, delete-orphan",
    )

    # One-to-Many
    recon_entries: Mapped[list["Recon"]] = relationship(
        "Recon",
        back_populates="engagement",
        cascade="all, delete-orphan",
    )

    notes: Mapped["Note"] = relationship(
        "Note",
        back_populates="engagement",
        cascade="all, delete-orphan",
    )

    evidence: Mapped[list[Evidence]] = relationship(
    "Evidence",
    back_populates="engagement",
    cascade="all, delete-orphan",
    )

    findings: Mapped[list[Finding]] = relationship(
    "Finding",
    back_populates="engagement",
    cascade="all, delete-orphan",
)

    reports: Mapped[list[Report]] = relationship(
        "Report",
        back_populates="engagement",
        cascade="all, delete-orphan",
    )