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


class Audio:
    FIELD_FILEID = 'file_id'
    FIELD_DURATION = 'duration'
    FIELD_PERFORMER = 'performer'
    FIELD_TITLE = 'title'
    FIELD_MIMETYPE = 'mime_type'
    FIELD_FILESIZE = 'file_size'

    def __init__(self, file_id, duration, performer=None, title=None,
                 mime_type=None, file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size

    @staticmethod
    def decode(j):
        try:
            obj = Audio(j[Audio.FIELD_FILEID], j[Audio.FIELD_DURATION])
            if Audio.FIELD_PERFORMER in j:
                obj.performer = j[Audio.FIELD_PERFORMER]
            if Audio.FIELD_TITLE in j:
                obj.title = j[Audio.FIELD_TITLE]
            if Audio.FIELD_MIMETYPE in j:
                obj.mime_type = j[Audio.FIELD_MIMETYPE]
            if Audio.FIELD_FILESIZE in j:
                obj.file_size = j[Audio.FIELD_FILESIZE]
        except KeyError:
            raise ObjectDecodingException("Audio", j)

        return obj
