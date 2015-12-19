import unittest
import os
import json
import datetime

from tests import TELEGRAM_TOKEN, SEND_MESSAGES, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Message, User, Chat


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class MessageTests(unittest.TestCase):
    CHATID = 70021520
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'message.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    @unittest.skipIf(not SEND_MESSAGES, 'Sending messages skipped')
    def test_simple_message(self):
        """Does it send messages correctly?"""
        msg = self.api.sendMessage(MessageTests.CHATID,
                                   "test_simple_message")
        self.assertIsInstance(msg, Message)

    @unittest.skipIf(not SEND_MESSAGES, 'Sending messages skipped')
    def test_markdown_message(self):
        """Does it send messages with markdown correctly?"""
        msg = self.api.sendMessage(MessageTests.CHATID,
                                   "*test_markdown_message*",
                                   parse_mode=TelegramAPI.MARKDOWN_MODE)
        self.assertIsInstance(msg, Message)

    def test_message_decode(self):
        with open(MessageTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Message.decode(j)

        self.assertEqual(obj.message_id, j[Message.FIELD_MESSAGEID])
        self.assertEqual(obj.text, j[Message.FIELD_TEXT])

        self.assertIsInstance(obj.date, datetime.datetime)
        self.assertIsInstance(obj.from_, User)
        self.assertIsInstance(obj.chat, Chat)
        self.assertIsInstance(obj.forward_from, User)
        self.assertIsInstance(obj.reply_to_message, Message)
