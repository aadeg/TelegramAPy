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
from telegram.types import Chat


class ChatTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'chat.json')

    def test_chat_decode(self):
        with open(ChatTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Chat.decode(j)

        self.assertEqual(obj.id, j[Chat.FIELD_ID])
        self.assertEqual(obj.first_name, j[Chat.FIELD_FIRSTNAME])
        self.assertEqual(obj.last_name, j[Chat.FIELD_LASTNAME])
        self.assertEqual(obj.username, j[Chat.FIELD_USERNAME])
        self.assertEqual(obj.type, j[Chat.FIELD_TYPE])
        self.assertEqual(obj.title, j[Chat.FIELD_TITLE])
