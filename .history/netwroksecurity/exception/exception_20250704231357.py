import sys
class NetworkSecurityException(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details