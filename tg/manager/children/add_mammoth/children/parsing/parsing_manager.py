from telebot import TeleBot

from tg.data import PARSING_BUTTON, BACK_BUTTON
from tg.manager.core.manager import Manager


class ParsingManager(Manager):
    this = PARSING_BUTTON

    def __init__(self, bot: TeleBot, message=None, parent=None, handler=None):
        super().__init__(
            bot=bot,
            message=message,
            handler=handler,
            level=2,
            parent=parent,
            this=self.this,
        )
        self.chats = []
        self.error_text = None

    def process_message(self, message, exists, **kwargs):
        exists = self.action(message, exists)
        return message, exists

    def action(self, message, exists):
        exists = self.parsing_text(message, exists)
        print(self.chats)
        return exists


    def parsing_text(self, message, exists):
        if message.text == BACK_BUTTON.title:
            return exists

        error_group = []
        for chat in message.text.split():
            print(chat)
            try:
                self.chats.append(self.bot.get_chat(chat))
            except Exception as e:
                print(e)
                error_group.append(chat)

        if len(error_group) != 0:
            exists = False
            self.error_text = f"Я не нашел такие группы: {','.join(error_group)}"
        return exists
