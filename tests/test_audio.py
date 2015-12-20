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
from telegramapy.types import Audio


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class AudioTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'audio.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPy(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(AudioTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Audio.decode(j)

        self.assertEqual(obj.duration, j[Audio.FIELD_DURATION])
        self.assertEqual(obj.mime_type, j[Audio.FIELD_MIMETYPE])
        self.assertEqual(obj.title, j[Audio.FIELD_TITLE])
        self.assertEqual(obj.performer, j[Audio.FIELD_PERFORMER])
        self.assertEqual(obj.file_id, j[Audio.FIELD_FILEID])
        self.assertEqual(obj.file_size, j[Audio.FIELD_FILESIZE])
