"""
Dashboard page for RedForge.
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)


class DashboardPage(QWidget):
    """
    Main dashboard screen.
    """

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.label = QLabel("Dashboard Page")

        self.main_layout.addWidget(self.label)

        self.setLayout(self.main_layout)