'''
TelegramAPy
Copyright (C) 2015  Giove Andrea

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
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
