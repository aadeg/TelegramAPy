import json


class ReplayKeyboardHide:
    FIELD_HIDEKEYBOARD = 'hide_keyboard'
    FIELD_SELECTIVE = 'selective'

    def __init__(self, hide_keyboard, selective=None):
        self.hide_keyboard = hide_keyboard
        self.selective = selective

    def encode(self):
        out = {ReplayKeyboardHide.FIELD_HIDEKEYBOARD: self.hide_keyboard}
        if self.selective:
            out[ReplayKeyboardHide.FIELD_SELECTIVE] = self.selective

        return json.dumps(out)
