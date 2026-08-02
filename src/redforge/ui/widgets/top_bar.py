"""
Top bar widget for RedForge.
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)


class TopBar(QWidget):
    """
    Top bar shown inside the workspace.
    """

    home_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self._build_ui()

    def _build_ui(self):
        """Build the top bar."""

        self.main_layout = QHBoxLayout(self)

        # Navigation
        self.back_button = QPushButton("← Home")
        self.back_button.clicked.connect(
            self._home_clicked
        )

        # Engagement information
        self.engagement_name_label = QLabel(
            "No Engagement"
        )

        self.engagement_info_label = QLabel("")

        # Layout
        self.main_layout.addWidget(
            self.back_button
        )

        self.main_layout.addWidget(
            self.engagement_name_label
        )

        self.main_layout.addWidget(
            self.engagement_info_label
        )

        self.main_layout.addStretch()

    def set_engagement(
        self,
        engagement,
    ):
        """
        Update the top bar with the selected engagement.
        """

        self.engagement_name_label.setText(
            engagement.program_name
        )

        self.engagement_info_label.setText(
            f"{engagement.platform} • "
            f"{engagement.engagement_type}"
        )

    def _home_clicked(self):
        """
        Handle the Home button click.
        """

        self.home_requested.emit()