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

from tests import TELEGRAM_TOKEN
from telegram.api import TelegramAPy
from telegram.exception import TelegramException, InvalidTokenException


@unittest.skipIf(TELEGRAM_TOKEN is None, 'Unable to get Telegram token')
class GeneralTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(GeneralTests, self).__init__(*args, **kwargs)
        self.api = TelegramAPy(TELEGRAM_TOKEN)

    def test_token(self):
        """Does work with correct token?"""
        self.api.getMe()

    def test_invalid_token(self):
        """Does raise exception with invalid token?"""
        with self.assertRaises(InvalidTokenException):
            TelegramAPy("wrongtoken")

    def test_wrong_token(self):
        """Does raise exception with invalid token?"""
        w_api = TelegramAPy("123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")
        with self.assertRaises(TelegramException):
            w_api.getMe()
