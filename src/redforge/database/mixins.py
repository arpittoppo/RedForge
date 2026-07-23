from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.now,
)