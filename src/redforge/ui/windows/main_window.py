"""
Main window for RedForge.
"""

from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RedForge")
        self.resize(1400, 900)