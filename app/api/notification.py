from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.notification import NotificationCreateSchema
from app.models.notification import Notification
from app.models.template import Template
from app.models.enums import NotificationType
from app.workers.tasks import send_notification_task


router = APIRouter()

def check_template_exists(db: Session, template_code: str, language: str) -> bool:
    return db.query(Template).filter(
        Template.name == template_code,
        Template.language == language
    ).first() is not None

@router.post("/notify/")
def create_notification(payload: NotificationCreateSchema, db: Session = Depends(get_db)):
    print("Creating notification")
    
    # Check if template exists
    if not check_template_exists(db, payload.template_code, payload.language):
        raise HTTPException(status_code=400, detail=f"Template '{payload.template_code}' not found for language '{payload.language}'")
    
    try:
        notification = Notification(
            template_code=payload.template_code,
            channel=payload.channel,
            recipient_id=payload.recipient.id,
            recipient=payload.recipient.model_dump(),
            data=payload.data,
            language=payload.language,
            type=NotificationType.info,  # default
        )
        db.add(notification)
        db.commit()
        db.refresh(notification)
        print(f"Notification created with ID: {notification.id}")

        send_notification_task.delay(notification.id)  

        return {"status": "queued", "notification_id": notification.id}
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

