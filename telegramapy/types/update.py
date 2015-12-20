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
from .message import Message


class Update:
    FIELD_UPDATEID = 'update_id'
    FIELD_MESSAGE = 'message'

    def __init__(self, update_id, message=None):
        self.update_id = update_id
        self.message = message

    @staticmethod
    def decode(j):
        try:
            obj = Update(j[Update.FIELD_UPDATEID])
            if Update.FIELD_MESSAGE in j:
                obj.message = Message.decode(j[Update.FIELD_MESSAGE])
        except KeyError:
            raise ObjectDecodingException("Update", j)

        return obj
