from telebot import TeleBot

from tg.manager.children.add_mammoth.add_mammoth_manager import AddMammothManager
from tg.manager.children.add_succub.add_succub import AddSuccubManager
from tg.manager.children.start_mailing.start_mailing import StartMailingManager
from tg.manager.core.manager import Manager


class StartManager(Manager):
    children = [AddMammothManager, StartMailingManager, AddSuccubManager]

    def __init__(self, bot: TeleBot, message=None, parent=None, handler=None):
        super().__init__(
            bot,
            level=0,
            handler=handler,
            parent=parent,
            children=self.children,
            title="Я бот pussybol, могу наpussybolить любому",
            message=message
        )
