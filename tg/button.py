from telebot import types


class Button:
    def __init__(self, title=None, response=''):
        self.title = None
        self.button = None
        self.response = response

        if title is not None:
            self.title = title
            self.button = types.KeyboardButton(self.title)

    def __str__(self):
        return self.title
