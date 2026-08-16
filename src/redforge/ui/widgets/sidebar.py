"""
Sidebar widget for RedForge.
"""

from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
    QLabel,
)

from redforge.ui.styles.tokens import SIDEBAR_WIDTH

# Note: an earlier version of this file used Unicode glyphs (◎ ▲ ▤ etc.)
# as lightweight icons. Several of them fall outside the core glyph set
# most system/UI fonts ship with, so they render inconsistently (missing
# glyph boxes, misaligned baselines) depending on the host's fonts —
# which reads as "text not visible enough". Plain labels + the active
# accent bar carry the same affordance without that risk. Swap in
# QIcon(...)-based icons here once real iconography assets exist.


class Sidebar(QFrame):
    """
    Sidebar navigation for the RedForge workspace.
    """

    navigation_requested = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("sidebar")
        self.setFixedWidth(SIDEBAR_WIDTH)

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
        self.active_page: str | None = None

        self._build_ui()

    def _build_ui(self):
        """
        Build the sidebar UI.
        """

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(2)
        self.layout.setContentsMargins(0, 16, 0, 16)

        brand_label = QLabel("REDFORGE")
        brand_label.setObjectName("eyebrow")
        brand_label.setContentsMargins(18, 0, 0, 0)
        self.layout.addWidget(brand_label)
        self.layout.addSpacing(16)

        for item in self.sidebar_items:

            button = QPushButton(f"   {item['label']}")
            button.setObjectName("navButton")
            button.setCheckable(False)
            button.setCursor(Qt.PointingHandCursor)
            button.setMinimumHeight(38)

            button.clicked.connect(
                lambda checked=False, page=item["id"]: self._navigate(page)
            )

            self.buttons[item["id"]] = button

            self.layout.addWidget(button)

            # Settings sits below a divider, detached from the main flow.
            if item["id"] == "reports":
                self.layout.addStretch()

        self.set_active("dashboard")

    def _navigate(self, page: str):
        """
        Emit a navigation request and update the active nav state.
        """

        self.set_active(page)
        self.navigation_requested.emit(page)

    def set_active(self, page: str):
        """
        Mark a single sidebar button as active and repolish its style.
        """

        if page not in self.buttons:
            return

        if self.active_page and self.active_page in self.buttons:
            old = self.buttons[self.active_page]
            old.setProperty("active", "false")
            old.style().unpolish(old)
            old.style().polish(old)

        new = self.buttons[page]
        new.setProperty("active", "true")
        new.style().unpolish(new)
        new.style().polish(new)

        self.active_page = page

    def button(self, page: str) -> QPushButton:
        """
        Return a sidebar button by its page id.
        """

        return self.buttons[page]
