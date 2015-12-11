import json


class ReplayKeyboardMarkup:
    FIELD_KEYBOARD = 'keyboard'
    FIELD_RESIZEKEYBOARD = 'resize_keyboard'
    FIELD_ONETIMEKEYBOARD = 'one_time_keyboard'

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

        return json.dumps(out)
