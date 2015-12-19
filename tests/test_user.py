import unittest
import os
import json

from tests import DECODING_FILES_PATH
from telegram.types import User


class UserTests(unittest.TestCase):
    DECODE_FILE = os.path.join(DECODING_FILES_PATH, 'user.json')

    def test_user_decode(self):
        with open(UserTests.DECODE_FILE) as json_file:
            j = json.load(json_file)
        obj = User.decode(j)

        self.assertEqual(obj.id, j[User.FIELD_ID])
        self.assertEqual(obj.first_name, j[User.FIELD_FIRSTNAME])
        self.assertEqual(obj.last_name, j[User.FIELD_LASTNAME])
        self.assertEqual(obj.username, j[User.FIELD_USERNAME])
