"""
Home dashboard page for RedForge.
"""

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
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

        self._build_ui()
        self._connect_signals()
        self.load_engagements()

    def _build_ui(
        self,
    ):
        """
        Build the user interface.
        """

        self.main_layout = QVBoxLayout(self)

        self.title_label = QLabel(
            "Home"
        )

        self.new_engagement_button = QPushButton(
            "+ New Engagement"
        )

        self.search_input = QLineEdit()

        self.search_input.setPlaceholderText(
            "Search engagements..."
        )

        self.recent_engagements_label = QLabel(
            "Recent Engagements"
        )

        self.engagement_list = QListWidget()

        self.main_layout.addWidget(
            self.title_label
        )

        self.main_layout.addWidget(
            self.new_engagement_button
        )

        self.main_layout.addWidget(
            self.search_input
        )

        self.main_layout.addWidget(
            self.recent_engagements_label
        )

        self.main_layout.addWidget(
            self.engagement_list
        )

    def _connect_signals(
        self,
    ):
        """
        Connect widget signals.
        """

        self.new_engagement_button.clicked.connect(
            self._new_engagement
        )

    def _new_engagement(
        self,
    ):
        """
        Open the New Engagement dialog.
        """

        dialog = NewEngagementDialog(
            self
        )

        if dialog.exec():

            data = dialog.get_data()

            engagement = (
                self.engagement_service.create_engagement(
                    **data
                )
            )

            print(
                f"Created engagement #{engagement.id}: "
                f"{engagement.program_name}"
            )

            self.load_engagements()

    def _engagement_selected(
        self,
        engagement_id: int,
    ):
        """
        Handle engagement selection.
        """

        self.engagement_selected.emit(
            engagement_id
        )

    def _delete_engagement(
        self,
        engagement_id: int,
    ):
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

        success = (
            self.engagement_service.delete_engagement(
                engagement_id
            )
        )

        if success:

            self.load_engagements()

    def load_engagements(
        self,
    ):
        """
        Load all engagements into the list.
        """

        engagements = (
            self.engagement_service.get_all_engagements()
        )

        self.engagement_list.clear()

        for engagement in engagements:

            card = EngagementCard(
                engagement.id,
                engagement.program_name,
                engagement.platform,
                engagement.engagement_type,
            )

            card.engagement_selected.connect(
                self._engagement_selected
            )

            card.delete_requested.connect(
                self._delete_engagement
            )

            item = QListWidgetItem()

            item.setSizeHint(
                card.sizeHint()
            )

            self.engagement_list.addItem(
                item
            )

            self.engagement_list.setItemWidget(
                item,
                card,
            )