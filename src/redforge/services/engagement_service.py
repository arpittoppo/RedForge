from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from redforge.models.engagement import Engagement


class EngagementService:

    def __init__(self, session: Session):
        self.session = session

    # -------------------------
    # Create
    # -------------------------

    def create_engagement(
        self,
        program_name: str,
        platform: str,
        engagement_type: str,
        description: str,
        last_opened_at: datetime | None = None,
    ) -> Engagement:
        engagement = Engagement(
            program_name=program_name,
            platform=platform,
            engagement_type=engagement_type,
            description=description,
            last_opened_at=last_opened_at,
        )

        self.session.add(engagement)
        self.session.commit()
        self.session.refresh(engagement)

        return engagement

    # -------------------------
    # Read (Single)
    # -------------------------

    def get_engagement(self, engagement_id: int) -> Engagement | None:
        return self.session.get(Engagement, engagement_id)

    # -------------------------
    # Read (All)
    # -------------------------

    def get_all_engagements(self) -> list[Engagement]:
        statement = select(Engagement)
        result = self.session.execute(statement)
        return result.scalars().all()

    # -------------------------
    # Update
    # -------------------------

    def update_engagement(
        self,
        engagement_id: int,
        program_name: str,
        platform: str,
        engagement_type: str,
        description: str,
        last_opened_at: datetime | None = None,
    ) -> Engagement | None:

        engagement = self.session.get(Engagement, engagement_id)

        if engagement is None:
            return None

        engagement.program_name = program_name
        engagement.platform = platform
        engagement.engagement_type = engagement_type
        engagement.description = description
        engagement.last_opened_at = last_opened_at

        self.session.commit()
        self.session.refresh(engagement)

        return engagement

    # -------------------------
    # Delete
    # -------------------------

    def delete_engagement(self, engagement_id: int) -> bool:

        engagement = self.session.get(Engagement, engagement_id)

        if engagement is None:
            return False

        self.session.delete(engagement)
        self.session.commit()

        return True

    