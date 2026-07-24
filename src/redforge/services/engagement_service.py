"""
Service layer for managing engagements.
"""

from redforge.database.session import SessionLocal
from redforge.models.engagement import Engagement


class EngagementService:
    """Provides operations for creating and managing engagements."""

    def create_engagement(
        self,
        program_name: str,
        platform: str,
        engagement_type: str,
        description: str,
    ) -> Engagement:
        """Create and save a new engagement."""

        session = SessionLocal()

        engagement = Engagement(
            program_name=program_name,
            platform=platform,
            engagement_type=engagement_type,
            description=description,
        )

        session.add(engagement)
        session.commit()
        session.refresh(engagement)
        session.close()

        return engagement