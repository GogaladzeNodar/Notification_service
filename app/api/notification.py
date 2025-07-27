from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.notification import NotificationCreateSchema
from app.models.notification import Notification
from app.workers.tasks import send_notification_task


router = APIRouter()

@router.post("/notify/")
def create_notification(payload: NotificationCreateSchema, db: Session = Depends(get_db)):
    notification = Notification(
        templte_code=payload.template_code,
        recipient_id = payload.recipient.id,
        recipient=payload.recipient.dict(),
        type = payload.channel,
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)

    send_notification_task.delay(notification.id)  #payload.recipient.dict()

    return {"status": "queued", "notification_id": notification.id}

