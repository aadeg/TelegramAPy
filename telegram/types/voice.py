from telegram.exception import ObjectDecodingException


class Voice:
    def __init__(self, file_id, duration, mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Voice(j['file_id'], j['duration'])
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("Voice", j)

        return obj
