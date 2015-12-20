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


class Location:
    FIELD_LONGITUDE = 'longitude'
    FIELD_LATITUDE = 'latitude'

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    @staticmethod
    def decode(j):
        try:
            obj = Location(j[Location.FIELD_LONGITUDE],
                           j[Location.FIELD_LATITUDE])
        except KeyError:
            raise ObjectDecodingException("Location", j)

        return obj
