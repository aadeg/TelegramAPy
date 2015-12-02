from telegram.exception import ObjectDecodingException


class Audio:
    def __init__(self, file_id, duration, performer=None, title=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Audio(j['file_id'], j['duration'])
            if 'performer' in j:
                obj.performer = j['performer']
            if 'title' in j:
                obj.title = j['title']
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("Audio", j)

        return obj

