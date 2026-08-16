"""
Dashboard page for the workspace.
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from redforge.services.note_service import (
    NoteService,
)

from redforge.services.finding_service import (
    FindingService,
)

from redforge.ui.widgets.stat_card import (
    StatCard,
)


class DashboardPage(QWidget):
    """
    Dashboard page displaying an engagement overview.
    """

    def __init__(
        self,
        note_service: NoteService,
        finding_service: FindingService,
        parent=None,
    ):
        super().__init__(parent)

        # ==================================================
        # Services
        # ==================================================

        self.note_service = note_service
        self.finding_service = finding_service

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

    def _build_ui(
        self,
    ):
        """
        Build the dashboard UI.
        """

        self.main_layout = QVBoxLayout(
            self
        )

        self.main_layout.setContentsMargins(
            32,
            28,
            32,
            28,
        )

        self.main_layout.setSpacing(
            20
        )

        # ==================================================
        # Engagement Information
        # ==================================================

        self.engagement_name_label = QLabel()

        self.engagement_name_label.setObjectName(
            "pageTitle"
        )

        self.engagement_info_label = QLabel()

        self.engagement_info_label.setObjectName(
            "caption"
        )

        self.main_layout.addWidget(
            self.engagement_name_label
        )

        self.main_layout.addWidget(
            self.engagement_info_label
        )

        # ==================================================
        # Statistics Cards
        # ==================================================

        self.scope_card = StatCard(
            "Scope"
        )

        self.recon_card = StatCard(
            "Recon"
        )

        self.evidence_card = StatCard(
            "Evidence"
        )

        self.findings_card = StatCard(
            "Findings"
        )

        cards_layout = QHBoxLayout()

        cards_layout.setSpacing(
            12
        )

        cards_layout.addWidget(
            self.scope_card
        )

        cards_layout.addWidget(
            self.recon_card
        )

        cards_layout.addWidget(
            self.evidence_card
        )

        cards_layout.addWidget(
            self.findings_card
        )

        self.main_layout.addLayout(
            cards_layout
        )

        # ==================================================
        # Recent Findings
        # ==================================================

        self.recent_findings_label = QLabel(
            "RECENT FINDINGS"
        )

        self.recent_findings_label.setObjectName(
            "eyebrow"
        )

        self.main_layout.addWidget(
            self.recent_findings_label
        )

        self.recent_findings_layout = QVBoxLayout()

        self.recent_findings_layout.setSpacing(
            6
        )

        self.main_layout.addLayout(
            self.recent_findings_layout
        )

        # ==================================================
        # Notes Preview
        # ==================================================

        self.notes_preview_title = QLabel(
            "NOTES PREVIEW"
        )

        self.notes_preview_title.setObjectName(
            "eyebrow"
        )

        self.main_layout.addWidget(
            self.notes_preview_title
        )

        self.notes_preview_label = QLabel(
            "No notes yet."
        )

        self.notes_preview_label.setObjectName(
            "caption"
        )

        self.notes_preview_label.setWordWrap(
            True
        )

        self.main_layout.addWidget(
            self.notes_preview_label
        )

        # ==================================================
        # Stretch
        # ==================================================

        self.main_layout.addStretch()

    # ==================================================
    # Public Methods
    # ==================================================

    def load_engagement(
        self,
        engagement,
    ):
        """
        Load engagement information into the dashboard.
        """

        self.engagement = engagement

        # ==================================================
        # Engagement Information
        # ==================================================

        self.engagement_name_label.setText(
            engagement.program_name
        )

        self.engagement_info_label.setText(
            f"{engagement.platform}  ·  "
            f"{engagement.engagement_type}"
        )

        # ==================================================
        # Statistics
        # ==================================================

        self.scope_card.set_count(
            1 if engagement.scope else 0
        )

        self.recon_card.set_count(
            len(
                engagement.recon_entries
            )
        )

        self.evidence_card.set_count(
            len(
                engagement.evidence
            )
        )

        self.findings_card.set_count(
            len(
                engagement.findings
            )
        )

        # ==================================================
        # Dashboard Content
        # ==================================================

        self._load_recent_findings()

        self._load_notes_preview()

    # ==================================================
    # Recent Findings
    # ==================================================

    def _load_recent_findings(
        self,
    ):
        """
        Load recent findings into the dashboard.
        """

        # Remove existing widgets.

        while (
            self.recent_findings_layout.count()
        ):

            item = (
                self.recent_findings_layout.takeAt(
                    0
                )
            )

            widget = item.widget()

            if widget is not None:

                widget.deleteLater()

        # No engagement loaded.

        if self.engagement is None:
            return

        # Get findings.

        findings = (
            self.finding_service.get_findings(
                self.engagement.id
            )
        )

        # No findings.

        if not findings:

            label = QLabel(
                "No findings yet."
            )

            label.setObjectName(
                "caption"
            )

            self.recent_findings_layout.addWidget(
                label
            )

            return

        # Show latest five findings.

        recent_findings = list(
            reversed(
                findings[-5:]
            )
        )

        for finding in recent_findings:

            title = (
                finding.title.strip()
                if finding.title
                else "Untitled finding"
            )

            label = QLabel(
                f"[{finding.severity}] {title}"
            )

            label.setObjectName(
                "caption"
            )

            label.setWordWrap(
                True
            )

            self.recent_findings_layout.addWidget(
                label
            )

    # ==================================================
    # Notes Preview
    # ==================================================

    def _load_notes_preview(
        self,
    ):
        """
        Load a preview of the engagement notes.
        """

        if self.engagement is None:

            self.notes_preview_label.setText(
                "No notes yet."
            )

            return

        note = self.note_service.get_note(
            self.engagement.id
        )

        if (
            note is None
            or not note.content
            or not note.content.strip()
        ):

            self.notes_preview_label.setText(
                "No notes yet."
            )

            return

        content = note.content.strip()

        # Limit the preview length.

        if len(content) > 300:

            content = (
                content[:300]
                + "..."
            )

        self.notes_preview_label.setText(
            content
        )