"""
Recon service.
"""

from sqlalchemy.orm import Session

from redforge.models.recon import Recon


class ReconService:
    """
    Handles database operations for Recon.
    """

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    # ==================================================
    # Public Methods
    # ==================================================

    def get_recons(
        self,
        engagement_id: int,
    ) -> list[Recon]:
        """
        Return all recon entries for an engagement.
        """

        return (
            self.session.query(Recon)
            .filter_by(
                engagement_id=engagement_id,
            )
            .order_by(
                Recon.id
            )
            .all()
        )

    def get_recon(
        self,
        recon_id: int,
    ) -> Recon | None:
        """
        Return a recon entry by its ID.
        """

        return (
            self.session.query(Recon)
            .filter_by(
                id=recon_id,
            )
            .first()
        )

    def create_recon(
        self,
        engagement_id: int,
    ) -> Recon:
        """
        Create a new recon entry.
        """

        recon = Recon(
            engagement_id=engagement_id,
            recon_type="Other",
            value="",
        )

        self.session.add(
            recon
        )

        self.session.commit()

        return recon

    def save_recon(
        self,
        recon: Recon,
        recon_type: str,
        value: str,
    ) -> None:
        """
        Save recon changes.
        """

        recon.recon_type = recon_type
        recon.value = value

        self.session.commit()

    def delete_recon(
        self,
        recon: Recon,
    ) -> None:
        """
        Delete a recon entry.
        """

        self.session.delete(
            recon
        )

        self.session.commit()