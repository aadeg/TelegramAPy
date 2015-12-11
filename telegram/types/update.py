from ..exception import ObjectDecodingException
from .message import Message


class Update:
    FIELD_UPDATEID = 'update_id'
    FIELD_MESSAGE = 'message'

    def __init__(self, update_id, message=None):
        self.update_id = update_id
        self.message = message

    @staticmethod
    def decode(j):
        try:
            obj = Update(j[Update.FIELD_UPDATEID])
            if Update.FIELD_MESSAGE in j:
                obj.message = Message.decode(j[Update.FIELD_MESSAGE])
        except KeyError:
            raise ObjectDecodingException("Update", j)

        return obj
