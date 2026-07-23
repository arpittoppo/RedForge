from pathlib import Path

REDFORGE_HOME = Path.home() / "Documents" / "RedForge"

DATABASE_DIR = REDFORGE_HOME / "database"
ENGAGEMENTS_DIR = REDFORGE_HOME / "engagements"
BACKUPS_DIR = REDFORGE_HOME / "backups"
EXPORTS_DIR = REDFORGE_HOME / "exports"


def initialize_workspace():

    """Create the RedForge workspace directories if they do not exist."""

    folders = [
        REDFORGE_HOME,
        DATABASE_DIR,
        ENGAGEMENTS_DIR,
        BACKUPS_DIR,
        EXPORTS_DIR,
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)