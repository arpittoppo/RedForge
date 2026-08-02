from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

from redforge.services.engagement_service import EngagementService
from redforge.ui.pages.home_dashboard_page import HomeDashboardPage


class HomeView(QWidget):
    """
    Home screen shown when RedForge starts.
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

    def _build_ui(self):

        self.main_layout = QVBoxLayout(self)

        self.home_dashboard_page = HomeDashboardPage(
            self.engagement_service
        )

        # Listen for engagement selections from the dashboard
        self.home_dashboard_page.engagement_selected.connect(
            self._engagement_selected
        )

        self.main_layout.addWidget(
            self.home_dashboard_page
        )

    def _engagement_selected(
        self,
        engagement_id: int,
    ):
        """Handle engagement selection from the dashboard."""

        print(f"HomeView received: {engagement_id}")

        # Pass the signal up to MainWindow
        self.engagement_selected.emit(
            engagement_id
        )