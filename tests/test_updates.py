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
import unittest
import json
import os

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegramapy.api import TelegramAPy
from telegramapy.types import Update, Message


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class UpdatesTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'update.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPy(TELEGRAM_TOKEN)

    def test_get_updates(self):
        upds = self.api.getUpdates()
        if upds:
            for upd in upds:
                self.assertIsInstance(upd, Update)
        else:
            self.skip("No updates recieved.")

    def test_update_decode(self):
        with open(UpdatesTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Update.decode(j)

        self.assertEqual(obj.update_id, j[Update.FIELD_UPDATEID])
        self.assertIsInstance(obj.message, Message)
