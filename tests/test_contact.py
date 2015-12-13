import unittest
import os
import json

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPI
from telegram.types import Contact


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class ContactTests(unittest.TestCase):
    CHATID =  70021520
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'contact.json')

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_photosize_decode(self):
        with open(ContactTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = Contact.decode(j)

        self.assertEqual(obj.phone_number, j[Contact.FIELD_PHONENUMBER])
        self.assertEqual(obj.first_name, j[Contact.FIELD_FIRSTNAME])
        self.assertEqual(obj.last_name, j[Contact.FIELD_LASTNAME])
        self.assertEqual(obj.user_id, j[Contact.FIELD_USERID])
