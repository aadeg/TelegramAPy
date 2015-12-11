import unittest

from tests import TELEGRAM_TOKEN
from telegram.api import TelegramAPI
from telegram.exception import TelegramException, InvalidTokenException


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class GeneralTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(GeneralTests, self).__init__(*args, **kwargs)
        self.api = TelegramAPI(TELEGRAM_TOKEN)

    def test_token(self):
        """Does work with correct token?"""
        self.api.getMe()

    def test_invalid_token(self):
        """Does raise exception with invalid token?"""
        with self.assertRaises(InvalidTokenException):
            TelegramAPI("wrongtoken")

    def test_wrong_token(self):
        """Does raise exception with invalid token?"""
        w_api = TelegramAPI("123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")
        with self.assertRaises(TelegramException):
            w_api.getMe()
