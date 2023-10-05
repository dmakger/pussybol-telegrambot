from telebot import TeleBot, types

from tg.data import BACK_BUTTON
from tg.manager.core.manager_handler import ManagerHandler


class Manager:
    # parent = None
    this = None
    children = []

    def __init__(self, bot: TeleBot, message=None, title=None, parent=None, this=None, children=None, level: int = 0,
                 handler: ManagerHandler = None):
        if children is None:
            children = []
        self.handler = handler
        self.bot = bot
        self.message = message
        self.title = title
        self.parent = parent
        self.this = this
        self.children = children
        self.level = level

    def get_message(self, message):
        if message is not None:
            return message
        return self.message

    def get_title(self, title):
        if title is not None:
            return title
        if self.this is not None:
            return self.this.response
        if self.title is not None:
            return self.title
        return 'Кнопка'

    # Отобразить кнопки
    def show(self, message=None, title=None):
        message = self.get_message(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*[manager.this.button for manager in self.children])
        if self.level > 0:
            markup.add(BACK_BUTTON.button)
        if message:
            self.bot.send_message(message.chat.id, text=self.get_title(title), reply_markup=markup)

    # Прослушка текущего текста

    def pre_process_message(self, message):
        message = self.get_message(message)
        exists = self.get_message(message)
        return message, exists

    def process_message(self, message, exists):
        for manager in self.children:
            if message.text == manager.this.title:
                exists = True
                child = manager(bot=self.bot, message=message, parent=self.handler.get_manager(), handler=self.handler)
                self.handler.set_manager(child)
                child.show()
                break
        return message, exists

    def post_process_message(self, message, exists):
        if message.text == BACK_BUTTON.title:
            self.back(message)
        if not exists:
            self.error(message)

    def text_handler(self, message):
        message, exists = self.pre_process_message(message)
        message, exists = self.process_message(message, exists)
        self.post_process_message(message, exists)

    # Вернуться назад
    def back(self, message):
        if self.level > 0:
            self.level -= 1
        if self.parent:
            self.handler.set_manager(self.parent)
            self.parent.show(title=BACK_BUTTON.response)

    # Вызов ошибки
    def error(self, message=None):
        message = self.get_message(message)
        self.bot.send_message(message.chat.id, text="Не пон")
        self.show()
