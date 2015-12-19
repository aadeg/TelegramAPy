import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import UserProfilePhotos, PhotoSize


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class UserProfilePhotosTests(unittest.TestCase):
    CHATID = 70021520
    DECODE_FILE = os.path.join(DECODING_FILES_PATH,
                               'userprofilephotos.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(UserProfilePhotosTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = UserProfilePhotos.decode(j)

        self.assertEqual(obj.total_count,
                         j[UserProfilePhotos.FIELD_TOTALCOUNT])
        self.assertIsInstance(obj.photos, list)
        for photo in obj.photos:
            self.assertIsInstance(photo, PhotoSize)
