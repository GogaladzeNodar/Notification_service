from app.services.channels.base_notification import BaseChannels
from app.services.channels.email import EmailChannel
from app.services.channels.sms import SMSChannel
from app.infrastructure.email.email_client import EmailClient
from app.infrastructure.email.email_config import build_fast_mail


class ChannelFactory:
    def __init__(self):
        self._email_client = EmailClient(build_fast_mail())

        self._builders = {
            "email": self._build_email_channel,
            "sms": self._build_sms_channel,
        }

    def _build_email_channel(self) -> BaseChannels:
        return EmailChannel(self._email_client)

    def _build_sms_channel(self) -> BaseChannels:
        return SMSChannel()

    def get_channel(self, channel_type: str) -> BaseChannels:
        try:
            return self._builders[channel_type]()
        except KeyError:
            raise ValueError(f"Unsupported channel type: {channel_type}")









# def get_channel(channel_type: str) -> BaseChannels:
#     """
#     Factory function to get the appropriate channel instance based on the channel type.
    
#     Args:
#         channel_type (str): The type of channel ("sms", "email", etc.).
    
#     Returns:
#         BaseChannel: An instance of the appropriate channel class.
    
#     Raises:
#         ValueError: If the channel type is not supported.
#     """
#     if channel_type == "sms":
#         return SMSChannel()
#     elif channel_type == "email":
#         return EmailChannel()
#     else:
#         raise ValueError(f"Unsupported channel type: {channel_type}")