from app.workers.celery import celery_app
from app.db.session import async_session
from app.services.processing.notification_processor import NotificationProcessor
import asyncio


@celery_app.task(name="send_notification_task", bind=True)
def send_notification_task(self, notification_id: int):
    async def _main():
        async with async_session() as session:
            processor = NotificationProcessor(session)
            await processor.process(notification_id)

    try:
        asyncio.run(_main())
        return f"Notification {notification_id} sent"
    except Exception as e:
        self.retry(exc=e, countdown=10, max_retries=3)
                



