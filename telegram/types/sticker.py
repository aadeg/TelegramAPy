from ..exception import ObjectDecodingException
from .document import Document
from .photosize import PhotoSize


class Sticker:
    FIELD_FILEID = 'file_id'
    FIELD_THUMB = 'thumb'
    FIELD_FILENAME = 'file_name'
    FIELD_MIMETYPE = 'mime_type'
    FIELD_FILESIZE = 'file_size'

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
            obj = Document(j[Sticker.FIELD_FILEID])
            if Sticker.FIELD_THUMB in j:
                obj.thumb = PhotoSize.deconde(j[Sticker.FIELD_THUMB])
            if Sticker.FIELD_FILENAME in j:
                obj.file_name = j[Sticker.FIELD_FILENAME]
            if Sticker.FIELD_MIMETYPE in j:
                obj.mime_type = j[Sticker.FIELD_MIMETYPE]
            if Sticker.FIELD_FILESIZE in j:
                obj.file_size = j[Sticker.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("Sticker", j)

        return obj
