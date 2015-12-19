import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Audio


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class AudioTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'audio.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

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
