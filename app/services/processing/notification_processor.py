from app.models.notification import Notification
from app.services.notifier.notify import NotificationService
from sqlalchemy.ext.asyncio import AsyncSession


class NotificationProcessor:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.service = NotificationService(session)

    async def process(self, notification_id: int):
        notification = await self.session.get(Notification, notification_id)
        if not notification:
            raise ValueError(f"Notification with ID {notification_id} not found.")
        
        await self.service.process_and_dispatch(notification)
        
        

    