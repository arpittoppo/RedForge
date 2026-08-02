"""
Evidence service.
"""

from sqlalchemy.orm import Session

from redforge.models.evidence import Evidence


class EvidenceService:
    """
    Handles database operations for Evidence.
    """

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    # ==================================================
    # Public Methods
    # ==================================================

    def get_evidence(
        self,
        engagement_id: int,
    ) -> list[Evidence]:
        """
        Return all evidence for an engagement.
        """

        return (
            self.session.query(Evidence)
            .filter_by(
                engagement_id=engagement_id,
            )
            .order_by(
                Evidence.id
            )
            .all()
        )

    def get_evidence_item(
        self,
        evidence_id: int,
    ) -> Evidence | None:
        """
        Return an evidence item by its ID.
        """

        return (
            self.session.query(Evidence)
            .filter_by(
                id=evidence_id,
            )
            .first()
        )

    def create_evidence(
        self,
        engagement_id: int,
    ) -> Evidence:
        """
        Create a new evidence item.
        """

        evidence = Evidence(
            engagement_id=engagement_id,
            title="",
            evidence_type="Other",
            file_path="",
            notes="",
        )

        self.session.add(
            evidence
        )

        self.session.commit()

        return evidence

    def save_evidence(
        self,
        evidence: Evidence,
        title: str,
        evidence_type: str,
        file_path: str,
        notes: str,
    ) -> None:
        """
        Save evidence changes.
        """

        evidence.title = title
        evidence.evidence_type = evidence_type
        evidence.file_path = file_path
        evidence.notes = notes

        self.session.commit()

    def delete_evidence(
        self,
        evidence: Evidence,
    ) -> None:
        """
        Delete an evidence item.
        """

        self.session.delete(
            evidence
        )

        self.session.commit()