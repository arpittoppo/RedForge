from redforge.database.base import Base
from redforge.database.engine import engine

import redforge.models


def initialize_database() -> None:
    """Create all database tables if they do not already exist."""
    Base.metadata.create_all(bind=engine)