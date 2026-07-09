"""
Bootstrap module for RedForge.

Responsible for creating and starting the application.
"""

from redforge.app.application import Application


def bootstrap() -> None:
    """
    Create and start the RedForge application.
    """
    app = Application()
    app.run()