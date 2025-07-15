from pydantic import BaseModel, Field
from typing import Optional, Literal, Dict

class RecipientSchema(BaseModel):
    id: str
    phone: Optional[str] = None
    email: Optional[str] = None


class NotificationSchema(BaseModel):
    template_code: str
    channel: Literal["sms", "email", "push"]
    recipient: RecipientSchema
    data: Dict[str, str]  # {"name": "Nodar", "code": "1234"}
    language: Optional[str] = "ka"