"""
Sidebar widget for RedForge.
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)


class Sidebar(QWidget):
    """
    Sidebar navigation for RedForge.
    """

    navigation_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(240)

        self._create_layout()
        self._create_navigation()
        self._create_buttons()

        self.setLayout(self.layout)

    def _create_layout(self):
        """
        Create the sidebar layout.
        """

        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(20, 10, 20, 10)

    def _create_navigation(self):
        """
        Define all sidebar navigation items.
        """

        self.sidebar_items = [
            {"id": "dashboard", "label": "Dashboard"},
            {"id": "scope", "label": "Scope"},
            {"id": "recon", "label": "Recon"},
            {"id": "notes", "label": "Notes"},
            {"id": "evidence", "label": "Evidence"},
            {"id": "findings", "label": "Findings"},
            {"id": "reports", "label": "Reports"},
            {"id": "settings", "label": "Settings"},
        ]

    def _create_buttons(self):
        """
        Create sidebar buttons.
        """

        self.navigation_buttons = {}

        for item in self.sidebar_items:
            button = QPushButton(item["label"])

            self.navigation_buttons[item["id"]] = button

            button.clicked.connect(
                lambda checked=False, page_id=item["id"]: self._handle_navigation(page_id)
            )

            self.layout.addWidget(button)

    def _handle_navigation(self, page_id):
        """
        Handle sidebar navigation.
        """

        self.navigation_requested.emit(page_id)