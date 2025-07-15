from app.workers.celery import celery_app




@celery_app.task(name="send_notification_task", bind=True)
def send_notification_task(self, notification_id: int, recipient: dict):
    print(f"📨 Task started for user {recipient.get('id')}")
    return f"✅ Sent to {recipient.get('phone')}"



