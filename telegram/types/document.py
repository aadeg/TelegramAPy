from ..exception import ObjectDecodingException
from .photosize import PhotoSize


class Document:
    FIELD_FILEID = 'file_id'
    FIELD_THUMB = 'thumb'
    FIELD_FILENAME = 'file_name'
    FIELD_MIMETYPE = 'mime_type'
    FIELD_FILESIZE = 'file_size'

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
            obj = Document(j[Document.FIELD_FILEID])
            if Document.FIELD_THUMB in j:
                obj.thumb = PhotoSize.deconde(j[Document.FIELD_THUMB])
            if Document.FIELD_FILENAME in j:
                obj.file_name = j[Document.FIELD_FILENAME]
            if Document.FIELD_MIMETYPE in j:
                obj.mime_type = j[Document.FIELD_MIMETYPE]
            if Document.FIELD_FILESIZE in j:
                obj.file_size = j[Document.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("Document", j)

        return obj
