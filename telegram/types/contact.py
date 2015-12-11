from ..exception import ObjectDecodingException


class Contact:
    FIELD_PHONENUMBER = 'phone_number'
    FIELD_FIRSTNAME = 'first_name'
    FIELD_LASTNAME = 'last_name'
    FIELD_USERID = 'user_id'

    def __init__(self, phone_number, first_name, last_name=None, user_id=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    @staticmethod
    def decode(j):
        try:
            obj = Contact(j[Contact.FIELD_PHONENUMBER],
                          j[Contact.FIELD_FIRSTNAME])
            if Contact.FIELD_LASTNAME in j:
                obj.last_name = j[Contact.FIELD_LASTNAME]
            if Contact.FIELD_USERID in j:
                obj.user_id = j[Contact.FIELD_USERID]
        except KeyError:
            raise ObjectDecodingException("Contact", j)

        return obj
