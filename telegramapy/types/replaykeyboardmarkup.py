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
import json


class ReplayKeyboardMarkup:
    FIELD_KEYBOARD = 'keyboard'
    FIELD_RESIZEKEYBOARD = 'resize_keyboard'
    FIELD_ONETIMEKEYBOARD = 'one_time_keyboard'
    FIELD_SELECTIVE = 'selective'

    def __init__(self, keyboard, resize_keyboard=None, one_time_keyboard=None,
                 selective=None):
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    def encode(self):
        out = {ReplayKeyboardMarkup.FIELD_KEYBOARD: self.keyboard}
        if self.resize_keyboard:
            out[ReplayKeyboardMarkup.FIELD_RESIZEKEYBOARD] = self.resize_keyboard
        if self.one_time_keyboard:
            out[ReplayKeyboardMarkup.FIELD_ONETIMEKEYBOARD] = self.one_time_keyboard
        if self.selective:
            out[ReplayKeyboardMarkup.FIELD_SELECTIVE] = self.selective

        return json.dumps(out)
