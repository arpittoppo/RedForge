from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from redforge.database.base import Base
from redforge.database.mixins import TimestampMixin


class Scope(Base, TimestampMixin):

    __tablename__ = "scopes"

    id: Mapped[int] = mapped_column(primary_key=True)

    engagement_id: Mapped[int] = mapped_column(
        ForeignKey("engagements.id")
    )

    scope_type: Mapped[str] = mapped_column(
        String(10)
    )

    target: Mapped[str] = mapped_column(
        String(255)
    )

    engagement = relationship(
        "Engagement",
        back_populates="scopes",
    )