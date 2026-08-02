"""
Report service.
"""

from sqlalchemy.orm import Session

from redforge.models.report import Report


class ReportService:
    """
    Handles database operations for Report.
    """

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    # ==================================================
    # Public Methods
    # ==================================================

    def get_reports(
        self,
        engagement_id: int,
    ) -> list[Report]:
        """
        Return all reports for an engagement.
        """

        return (
            self.session.query(Report)
            .filter_by(
                engagement_id=engagement_id,
            )
            .order_by(
                Report.id
            )
            .all()
        )

    def get_report(
        self,
        report_id: int,
    ) -> Report | None:
        """
        Return a report by its ID.
        """

        return (
            self.session.query(Report)
            .filter_by(
                id=report_id,
            )
            .first()
        )

    def create_report(
        self,
        engagement_id: int,
    ) -> Report:
        """
        Create a new report.
        """

        report = Report(
            engagement_id=engagement_id,
            title="",
            content="",
        )

        self.session.add(
            report
        )

        self.session.commit()

        return report

    def save_report(
        self,
        report: Report,
        title: str,
        content: str,
    ) -> None:
        """
        Save report changes.
        """

        report.title = title
        report.content = content

        self.session.commit()

    def delete_report(
        self,
        report: Report,
    ) -> None:
        """
        Delete a report.
        """

        self.session.delete(
            report
        )

        self.session.commit()