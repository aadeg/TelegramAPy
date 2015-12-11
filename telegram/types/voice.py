from ..exception import ObjectDecodingException


class Voice:
    FIELD_FILEID = 'file_id'
    FIELD_DURATION = 'duration'
    FIELD_MIMETYPE = 'mime_type'
    FIELD_FILESIZE = 'file_size'

    def __init__(self, file_id, duration, mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Voice(j[Voice.FIELD_FILEID], j[Voice.FIELD_DURATION])
            if Voice.FIELD_MIMETYPE in j:
                obj.mime_type = j[Voice.FIELD_MIMETYPE]
            if Voice.FIELD_FILESIZE in j:
                obj.file_size = j[Voice.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("Voice", j)

        return obj
