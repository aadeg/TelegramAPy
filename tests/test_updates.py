import unittest
import json
import os

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Update, Message, User


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class UpdatesTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'update.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

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
