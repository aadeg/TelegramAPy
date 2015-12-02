from telegram.exception import ObjectDecodingException


class ReplayKeyboardHide:
    def __init__(self, hide_keyboard, selective=None):
        self.hide_keyboard = hide_keyboard
        self.selective = selective

    @staticmethod
    def decode(j):
        try:
            obj = ReplayKeyboardHide(j['hide_keyboard'])
            if 'selective' in j:
                obj.selective = j['selective']
        except KeyError:
            raise ObjectDecodingException("ReplayKeyboardHide", j)

        return obj
