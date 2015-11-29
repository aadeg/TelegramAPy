class TelegramException(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return repr(self.info)


class ObjectDecodingException(TelegramException):
    MSG = "Exception trying to decode a %s object."

    def __init__(self, obj_type, j):
        TelegramException.__init__(self,
                                   ObjectDecodingException.MSG % self.obj_type)
        self.obj_type = obj_type
        self.json = j

    def __str__(self):
        return "Exception trying to decode a %s object." % (
            self.obj_type)
