from app.services.channels.base_notification import BaseChannels
from app.infrastructure.email.email_client import EmailClient


class EmailChannel(BaseChannels):
    """
    Email channel for sending notifications.
    """

    def __init__(self, email_client: EmailClient):
        self._email_client = email_client


    async def send_notification(self, recipient: dict, message: dict, **kwargs) -> None:
        """
        Send an email notification to the recipient.
        """
        print(f"[DEBUG] Sending email to {recipient['email']} with subject '{message['title']}' and body '{message['body']}'")
        await self._email_client.send(
            subject=message["title"],
            recipients=[recipient["email"]],
            body=message["body"],
        )