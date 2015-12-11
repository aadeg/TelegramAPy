from ..exception import ObjectDecodingException


class User:
    FIELD_ID = 'id'
    FIELD_FIRSTNAME = 'first_name'
    FIELD_LASTNAME = 'last_name'
    FIELD_USERNAME = 'username'

    def __init__(self, _id, first_name, last_name=None, username=None):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @staticmethod
    def decode(j):
        try:
            obj = User(j[User.FIELD_ID], j[User.FIELD_FIRSTNAME])
            if User.FIELD_LASTNAME in j:
                obj.last_name = j[User.FIELD_LASTNAME]
            if User.FIELD_USERNAME in j:
                obj.username = j[User.FIELD_USERNAME]
        except KeyError:
            raise ObjectDecodingException("User", j)

        return obj
