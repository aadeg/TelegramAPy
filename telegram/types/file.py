from telegram.exception import ObjectDecodingException


class File:
    def __init__(self, file_id, file_size=None, file_path=None):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path

    @staticmethod
    def decode(j):
        try:
            obj = File(j['file_id'])
            if 'file_size' in j:
                obj.file_size = j['file_size']
            if 'file_path' in j:
                obj.file_path = j['file_path']
        except KeyError:
            raise ObjectDecodingException("File", j)

        return obj
