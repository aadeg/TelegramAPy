from ..exception import ObjectDecodingException
from .photosize import PhotoSize


class Document:
    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
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
            raise ObjectDecodingException("Document", j)

        return obj
