from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB


from app.database import Base
from app.models.enums import NotificationType

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    message = Column(String, nullable=False)
    recipient_id = Column(String, nullable=False)
    recipient = Column(JSONB, nullable=False)
    type = Column(Enum(NotificationType), nullable=False)
    template_id = Column(UUID(as_uuid=True), ForeignKey("templates.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    sent_at = Column(DateTime, nullable=True)

    delivery_logs = relationship("DeliveryLog", back_populates="notification", cascade="all, delete-orphan")


