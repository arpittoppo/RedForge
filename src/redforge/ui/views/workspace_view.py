"""
Workspace view for RedForge.
"""

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from redforge.services.scope_service import ScopeService
from redforge.services.note_service import NoteService
from redforge.services.recon_service import ReconService
from redforge.services.evidence_service import EvidenceService
from redforge.services.finding_service import FindingService
from redforge.services.report_service import ReportService

from redforge.ui.widgets.sidebar import Sidebar
from redforge.ui.widgets.top_bar import TopBar
from redforge.ui.widgets.status_bar import StatusBar

from redforge.ui.pages.dashboard_page import DashboardPage
from redforge.ui.pages.scope_page import ScopePage
from redforge.ui.pages.recon_page import ReconPage
from redforge.ui.pages.notes_page import NotesPage
from redforge.ui.pages.evidence_page import EvidencePage
from redforge.ui.pages.findings_page import FindingsPage
from redforge.ui.pages.reports_page import ReportsPage
from redforge.ui.pages.settings_page import SettingsPage

from redforge.ui.styles.theme import apply_theme


class WorkspaceView(QWidget):
    """
    Workspace shown after opening an engagement.
    """

    home_requested = Signal()

    def __init__(
        self,
        scope_service: ScopeService,
        note_service: NoteService,
        recon_service: ReconService,
        evidence_service: EvidenceService,
        finding_service: FindingService,
        report_service: ReportService,
        parent=None,
    ):
        super().__init__(parent)

        # ==================================================
        # Services
        # ==================================================

        self.scope_service = scope_service
        self.note_service = note_service
        self.recon_service = recon_service
        self.evidence_service = evidence_service
        self.finding_service = finding_service
        self.report_service = report_service

        # ==================================================
        # Data
        # ==================================================

        self.engagement = None

        # ==================================================
        # Build UI
        # ==================================================

        self._build_ui()

    # ==================================================
    # UI
    # ==================================================

    def _build_ui(self) -> None:
        """
        Build the workspace UI.
        """

        # ==================================================
        # Widgets
        # ==================================================

        self.sidebar = Sidebar()

        self.top_bar = TopBar()

        self.status_bar = StatusBar()

        # ==================================================
        # Pages
        # ==================================================

        self.dashboard_page = DashboardPage(
            note_service=self.note_service,
            finding_service=self.finding_service,
        )

        self.scope_page = ScopePage(
            scope_service=self.scope_service,
        )

        self.recon_page = ReconPage(
            recon_service=self.recon_service,
        )

        self.notes_page = NotesPage(
            note_service=self.note_service,
        )

        self.evidence_page = EvidencePage(
            evidence_service=self.evidence_service,
        )

        self.findings_page = FindingsPage(
            finding_service=self.finding_service,
        )

        self.reports_page = ReportsPage(
            report_service=self.report_service,
        )

        self.settings_page = SettingsPage()

        # ==================================================
        # Stack
        # ==================================================

        self.stack = QStackedWidget()

        pages = [
            self.dashboard_page,
            self.scope_page,
            self.recon_page,
            self.notes_page,
            self.evidence_page,
            self.findings_page,
            self.reports_page,
            self.settings_page,
        ]

        for page in pages:
            self.stack.addWidget(
                page
            )

        self.stack.setCurrentWidget(
            self.dashboard_page
        )

        self.sidebar.set_active(
            "dashboard"
        )

        # ==================================================
        # Signals
        # ==================================================

        self.top_bar.home_requested.connect(
            self._home_requested
        )

        self.sidebar.navigation_requested.connect(
            self._navigate
        )

        self.settings_page.font_scale_changed.connect(
            self._font_scale_changed
        )

        # ==================================================
        # Workspace Layout
        # ==================================================

        workspace_layout = QHBoxLayout()

        workspace_layout.setSpacing(
            0
        )

        workspace_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        workspace_layout.addWidget(
            self.sidebar
        )

        workspace_layout.addWidget(
            self.stack,
            stretch=1,
        )

        # ==================================================
        # Root Layout
        # ==================================================

        root = QVBoxLayout(
            self
        )

        root.setSpacing(
            0
        )

        root.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        root.addWidget(
            self.top_bar
        )

        root.addLayout(
            workspace_layout,
            stretch=1,
        )

        root.addWidget(
            self.status_bar
        )

    # ==================================================
    # Public Methods
    # ==================================================

    def load_engagement(
        self,
        engagement,
    ) -> None:
        """
        Load the selected engagement.
        """

        self.engagement = engagement

        self.top_bar.set_engagement(
            engagement
        )

        self.dashboard_page.load_engagement(
            engagement
        )

        self.scope_page.load_engagement(
            engagement
        )

        self.recon_page.load_engagement(
            engagement
        )

        self.notes_page.load_engagement(
            engagement
        )

        self.evidence_page.load_engagement(
            engagement
        )

        self.findings_page.load_engagement(
            engagement
        )

        self.reports_page.load_engagement(
            engagement
        )

        self._navigate(
            "dashboard"
        )

    # ==================================================
    # Navigation
    # ==================================================

    def _navigate(
        self,
        page: str,
    ) -> None:
        """
        Switch between workspace pages.
        """

        pages = {
            "dashboard": self.dashboard_page,
            "scope": self.scope_page,
            "recon": self.recon_page,
            "notes": self.notes_page,
            "evidence": self.evidence_page,
            "findings": self.findings_page,
            "reports": self.reports_page,
            "settings": self.settings_page,
        }

        widget = pages.get(
            page
        )

        if widget is not None:

            self.stack.setCurrentWidget(
                widget
            )

            self.sidebar.set_active(
                page
            )

    # ==================================================
    # Font Size
    # ==================================================

    def _font_scale_changed(
        self,
        scale: float,
    ) -> None:
        """
        Apply the selected font scale
        to the entire RedForge application.
        """

        app = QApplication.instance()

        if app is None:
            return

        apply_theme(
            app,
            font_scale=scale,
        )

    # ==================================================
    # Home
    # ==================================================

    def _home_requested(
        self,
    ) -> None:
        """
        Forward the home request to MainWindow.
        """

        print(
            "WorkspaceView received Home request"
        )

        self.home_requested.emit()