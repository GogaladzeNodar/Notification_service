from app.workers.celery import celery_app
from app.db.session import async_session
#from asgiref.sync import async_to_sync
from app.db.session import get_async_db
from app.services.processing.notification_processor import NotificationProcessor
#import asyncio


@celery_app.task(name="send_notification_task", bind=True)
def send_notification_task(self, notification_id: str):
    import asyncio
    try:
        asyncio.run(run(notification_id))
        return f"Notification {notification_id} sent"
    except Exception as e:
        raise self.retry(exc=e, countdown=10, max_retries=3)


async def run(notification_id: str):
    async with get_async_db() as session:
        processor = NotificationProcessor(session)
        await processor.process(notification_id)
        await session.commit()