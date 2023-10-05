from telebot import TeleBot

from tg.data import ADD_MAMMOTH_BUTTON
from tg.manager.children.add_mammoth.children.parsing.parsing_manager import ParsingManager
from tg.manager.core.manager import Manager


class AddMammothManager(Manager):
    this = ADD_MAMMOTH_BUTTON
    children = [ParsingManager]

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
