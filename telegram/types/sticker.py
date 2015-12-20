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
from .document import Document
from .photosize import PhotoSize


class Sticker:
    FIELD_FILEID = 'file_id'
    FIELD_THUMB = 'thumb'
    FIELD_WIDTH = 'width'
    FIELD_HEIGHT = 'height'
    FIELD_FILESIZE = 'file_size'

    def __init__(self, file_id, width, height, thumb=None,
                 file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumb = thumb
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Document(j[Sticker.FIELD_FILEID])
            if Sticker.FIELD_THUMB in j:
                obj.thumb = PhotoSize.decode(j[Sticker.FIELD_THUMB])
            if Sticker.FIELD_WIDTH in j:
                obj.width = j[Sticker.FIELD_WIDTH]
            if Sticker.FIELD_HEIGHT in j:
                obj.height = j[Sticker.FIELD_HEIGHT]
            if Sticker.FIELD_FILESIZE in j:
                obj.file_size = j[Sticker.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("Sticker", j)

        return obj
