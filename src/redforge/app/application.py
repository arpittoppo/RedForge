"""
Application lifecycle management for RedForge.

This module is responsible for coordinating the startup
and shutdown of the application.
"""

import sys

from PySide6.QtWidgets import QApplication

from redforge.database.session import SessionLocal

from redforge.services.engagement_service import EngagementService
from redforge.services.scope_service import ScopeService
from redforge.services.note_service import NoteService
from redforge.services.recon_service import ReconService
from redforge.services.evidence_service import EvidenceService
from redforge.services.finding_service import FindingService
from redforge.services.report_service import ReportService
from redforge.ui.windows.main_window import MainWindow


class Application:
    """
    Coordinates the lifecycle of the RedForge application.
    """

    def __init__(self) -> None:
        """
        Initialize the application.
        """

        # ==================================================
        # Qt Application
        # ==================================================

        self.qt_app = QApplication(sys.argv)

        # ==================================================
        # Database
        # ==================================================

        self.session = SessionLocal()

        # ==================================================
        # Services
        # ==================================================

        self.engagement_service = EngagementService(
            self.session
        )

        self.scope_service = ScopeService(
            self.session
        )

        self.note_service = NoteService(
            self.session
        )
        self.recon_service = ReconService(
                    self.session
                )
        self.evidence_service = EvidenceService(
            self.session
        )
        self.finding_service = FindingService(
            self.session
        )
        self.report_service = ReportService(
            self.session
        )

        # ==================================================
        # Main Window
        # ==================================================

        self.window = MainWindow(
            engagement_service=self.engagement_service,
            scope_service=self.scope_service,
            note_service=self.note_service,
            recon_service=self.recon_service,
            evidence_service=self.evidence_service,
            finding_service=self.finding_service,
            report_service=self.report_service,
        )

    def run(self) -> None:
        """
        Run the RedForge application.
        """

        self.window.show()

        try:
            sys.exit(self.qt_app.exec())

        finally:
            # Close the database session.
            self.session.close()