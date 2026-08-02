from sqlalchemy.orm import Session

from redforge.services.engagement_service import EngagementService


class ServiceContainer:

    def __init__(self, session: Session):
        self.engagement = EngagementService(session)