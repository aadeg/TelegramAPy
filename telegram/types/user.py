from ..exception import ObjectDecodingException


class User:
    def __init__(self, _id, first_name, last_name=None, username=None):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @staticmethod
    def decode(j):
        try:
            obj = User(j['id'], j['first_name'])
            if 'last_name' in j:
                obj.last_name = j['last_name']
            if 'username' in j:
                obj.username = j['username']
        except KeyError:
            raise ObjectDecodingException("User", j)

        return obj
