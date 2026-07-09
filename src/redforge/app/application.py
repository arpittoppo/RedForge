"""
Application lifecycle management for RedForge.

This module is responsible for coordinating the startup
and shutdown of the application.
"""

import sys

from PySide6.QtWidgets import QApplication

from redforge.ui.windows.main_window import MainWindow


class Application:
    """
    Coordinates the lifecycle of the RedForge application.
    """

    def __init__(self) -> None:
        """Initialize the application."""
        self.qt_app = QApplication(sys.argv)
        self.window = MainWindow()

    def run(self) -> None:
        """
        Run the RedForge application.
        """
        self.window.show()
        sys.exit(self.qt_app.exec())