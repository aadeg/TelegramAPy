import json


class ReplayKeyboardMarkup:
    def __init__(self, keyboard, resize_keyboard=None, one_time_keyboard=None,
                 selective=None):
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    def encode(self):
        out = {'keyboard': self.keyboard}
        if self.resize_keyboard:
            out['resize_keyboard'] = self.resize_keyboard
        if self.one_time_keyboard:
            out['one_time_keyboard'] = self.one_time_keyboard

        return json.dumps(out)
