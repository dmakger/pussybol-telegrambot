import telebot

import config
from tg.manager.core.manager_handler import ManagerHandler
from tg.manager.start_manager import StartManager

bot = telebot.TeleBot(config.token)
# manager = StartManager(bot=bot)
manager_handler = ManagerHandler(StartManager(bot=bot))
manager_handler.manager.handler = manager_handler
level = 0


@bot.message_handler(commands=['start'])
def start(message):
    manager_handler.get_manager().message = message
    manager_handler.get_manager().show(message)


@bot.message_handler(content_types=['text'])
def func(message):
    manager_handler.get_manager().text_handler(message)


bot.polling(none_stop=True)
