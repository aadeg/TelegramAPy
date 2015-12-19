import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Location


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class LocationTests(unittest.TestCase):
    CHATID = 70021520
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'location.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(LocationTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Location.decode(j)

        self.assertEqual(obj.longitude, j[Location.FIELD_LONGITUDE])
        self.assertEqual(obj.latitude, j[Location.FIELD_LATITUDE])
