from fastapi_mail import FastMail, MessageSchema, MessageType


class EmailClient:
    def __init__(self, fast_mail: FastMail):
        self._fast_mail = fast_mail

    async def send(
        self,
        subject: str,
        recipients: list[str],
        body: str,
        html: bool = True,
    ) -> None:
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            subtype=MessageType.html if html else MessageType.plain,
        )

        await self._fast_mail.send_message(message)
