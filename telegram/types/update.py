from telegram.exception import ObjectDecodingException
from .message import Message


class Update:
    def __init__(self, update_id, message=None):
        self.update_id = update_id
        self.message = message

    @staticmethod
    def decode(j):
        try:
            obj = Update(j['update_id'])
            if 'message' in j:
                obj.message = Message.decode(j['message'])
        except KeyError:
            raise ObjectDecodingException("Update", j)

        return obj
