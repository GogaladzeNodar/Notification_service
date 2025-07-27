from abc import ABC, abstractmethod


class BaseChannels(ABC):
    @abstractmethod
    async def send_notification(self, recipient: dict, message: str, **kwargs):
        """
        Sends a notification to the recipient.
            
            :param recipient: A dictionary containing recipient details (e.g., phone, email).
            :param message: The message to be sent.
            :param kwargs: Additional parameters for the notification.
        """
        pass

    

