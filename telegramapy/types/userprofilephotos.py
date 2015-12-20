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


class UserProfilePhotos:
    FIELD_PHOTOS = 'photos'
    FIELD_TOTALCOUNT = 'total_count'

    def __init__(self, total_count, photos):
        self.total_count = total_count
        self.photos = photos

    @staticmethod
    def decode(j):
        try:
            photos = []
            for i in j[UserProfilePhotos.FIELD_PHOTOS]:
                for k in i:
                    photos.append(PhotoSize.decode(k))

            obj = UserProfilePhotos(j[UserProfilePhotos.FIELD_TOTALCOUNT],
                                    photos)
        except KeyError:
            raise ObjectDecodingException("UserProfilePhotos", j)

        return obj
