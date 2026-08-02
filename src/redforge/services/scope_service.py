"""
Scope service.
"""

from sqlalchemy.orm import Session

from redforge.models.scope import Scope


class ScopeService:
    """
    Handles database operations for Scope.
    """

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    # ==================================================
    # Public Methods
    # ==================================================

    def get_scope(
        self,
        engagement_id: int,
    ) -> Scope | None:
        """
        Return the scope for an engagement.
        """

        return (
            self.session.query(Scope)
            .filter_by(
                engagement_id=engagement_id,
            )
            .first()
        )

    def create_scope(
        self,
        engagement_id: int,
    ) -> Scope:
        """
        Create a scope for an engagement.
        """

        scope = Scope(
            engagement_id=engagement_id,
        )

        self.session.add(scope)
        self.session.commit()

        return scope

    def save_scope(
        self,
        scope: Scope,
        in_scope: str,
        out_scope: str,
    ) -> None:
        """
        Save scope changes.
        """

        scope.in_scope = in_scope
        scope.out_scope = out_scope

        self.session.commit()