from ..exception import ObjectDecodingException


class PhotoSize:
    FIELD_FILEID = 'file_id'
    FIELD_WIDTH = 'width'
    FIELD_HEIGHT = 'height'
    FIELD_FILESIZE = 'file_size'

    def __init__(self, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = PhotoSize(j[PhotoSize.FIELD_FILEID], j[PhotoSize.FIELD_WIDTH],
                            j[PhotoSize.FIELD_HEIGHT])
            if PhotoSize.FIELD_FILESIZE in j:
                obj.file_size = j[PhotoSize.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("PhotoSize", j)

        return obj
