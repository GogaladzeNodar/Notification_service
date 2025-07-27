from app.services.channels.base_notification import BaseChannels
from app.services.channels.email import EmailChannel
from app.services.channels.sms import SMSChannel


class ChannelFactory:
    """
    Factory class to create channel instances based on the channel type.
    
    This class provides a method to get the appropriate channel instance
    based on the provided channel type.
    """

    def __init__(self):
        self._channels = {
            "sms": SMSChannel(),
            "email": EmailChannel(),
        }
            
    
    def get_channel(self, channel_type: str) -> BaseChannels:
        channel_class = self._channels.get(channel_type)
        if not channel_class:
            raise ValueError(f"Unsupported channel type: {channel_type}")
        return channel_class









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