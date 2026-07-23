from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer

from redforge.database.base import Base
class Engagement(Base):

    __tablename__ = "engagements"

    id: Mapped[int] = mapped_column(primary_key=True)

    program_name: Mapped[str] = mapped_column(String(255))

    platform: Mapped[str] = mapped_column(String(255))

    engagement_type: Mapped[str] = mapped_column(String(255))

    description: Mapped[str] = mapped_column(String(255))