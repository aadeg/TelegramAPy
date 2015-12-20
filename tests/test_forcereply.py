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

from tests import TELEGRAM_TOKEN, DECODING_FILES_PATH
from telegram.api import TelegramAPy
from telegram.types import ForceReply


class ForceReplyTests(unittest.TestCase):
    RESULTS_FILE = os.path.join(DECODING_FILES_PATH, 'forcereply.json')

    def test_forcereply_encode(self):
        with open(ForceReplyTests.RESULTS_FILE) as json_file:
            j = json.load(json_file)
        tests = j['tests']

        fr = ForceReply(True)
        self.assertEquals(fr.encode(), tests[0])

        fr = ForceReply(True, True)
        self.assertEquals(fr.encode(), tests[1])