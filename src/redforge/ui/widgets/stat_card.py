"""
Reusable statistic card widget for the RedForge dashboard.
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class StatCard(QFrame):
    """
    Reusable statistic card for displaying dashboard metrics.
    """

    def __init__(
        self,
        title: str,
        count: int = 0,
        parent=None,
    ):
        super().__init__(parent)

        self.setObjectName("card")
        self.title = title
        self.count = count

        self._build_ui()

    def _build_ui(self):
        """
        Build the card UI.
        """

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 16, 18, 16)
        layout.setSpacing(6)

        self.count_label = QLabel(str(self.count))
        self.count_label.setStyleSheet(
            "font-size: 28px; font-weight: 700;"
        )

        self.title_label = QLabel(self.title.upper())
        self.title_label.setObjectName("eyebrow")

        layout.addWidget(self.count_label)
        layout.addWidget(self.title_label)

    def set_count(self, count: int):
        """
        Update the displayed count.
        """

        self.count = count
        self.count_label.setText(str(count))
