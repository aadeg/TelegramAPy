import json


class ReplayKeyboardHide:
    def __init__(self, hide_keyboard, selective=None):
        self.hide_keyboard = hide_keyboard
        self.selective = selective

    def encode(self):
        out = {'hide_keyboard': self.hide_keyboard}
        if self.selective:
            out['selective'] = self.selective

        return json.dumps(out)
