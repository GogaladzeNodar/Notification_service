from app.models.notification import Notification
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.template_render.get_template import TemplateRenderer  
from app.services.channels.dispatcher import NotificationDispatcher

class NotificationService:
    def __init__(self, session: AsyncSession):
        self.template_renderer = TemplateRenderer(session)
        self.dispatcher = NotificationDispatcher()

    async def process_and_dispatch(self, notification: Notification) -> None:
        rendered = await self.template_renderer.render_by_name(
            name=notification.template_code,
            lang=notification.language,
            context=notification.data
        )
        recipient_data = notification.recipient
        await self.dispatcher.dispatch(notification.channel, recipient_data, rendered)
