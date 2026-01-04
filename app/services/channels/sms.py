from app.services.channels.base_notification import BaseChannels


class SMSChannel(BaseChannels):
    """
    SMS channel for sending notifications.
    """

    async def send_notification(self, recipient: dict, message: dict, **kwargs) -> None:
        """
        Send an SMS notification to the recipient.
        """
        print(f"[MOCK SMS] Sending SMS to {recipient['phone']}: {message['body']}")