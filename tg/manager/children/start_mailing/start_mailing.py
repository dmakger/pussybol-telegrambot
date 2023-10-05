from telebot import TeleBot

from tg.data import START_MAILING_BUTTON
from tg.manager.core.manager import Manager


class StartMailingManager(Manager):
    this = START_MAILING_BUTTON
    # children = [ParsingManager]

    def __init__(self, bot: TeleBot, message=None, parent=None, handler=None):
        super().__init__(
            bot=bot,
            message=message,
            handler=handler,
            level=1,
            parent=parent,
            this=self.this,
            children=self.children,
        )
        # print(self.parent)
