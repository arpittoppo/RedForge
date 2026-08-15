"""
Top bar widget for RedForge.
"""

from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)

from redforge.ui.styles.tokens import TOPBAR_HEIGHT


class TopBar(QWidget):
    """
    Top bar shown inside the workspace.
    """

    home_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("topBar")
        self.setFixedHeight(TOPBAR_HEIGHT)

        self._build_ui()

    def _build_ui(self):
        """Build the top bar."""

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(20, 0, 20, 0)
        self.main_layout.setSpacing(10)

        # Navigation
        self.back_button = QPushButton("←  All Engagements")
        self.back_button.setObjectName("ghostButton")
        self.back_button.setCursor(Qt.PointingHandCursor)
        self.back_button.clicked.connect(self._home_clicked)

        self.divider_label = QLabel("/")
        self.divider_label.setObjectName("caption")

        # Engagement information
        self.engagement_name_label = QLabel("No Engagement")
        self.engagement_name_label.setStyleSheet("font-weight: 600;")

        self.engagement_info_label = QLabel("")
        self.engagement_info_label.setObjectName("caption")

        # Layout
        self.main_layout.addWidget(self.back_button)
        self.main_layout.addWidget(self.divider_label)
        self.main_layout.addWidget(self.engagement_name_label)
        self.main_layout.addWidget(self.engagement_info_label)
        self.main_layout.addStretch()

    def set_engagement(self, engagement):
        """
        Update the top bar with the selected engagement.
        """

        self.engagement_name_label.setText(engagement.program_name)
        self.engagement_info_label.setText(
            f"{engagement.platform}  ·  {engagement.engagement_type}"
        )

    def _home_clicked(self):
        """
        Handle the Home button click.
        """

        self.home_requested.emit()
