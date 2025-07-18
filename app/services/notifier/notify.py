from app.models.notification import Notification
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.template_render.get_template import TemplateRenderer  
from app.services.channels.dispatcher import NotificationDispatcher

class NotificationService:
    def __init__(self, session: AsyncSession):
        self.template_renderer = TemplateRenderer(session)
        self.dispatcher = NotificationDispatcher()

    async def process_and_dispatch(self, notification: Notification) -> None:
        message = await self.template_renderer.render_by_name(
            name=notification.template_name,
            lang=notification.language,
            context=notification.context
        )
        self.dispatcher.dispatch(notification.channel, notification.recipient, message)
