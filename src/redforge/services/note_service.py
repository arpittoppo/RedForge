"""
Note service.
"""

from sqlalchemy.orm import Session

from redforge.models.note import Note


class NoteService:
    """
    Handles database operations for Note.
    """

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    # ==================================================
    # Public Methods
    # ==================================================

    def get_note(
        self,
        engagement_id: int,
    ) -> Note | None:
        """
        Return the notes document for an engagement.
        """

        return (
            self.session.query(Note)
            .filter_by(
                engagement_id=engagement_id,
            )
            .first()
        )

    def create_note(
        self,
        engagement_id: int,
    ) -> Note:
        """
        Create a notes document for an engagement.
        """

        note = Note(
            engagement_id=engagement_id,
        )

        self.session.add(note)
        self.session.commit()

        return note

    def save_note(
        self,
        note: Note,
        content: str,
    ) -> None:
        """
        Save notes.
        """

        note.content = content

        self.session.commit()