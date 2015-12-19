import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import File


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class FileTests(unittest.TestCase):
    CHATID = 70021520
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'file.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(FileTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = File.decode(j)

        self.assertEqual(obj.file_id, j[File.FIELD_FILEID])
        self.assertEqual(obj.file_size, j[File.FIELD_FILESIZE])
        self.assertEqual(obj.file_path, j[File.FIELD_FILEPATH])
