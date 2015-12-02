from telegram.exception import ObjectDecodingException


class PhotoSize:
    def __init__(self, file_id, width, height, file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = PhotoSize(j['file_id'], j['width'], j['height'])
            if 'file_size' in j:
                obj.file_size = j['file_size']
        except KeyError:
            raise ObjectDecodingException("PhotoSize", j)

        return obj
