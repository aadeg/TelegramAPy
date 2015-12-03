from ..exception import ObjectDecodingException
from .photosize import PhotoSize


class Video:
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
            obj = Video(j['file_id'], j['width'], j['height'],
                                j['duration'])
            if 'thumb' in j:
                obj.thumb = PhotoSize.deconde(j['thumb'])
            if 'file_name' in j:
                obj.file_name = j['file_name']
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("Video", j)

        return obj
