from PySide6.QtCore import Signal

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

        self.engagement_id = engagement_id
        self.program_name = program_name
        self.platform = platform
        self.engagement_type = engagement_type

        self.main_layout = QVBoxLayout(self)

        self._build_ui()

    def _build_ui(
        self,
    ):
        """
        Build the engagement card.
        """

        # ==================================================
        # Title
        # ==================================================

        self.title_label = QLabel(
            self.program_name
        )

        self.main_layout.addWidget(
            self.title_label
        )

        # ==================================================
        # Platform
        # ==================================================

        self.platform_layout = QHBoxLayout()

        self.platform_text_label = QLabel(
            "Platform:"
        )

        self.platform_value_label = QLabel(
            self.platform
        )

        self.platform_layout.addWidget(
            self.platform_text_label
        )

        self.platform_layout.addWidget(
            self.platform_value_label
        )

        self.main_layout.addLayout(
            self.platform_layout
        )

        # ==================================================
        # Type
        # ==================================================

        self.type_layout = QHBoxLayout()

        self.type_text_label = QLabel(
            "Type:"
        )

        self.type_value_label = QLabel(
            self.engagement_type
        )

        self.type_layout.addWidget(
            self.type_text_label
        )

        self.type_layout.addWidget(
            self.type_value_label
        )

        self.main_layout.addLayout(
            self.type_layout
        )

        # ==================================================
        # Actions
        # ==================================================

        self.actions_layout = QHBoxLayout()

        self.actions_layout.addStretch()

        self.delete_button = QPushButton(
            "Delete"
        )

        self.actions_layout.addWidget(
            self.delete_button
        )

        self.main_layout.addLayout(
            self.actions_layout
        )

        self.delete_button.clicked.connect(
            self._delete_clicked
        )

    def mousePressEvent(
        self,
        event,
    ):
        """
        Handle mouse click on the engagement card.
        """

        print(
            f"Card clicked! ID = {self.engagement_id}"
        )

        self.engagement_selected.emit(
            self.engagement_id
        )

        super().mousePressEvent(
            event
        )

    def _delete_clicked(
        self,
    ):
        """
        Request deletion of this engagement.
        """

        self.delete_requested.emit(
            self.engagement_id
        )