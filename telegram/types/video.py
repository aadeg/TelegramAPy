from ..exception import ObjectDecodingException
from .photosize import PhotoSize


class Video:
    FIELD_FILEID = 'file_id'
    FIELD_WIDTH = 'width'
    FIELD_HEIGHT = 'height'
    FIELD_DURATION = 'duration'
    FIELD_THUMB = 'thumb'
    FIELD_FILENAME = 'file_name'
    FIELD_MIMETYPE = 'mime_type'
    FIELD_FILESIZE = 'file_size'

    def __init__(self, file_id, width, height, duration, thumb=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Video(j[Video.FIELD_FILEID], j[Video.FIELD_WIDTH],
                        j[Video.FIELD_HEIGHT], j[Video.FIELD_DURATION])
            if Video.FIELD_THUMB in j:
                obj.thumb = PhotoSize.deconde(j[Video.FIELD_THUMB])
            if Video.FIELD_FILENAME in j:
                obj.file_name = j[Video.FIELD_FILENAME]
            if Video.FIELD_MIMETYPE in j:
                obj.mime_type = j[Video.FIELD_MIMETYPE]
            if Video.FIELD_FILESIZE in j:
                obj.file_size = j[Video.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("Video", j)

        return obj
