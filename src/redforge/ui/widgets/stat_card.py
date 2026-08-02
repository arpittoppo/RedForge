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

        self.title = title
        self.count = count

        self._build_ui()

    def _build_ui(self):
        """
        Build the card UI.
        """

        layout = QVBoxLayout(self)

        self.title_label = QLabel(
            self.title
        )

        self.count_label = QLabel(
            str(self.count)
        )

        layout.addWidget(
            self.title_label
        )

        layout.addWidget(
            self.count_label
        )

    def set_count(
        self,
        count: int,
    ):
        """
        Update the displayed count.
        """

        self.count = count

        self.count_label.setText(
            str(count)
        )