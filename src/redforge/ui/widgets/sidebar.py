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
    Sidebar navigation for the RedForge workspace.
    """

    navigation_requested = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(240)

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

        self.buttons: dict[str, QPushButton] = {}

        self._build_ui()

    def _build_ui(self):
        """
        Build the sidebar UI.
        """

        self.layout = QVBoxLayout(self)

        self.layout.setSpacing(10)
        self.layout.setContentsMargins(
            20,
            10,
            20,
            10,
        )

        for item in self.sidebar_items:

            button = QPushButton(
                item["label"]
            )

            button.clicked.connect(
                lambda checked=False, page=item["id"]: self._navigate(page)
            )

            self.buttons[item["id"]] = button

            self.layout.addWidget(
                button
            )

        # Keep the navigation buttons at the top.
        self.layout.addStretch()

    def _navigate(
        self,
        page: str,
    ):
        """
        Emit a navigation request.
        """

        self.navigation_requested.emit(
            page
        )

    def button(
        self,
        page: str,
    ) -> QPushButton:
        """
        Return a sidebar button by its page id.
        """

        return self.buttons[page]