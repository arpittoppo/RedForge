"""
Scope page.
"""

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QLabel,
    QPlainTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

from redforge.services.scope_service import ScopeService


class ScopePage(QWidget):
    """
    Workspace page for managing an engagement's scope.
    """

    def __init__(
        self,
        scope_service: ScopeService,
        parent=None,
    ):
        super().__init__(parent)

        # ==================================================
        # Timer
        # ==================================================

        self.save_timer = QTimer(self)
        self.save_timer.setSingleShot(True)

        # ==================================================
        # Services
        # ==================================================

        self.scope_service = scope_service

        # ==================================================
        # Data
        # ==================================================

        self.engagement = None
        self.scope = None

        # ==================================================
        # Widgets
        # ==================================================

        self.in_scope_label = QLabel("IN SCOPE")
        self.in_scope_label.setObjectName("eyebrow")

        self.out_scope_label = QLabel("OUT OF SCOPE")
        self.out_scope_label.setObjectName("eyebrow")

        self.save_status_label = QLabel("Saved")
        self.save_status_label.setObjectName("caption")

        self.in_scope_editor = QPlainTextEdit()
        self.in_scope_editor.setObjectName("mono")
        self.in_scope_editor.setPlaceholderText(
            "*.acme.com\napi.acme.com\n192.168.1.0/24"
        )

        self.out_scope_editor = QPlainTextEdit()
        self.out_scope_editor.setObjectName("mono")
        self.out_scope_editor.setPlaceholderText(
            "staging.acme.com\nthird-party.acme.com"
        )

        # ==================================================
        # Signals
        # ==================================================

        self.save_timer.timeout.connect(self._save_scope)
        self.in_scope_editor.textChanged.connect(self._restart_save_timer)
        self.out_scope_editor.textChanged.connect(self._restart_save_timer)

        # ==================================================
        # Layout
        # ==================================================

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(32, 28, 32, 28)
        self.layout.setSpacing(8)

        self.layout.addWidget(self.in_scope_label)
        self.layout.addWidget(self.in_scope_editor)

        self.layout.addWidget(self.out_scope_label)
        self.layout.addWidget(self.out_scope_editor)

        status_layout = QHBoxLayout()
        status_layout.addStretch()
        status_layout.addWidget(self.save_status_label)
        self.layout.addLayout(status_layout)

    def load_engagement(self, engagement):
        """
        Load the engagement scope.
        """

        self.engagement = engagement

        self.scope = self.scope_service.get_scope(engagement.id)

        if self.scope is None:
            self.scope = self.scope_service.create_scope(engagement.id)

        self.in_scope_editor.blockSignals(True)
        self.out_scope_editor.blockSignals(True)

        self.in_scope_editor.setPlainText(self.scope.in_scope)
        self.out_scope_editor.setPlainText(self.scope.out_scope)

        self.in_scope_editor.blockSignals(False)
        self.out_scope_editor.blockSignals(False)

        self.save_status_label.setText("Saved")

    def _restart_save_timer(self):
        """
        Restart the autosave timer.
        """

        self.save_status_label.setText("Saving...")
        self.save_timer.start(1000)

    def _save_scope(self):
        """
        Save the current scope to the database.
        """

        self.scope_service.save_scope(
            scope=self.scope,
            in_scope=self.in_scope_editor.toPlainText(),
            out_scope=self.out_scope_editor.toPlainText(),
        )

        self.save_status_label.setText("Saved")
