'''
TelegramAPy
Copyright (C) 2015  Giove Andrea

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''
import unittest
import os
import json
import datetime

from tests import (TELEGRAM_TOKEN, SEND_MESSAGES, DECODING_FILES_PATH,
                   TEST_CHAT_ID)
from telegramapy.api import TelegramAPy
from telegramapy.types import Message, User, Chat


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class MessageTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'message.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPy(TELEGRAM_TOKEN)

    @unittest.skipIf(not SEND_MESSAGES, 'Sending messages skipped')
    def test_simple_message(self):
        """Does it send messages correctly?"""
        msg = self.api.sendMessage(TEST_CHAT_ID,
                                   "test_simple_message")
        self.assertIsInstance(msg, Message)

    @unittest.skipIf(not SEND_MESSAGES, 'Sending messages skipped')
    def test_markdown_message(self):
        """Does it send messages with markdown correctly?"""
        msg = self.api.sendMessage(TEST_CHAT_ID,
                                   "*test_markdown_message*",
                                   parse_mode=TelegramAPy.MARKDOWN_MODE)
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
