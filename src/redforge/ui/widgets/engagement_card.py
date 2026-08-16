from PySide6.QtCore import Signal, Qt

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class EngagementCard(QFrame):
    """
    Card widget representing a single engagement.
    """

    engagement_selected = Signal(int)
    delete_requested = Signal(int)

    def __init__(
        self,
        engagement_id: int,
        program_name: str,
        platform: str,
        engagement_type: str,
        parent=None,
    ):
        super().__init__(parent)

        self.setObjectName("card")
        self.setCursor(Qt.PointingHandCursor)

        self.engagement_id = engagement_id
        self.program_name = program_name
        self.platform = platform
        self.engagement_type = engagement_type

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(16, 14, 12, 14)
        self.main_layout.setSpacing(8)

        self._build_ui()

    def _build_ui(self):
        """
        Build the engagement card.
        """

        # ---- Header row: title + delete -----------------------------
        header_layout = QHBoxLayout()
        header_layout.setSpacing(8)

        self.title_label = QLabel(self.program_name)
        self.title_label.setStyleSheet("font-size: 15px; font-weight: 600;")

        header_layout.addWidget(self.title_label)
        header_layout.addStretch()

        self.delete_button = QPushButton("✕")
        self.delete_button.setObjectName("ghostButton")
        self.delete_button.setFixedSize(26, 26)
        self.delete_button.setCursor(Qt.PointingHandCursor)
        self.delete_button.clicked.connect(self._delete_clicked)

        header_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(header_layout)

        # ---- Meta row: platform + type as small tags -----------------
        meta_layout = QHBoxLayout()
        meta_layout.setSpacing(8)

        self.platform_value_label = QLabel(self.platform)
        self.platform_value_label.setObjectName("caption")

        self.type_value_label = QLabel(f"·  {self.engagement_type}")
        self.type_value_label.setObjectName("caption")

        meta_layout.addWidget(self.platform_value_label)
        meta_layout.addWidget(self.type_value_label)
        meta_layout.addStretch()

        self.main_layout.addLayout(meta_layout)

    def mousePressEvent(self, event):
        """
        Handle mouse click on the engagement card (opens the engagement).
        The delete button is a real child widget and consumes its own
        press event, so clicks on it never reach here.
        """

        self.engagement_selected.emit(self.engagement_id)

        super().mousePressEvent(event)

    def _delete_clicked(self):
        """
        Request deletion of this engagement.
        """

        self.delete_requested.emit(self.engagement_id)
