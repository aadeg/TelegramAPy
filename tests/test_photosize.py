import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import PhotoSize


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class PhotoSizeTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'photosize.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(PhotoSizeTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = PhotoSize.decode(j)

        self.assertEqual(obj.file_id, j[PhotoSize.FIELD_FILEID])
        self.assertEqual(obj.file_size, j[PhotoSize.FIELD_FILESIZE])
        self.assertEqual(obj.width, j[PhotoSize.FIELD_WIDTH])
        self.assertEqual(obj.height, j[PhotoSize.FIELD_HEIGHT])
