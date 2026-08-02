"""
Dashboard page for the workspace.
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from redforge.ui.widgets.stat_card import StatCard


class DashboardPage(QWidget):
    """
    Dashboard page displaying an engagement overview.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.engagement = None

        self._build_ui()

    def _build_ui(self):
        """
        Build the dashboard UI.
        """

        main_layout = QVBoxLayout(self)

        # Engagement Information
        self.engagement_name_label = QLabel()

        self.engagement_info_label = QLabel()

        main_layout.addWidget(
            self.engagement_name_label
        )

        main_layout.addWidget(
            self.engagement_info_label
        )

        # Statistics Cards
        self.scope_card = StatCard("Scope")
        self.recon_card = StatCard("Recon")
        self.evidence_card = StatCard("Evidence")
        self.findings_card = StatCard("Findings")

        cards_layout = QHBoxLayout()

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

        main_layout.addLayout(
            cards_layout
        )

        # Recent Findings
        self.recent_findings_label = QLabel(
            "Recent Findings"
        )

        main_layout.addWidget(
            self.recent_findings_label
        )

        # Recent Notes
        self.recent_notes_label = QLabel(
            "Recent Notes"
        )

        main_layout.addWidget(
            self.recent_notes_label
        )

        main_layout.addStretch()

    def load_engagement(
    self,
    engagement,):
     """
    Load engagement information into the dashboard.
    """

     self.engagement = engagement

     self.engagement_name_label.setText(
        engagement.program_name
    )

     self.engagement_info_label.setText(
        f"{engagement.platform} • {engagement.engagement_type}"
    )

     self.scope_card.set_count(
        1 if engagement.scope else 0
    )

     self.recon_card.set_count(
        len(engagement.recon_entries)
    )

     self.evidence_card.set_count(
        len(engagement.evidence)
    )

     self.findings_card.set_count(
        len(engagement.findings)
    )