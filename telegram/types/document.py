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
from .photosize import PhotoSize


class Document:
    FIELD_FILEID = 'file_id'
    FIELD_THUMB = 'thumb'
    FIELD_FILENAME = 'file_name'
    FIELD_MIMETYPE = 'mime_type'
    FIELD_FILESIZE = 'file_size'

    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None,
                 file_size=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Document(j[Document.FIELD_FILEID])
            if Document.FIELD_THUMB in j:
                obj.thumb = PhotoSize.decode(j[Document.FIELD_THUMB])
            if Document.FIELD_FILENAME in j:
                obj.file_name = j[Document.FIELD_FILENAME]
            if Document.FIELD_MIMETYPE in j:
                obj.mime_type = j[Document.FIELD_MIMETYPE]
            if Document.FIELD_FILESIZE in j:
                obj.file_size = j[Document.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("Document", j)

        return obj
