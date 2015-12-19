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

        self.assertEqual(obj.id, j[Chat.FIELD_ID])
        self.assertEqual(obj.first_name, j[Chat.FIELD_FIRSTNAME])
        self.assertEqual(obj.last_name, j[Chat.FIELD_LASTNAME])
        self.assertEqual(obj.username, j[Chat.FIELD_USERNAME])
        self.assertEqual(obj.type, j[Chat.FIELD_TYPE])
        self.assertEqual(obj.title, j[Chat.FIELD_TITLE])
