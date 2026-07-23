from sqlalchemy import create_engine
from redforge.core.paths import DATABASE_DIR
DATABASE_PATH = DATABASE_DIR / "redforge.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
engine = create_engine(DATABASE_URL)