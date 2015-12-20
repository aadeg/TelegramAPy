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
