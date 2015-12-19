import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Video, PhotoSize


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class VideoTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'video.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_video_decode(self):
        with open(VideoTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Video.decode(j)

        self.assertEqual(obj.duration, j[Video.FIELD_DURATION])
        self.assertEqual(obj.mime_type, j[Video.FIELD_MIMETYPE])
        self.assertEqual(obj.file_id, j[Video.FIELD_FILEID])
        self.assertEqual(obj.file_size, j[Video.FIELD_FILESIZE])
        self.assertEqual(obj.width, j[Video.FIELD_WIDTH])
        self.assertEqual(obj.height, j[Video.FIELD_HEIGHT])
        self.assertIsInstance(obj.thumb, PhotoSize)
