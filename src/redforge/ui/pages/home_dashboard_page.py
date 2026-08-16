"""
Home dashboard page for RedForge.
"""

from PySide6.QtCore import Signal, Qt, QSize

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QMessageBox,
)

from redforge.services.engagement_service import (
    EngagementService,
)

from redforge.ui.dialogs.new_engagement_dialog import (
    NewEngagementDialog,
)

from redforge.ui.widgets.engagement_card import (
    EngagementCard,
)


class HomeDashboardPage(QWidget):
    """
    Home page shown when RedForge starts.
    """

    engagement_selected = Signal(int)

    def __init__(
        self,
        engagement_service: EngagementService,
        parent=None,
    ):
        super().__init__(parent)

        self.engagement_service = engagement_service
        self._all_engagements = []

        self._build_ui()
        self._connect_signals()
        self.load_engagements()

    def _build_ui(self):
        """
        Build the user interface.
        """

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(32, 28, 32, 28)
        self.main_layout.setSpacing(20)

        # ---- Header row: title + new engagement -----------------------
        header_layout = QHBoxLayout()

        title_block = QVBoxLayout()
        title_block.setSpacing(2)

        eyebrow = QLabel("REDFORGE")
        eyebrow.setObjectName("eyebrow")

        self.title_label = QLabel("Engagements")
        self.title_label.setObjectName("pageTitle")

        title_block.addWidget(eyebrow)
        title_block.addWidget(self.title_label)

        header_layout.addLayout(title_block)
        header_layout.addStretch()

        self.new_engagement_button = QPushButton("+  New Engagement")
        self.new_engagement_button.setObjectName("primaryButton")
        self.new_engagement_button.setCursor(Qt.PointingHandCursor)
        self.new_engagement_button.setMinimumHeight(36)

        header_layout.addWidget(
            self.new_engagement_button, alignment=Qt.AlignTop
        )

        self.main_layout.addLayout(header_layout)

        # ---- Search -----------------------------------------------------
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search by program, platform, or engagement type..."
        )
        self.search_input.setMinimumHeight(36)

        self.main_layout.addWidget(self.search_input)

        # ---- List ---------------------------------------------------
        self.recent_engagements_label = QLabel("ALL ENGAGEMENTS")
        self.recent_engagements_label.setObjectName("eyebrow")

        self.main_layout.addWidget(self.recent_engagements_label)

        self.engagement_list = QListWidget()
        self.engagement_list.setSpacing(6)
        self.engagement_list.setFrameShape(QListWidget.NoFrame)

        self.main_layout.addWidget(self.engagement_list)

        # ---- Empty state -------------------------------------------------
        self.empty_state_label = QLabel(
            "No engagements yet — start your first one above."
        )
        self.empty_state_label.setObjectName("caption")
        self.empty_state_label.setAlignment(Qt.AlignCenter)
        self.empty_state_label.setVisible(False)

        self.main_layout.addWidget(self.empty_state_label)

    def _connect_signals(self):
        """
        Connect widget signals.
        """

        self.new_engagement_button.clicked.connect(self._new_engagement)
        self.search_input.textChanged.connect(self._apply_filter)

    def _new_engagement(self):
        """
        Open the New Engagement dialog.
        """

        dialog = NewEngagementDialog(self)

        if dialog.exec():

            data = dialog.get_data()

            engagement = self.engagement_service.create_engagement(**data)

            print(
                f"Created engagement #{engagement.id}: "
                f"{engagement.program_name}"
            )

            self.load_engagements()

    def _engagement_selected(self, engagement_id: int):
        """
        Handle engagement selection.
        """

        self.engagement_selected.emit(engagement_id)

    def _delete_engagement(self, engagement_id: int):
        """
        Delete an engagement after confirmation.
        """

        reply = QMessageBox.question(
            self,
            "Delete Engagement",
            (
                "Are you sure you want to delete "
                "this engagement?\n\n"
                "This action cannot be undone."
            ),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply != QMessageBox.Yes:
            return

        success = self.engagement_service.delete_engagement(engagement_id)

        if success:
            self.load_engagements()

    def load_engagements(self):
        """
        Load all engagements into the list.
        """

        self._all_engagements = self.engagement_service.get_all_engagements()
        self._render_engagements(self._all_engagements)

    def _apply_filter(self, text: str):
        """
        Client-side filter over the already-loaded engagement list.
        Purely presentational — does not touch the service layer.
        """

        text = text.strip().lower()

        if not text:
            self._render_engagements(self._all_engagements)
            return

        filtered = [
            e
            for e in self._all_engagements
            if text in e.program_name.lower()
            or text in e.platform.lower()
            or text in e.engagement_type.lower()
        ]

        self._render_engagements(filtered)

    def _render_engagements(self, engagements):
        """
        Render a list of engagements as cards.
        """

        self.engagement_list.clear()

        self.empty_state_label.setVisible(len(engagements) == 0)
        self.engagement_list.setVisible(len(engagements) > 0)

        for engagement in engagements:

            card = EngagementCard(
                engagement.id,
                engagement.program_name,
                engagement.platform,
                engagement.engagement_type,
            )

            card.engagement_selected.connect(self._engagement_selected)
            card.delete_requested.connect(self._delete_engagement)

            item = QListWidgetItem()

            # QListWidget::item padding/margin (set globally in the QSS
            # theme) is reserved *inside* this same rect when a custom
            # widget is attached via setItemWidget — without this buffer
            # the card gets squeezed shorter than its own sizeHint() and
            # text baselines/descenders get clipped.
            hint = card.sizeHint()
            item.setSizeHint(QSize(hint.width(), hint.height() + 16))
            item.setFlags(Qt.NoItemFlags)

            self.engagement_list.addItem(item)
            self.engagement_list.setItemWidget(item, card)
