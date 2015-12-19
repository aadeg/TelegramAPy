import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Document, PhotoSize


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class DocumentTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'document.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(DocumentTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Document.decode(j)

        self.assertEqual(obj.file_id, j[Document.FIELD_FILEID])
        self.assertEqual(obj.mime_type, j[Document.FIELD_MIMETYPE])
        self.assertEqual(obj.file_name, j[Document.FIELD_FILENAME])
        self.assertEqual(obj.file_size, j[Document.FIELD_FILESIZE])
        self.assertIsInstance(obj.thumb, PhotoSize)
