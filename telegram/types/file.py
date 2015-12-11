from ..exception import ObjectDecodingException


class File:
    FIELD_FILEID = 'file_id'
    FIELD_FILESIZE = 'file_size'
    FIELD_FILEPATH = 'file_path'

    def __init__(self, file_id, file_size=None, file_path=None):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path

    @staticmethod
    def decode(j):
        try:
            obj = File(j[File.FIELD_FILEID])
            if File.FIELD_FILESIZE in j:
                obj.file_size = j[File.FIELD_FILESIZE]
            if File.FIELD_FILEPATH in j:
                obj.file_path = j[File.FIELD_FILEPATH]
        except KeyError:
            raise ObjectDecodingException("File", j)

        return obj
