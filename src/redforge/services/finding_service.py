"""
Finding service.
"""

from sqlalchemy.orm import Session

from redforge.models.finding import Finding


class FindingService:
    """
    Handles database operations for Finding.
    """

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    # ==================================================
    # Public Methods
    # ==================================================

    def get_findings(
        self,
        engagement_id: int,
    ) -> list[Finding]:
        """
        Return all findings for an engagement.
        """

        return (
            self.session.query(Finding)
            .filter_by(
                engagement_id=engagement_id,
            )
            .order_by(
                Finding.id
            )
            .all()
        )

    def get_finding(
        self,
        finding_id: int,
    ) -> Finding | None:
        """
        Return a finding by its ID.
        """

        return (
            self.session.query(Finding)
            .filter_by(
                id=finding_id,
            )
            .first()
        )

    def create_finding(
        self,
        engagement_id: int,
    ) -> Finding:
        """
        Create a new finding.
        """

        finding = Finding(
            engagement_id=engagement_id,
            title="",
            severity="Info",
            status="Open",
            description="",
        )

        self.session.add(
            finding
        )

        self.session.commit()

        return finding

    def save_finding(
        self,
        finding: Finding,
        title: str,
        severity: str,
        status: str,
        description: str,
    ) -> None:
        """
        Save finding changes.
        """

        finding.title = title
        finding.severity = severity
        finding.status = status
        finding.description = description

        self.session.commit()

    def delete_finding(
        self,
        finding: Finding,
    ) -> None:
        """
        Delete a finding.
        """

        self.session.delete(
            finding
        )

        self.session.commit()