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
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegramapy.api import TelegramAPy
from telegramapy.types import Voice


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class VoiceTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'voice.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPy(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(VoiceTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Voice.decode(j)

        self.assertEqual(obj.duration, j[Voice.FIELD_DURATION])
        self.assertEqual(obj.mime_type, j[Voice.FIELD_MIMETYPE])
        self.assertEqual(obj.file_id, j[Voice.FIELD_FILEID])
        self.assertEqual(obj.file_size, j[Voice.FIELD_FILESIZE])
