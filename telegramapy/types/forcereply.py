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


class ForceReply:
    FIELD_FORCEREPLY = 'force_reply'
    FIELD_SELECTIVE = 'selective'

    def __init__(self, force_reply, selective=None):
        self.force_reply = force_reply
        self.selective = selective

    def encode(self):
        out = {ForceReply.FIELD_FORCEREPLY: self.force_reply}
        if self.selective:
            out[ForceReply.FIELD_SELECTIVE] = self.selective

        return json.dumps(out)
