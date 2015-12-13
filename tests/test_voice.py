import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Voice


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class VoiceTests(unittest.TestCase):
    CHATID =  70021520
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'voice.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(VoiceTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Voice.decode(j)

        self.assertEqual(obj.duration, j[Voice.FIELD_DURATION])
        self.assertEqual(obj.mime_type, j[Voice.FIELD_MIMETYPE])
        self.assertEqual(obj.file_id, j[Voice.FIELD_FILEID])
        self.assertEqual(obj.file_size, j[Voice.FIELD_FILESIZE])
