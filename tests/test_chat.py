import unittest
import os
import json

from tests import DECODING_FILES_PATH
from telegram.types import Chat


class ChatTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'chat.json')

    def test_chat_decode(self):
        with open(ChatTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Chat.decode(j)

        self.assertEqual(obj.duration, j[Chat.FIELD_DURATION])
        self.assertEqual(obj.mime_type, j[Chat.FIELD_MIMETYPE])
        self.assertEqual(obj.title, j[Chat.FIELD_TITLE])
        self.assertEqual(obj.performer, j[Chat.FIELD_PERFORMER])
        self.assertEqual(obj.file_id, j[Chat.FIELD_FILEID])
        self.assertEqual(obj.file_size, j[Chat.FIELD_FILESIZE])
