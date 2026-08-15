from pathlib import Path
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
)

from redforge.services.engagement_service import EngagementService
from redforge.services.scope_service import ScopeService
from redforge.services.note_service import NoteService
from redforge.services.recon_service import ReconService
from redforge.services.evidence_service import EvidenceService
from redforge.services.finding_service import FindingService
from redforge.services.report_service import ReportService

from redforge.ui.views.home_view import HomeView
from redforge.ui.views.workspace_view import WorkspaceView


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(
        self,
        engagement_service: EngagementService,
        scope_service: ScopeService,
        note_service: NoteService,
        recon_service: ReconService,
        evidence_service: EvidenceService,
        finding_service: FindingService,
        report_service: ReportService,
    ):
        super().__init__()

        # ==================================================
        # Services
        # ==================================================

        self.engagement_service = engagement_service
        self.scope_service = scope_service
        self.note_service = note_service
        self.recon_service = recon_service
        self.evidence_service = evidence_service
        self.finding_service = finding_service
        self.report_service = report_service

        # ==================================================
        # Window
        # ==================================================

        self.setWindowTitle("RedForge")
        self.resize(1400, 900)

        # Icon

        if getattr(sys, "frozen", False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(__file__).resolve().parents[4]

        icon_path = base_path / "assets" / "redforge.ico"
        self.setWindowIcon(QIcon(str(icon_path)))

        # ==================================================
        # Central Stack
        # ==================================================

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # ==================================================
        # Views
        # ==================================================

        self.home_view = HomeView(
            engagement_service=self.engagement_service,
        )

        self.workspace_view = WorkspaceView(
            scope_service=self.scope_service,
            note_service=self.note_service,
            recon_service=self.recon_service,
            evidence_service=self.evidence_service,
            finding_service=self.finding_service,
            report_service=self.report_service,
        )

        # ==================================================
        # Signals
        # ==================================================

        self.home_view.engagement_selected.connect(
            self._open_engagement
        )

        self.workspace_view.home_requested.connect(
            self._go_home
        )

        # ==================================================
        # Stack
        # ==================================================

        self.stack.addWidget(
            self.home_view
        )

        self.stack.addWidget(
            self.workspace_view
        )

        self.stack.setCurrentWidget(
            self.home_view
        )

    def _open_engagement(
        self,
        engagement_id: int,
    ):
        """
        Open the selected engagement.
        """

        print(
            f"MainWindow received: {engagement_id}"
        )

        engagement = self.engagement_service.get_engagement(
            engagement_id
        )

        if engagement is None:
            return

        self.workspace_view.load_engagement(
            engagement
        )

        self.stack.setCurrentWidget(
            self.workspace_view
        )

    def _go_home(self):
        """
        Return to the Home dashboard.
        """

        print(
            "MainWindow received Home request"
        )

        self.stack.setCurrentWidget(
            self.home_view
        )