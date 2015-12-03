from ..exception import ObjectDecodingException


class Contact:
    def __init__(self, phone_number, first_name, last_name=None, user_id=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    @staticmethod
    def decode(j):
        try:
            obj = Contact(j['phone_number'], j['first_name'])
            if 'last_name' in j:
                obj.last_name = j['last_name']
            if 'user_id' in j:
                obj.user_id = j['user_id']
        except KeyError:
            raise ObjectDecodingException("Contact", j)

        return obj
