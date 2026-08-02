"""
Notes page.
"""
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QLabel,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

from redforge.services.note_service import NoteService


class NotesPage(QWidget):
    """
    Workspace page for managing an engagement's notes.
    """

    def __init__(
        self,
        note_service: NoteService,
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

        self.note_service = note_service

        # ==================================================
        # Data
        # ==================================================

        self.engagement = None
        self.note = None

        # ==================================================
        # Widgets
        # ==================================================

        self.notes_label = QLabel(
            "Notes"
        )

        self.notes_editor = QPlainTextEdit()
        
        #==================================================
        # Signals
        #==================================================
        self.notes_editor.textChanged.connect(
        self._restart_save_timer)
        self.save_timer.timeout.connect(
        self._save_note)

        # ==================================================
        # Layout
        # ==================================================

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(
            self.notes_label
        )

        self.layout.addWidget(
            self.notes_editor
        )
    def load_engagement(
    self,
    engagement,
):
     """
    Load the engagement notes.
    """

     self.engagement = engagement

     self.note = self.note_service.get_note(
        engagement.id
    )

     if self.note is None:
        self.note = self.note_service.create_note(
            engagement.id
        )
     self.notes_editor.blockSignals(True)  #block the uncessary signal
     self.notes_editor.setPlainText(
        self.note.content
    )
     self.notes_editor.blockSignals(False) #block the uncessary signal

    def _restart_save_timer(self):
     """
     Restart the autosave timer.
     """

     self.save_timer.start(2000) 
    def _save_note(self):
     """
     Save the notes document.
     """

     if self.note is None:
        return

     self.note_service.save_note(
        note=self.note,
        content=self.notes_editor.toPlainText(),
    )