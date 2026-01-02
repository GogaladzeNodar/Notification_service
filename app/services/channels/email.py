from app.services.channels.base_notification import BaseChannels



class EmailChannel(BaseChannels):
    """
    Email channel for sending notifications.
    """

    async def send_notification(self, recipient: dict, message: dict, **kwargs) -> None:
        """
        Send an email notification to the recipient.
        """
        print(f"[MOCK email] Sending email to {recipient['email']}: Title: {message['title']}, Body: {message['body']}")