from telegram.exception import ObjectDecodingException


class ReplayKeyboardMarkup:
    def __init__(self, keyboard, resize_keyboard=None, one_time_keyboard=None,
                 selective=None):
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    @staticmethod
    def decode(j):
        try:
            obj = ReplayKeyboardMarkup(j['keyboard'])
            if 'resize_keyboard' in j:
                obj.resize_keyboard = j['resize_keyboard']
            if 'one_time_keyboard' in j:
                obj.one_time_keyboard = j['one_time_keyboard']
            if 'selective' in j:
                obj.selective = j['selective']
        except KeyError:
            raise ObjectDecodingException("ReplayKeyboardMarkup", j)

        return obj
