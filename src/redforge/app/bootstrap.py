"""
Bootstrap module for RedForge.

Responsible for initializing the application environment
and starting the application.
"""

from redforge.app.application import Application
from redforge.core.paths import initialize_workspace
from redforge.database.initializer import initialize_database


def bootstrap() -> None:
    """
    Initialize RedForge and start the application.
    """

    # Create the RedForge workspace folders.
    initialize_workspace()

    # Create the database and tables.
    initialize_database()

    # Start the application.
    app = Application()
    app.run()