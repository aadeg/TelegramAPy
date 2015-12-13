import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Sticker, PhotoSize


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class StickerTests(unittest.TestCase):
    CHATID =  70021520
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'sticker.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(StickerTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Sticker.decode(j)

        self.assertEqual(obj.file_id, j[Sticker.FIELD_FILEID])
        self.assertEqual(obj.width, j[Sticker.FIELD_WIDTH])
        self.assertEqual(obj.height, j[Sticker.FIELD_HEIGHT])
        self.assertEqual(obj.file_size, j[Sticker.FIELD_FILESIZE])
        self.assertIsInstance(obj.thumb, PhotoSize)
