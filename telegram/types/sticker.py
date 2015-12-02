from telegram.exception import ObjectDecodingException
from .document import Document
from .photosize import PhotoSize


class Sticker:
    def __init__(self, file_id, width, height, thumb=None,
                 file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumb = thumb
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Document(j['file_id'])
            if 'thumb' in j:
                obj.thumb = PhotoSize.deconde(j['thumb'])
            if 'file_name' in j:
                obj.file_name = j['file_name']
            if 'mime_type' in j:
                obj.mime_type = j['mime_type']
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("Sticker", j)

        return obj
