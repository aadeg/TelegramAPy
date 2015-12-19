'''
TelegramAPI
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
import unittest
import os
import json

from tests import DECODING_FILES_PATH
from telegram.types import User


class UserTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'user.json')

    def test_user_decode(self):
        with open(UserTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = User.decode(j)

        self.assertEqual(obj.id, j[User.FIELD_ID])
        self.assertEqual(obj.first_name, j[User.FIELD_FIRSTNAME])
        self.assertEqual(obj.last_name, j[User.FIELD_LASTNAME])
        self.assertEqual(obj.username, j[User.FIELD_USERNAME])
