from redforge.services.engagement_service import EngagementService

service = EngagementService()

engagement = service.create_engagement(
    program_name="RedForge Test",
    platform="HackerOne",
    engagement_type="Bug Bounty",
    description="Testing SQLAlchemy integration."
)

print(f"Created engagement with ID: {engagement.id}")