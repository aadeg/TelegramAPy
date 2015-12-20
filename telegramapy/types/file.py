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


class File:
    FIELD_FILEID = 'file_id'
    FIELD_FILESIZE = 'file_size'
    FIELD_FILEPATH = 'file_path'

    def __init__(self, file_id, file_size=None, file_path=None):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path

    @staticmethod
    def decode(j):
        try:
            obj = File(j[File.FIELD_FILEID])
            if File.FIELD_FILESIZE in j:
                obj.file_size = j[File.FIELD_FILESIZE]
            if File.FIELD_FILEPATH in j:
                obj.file_path = j[File.FIELD_FILEPATH]
        except KeyError:
            raise ObjectDecodingException("File", j)

        return obj
