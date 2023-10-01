# import telebot
from telethon.sync import TelegramClient


# Замените на ваши данные
API_ID = 23947968
API_HASH = '22084828a6dd26359a937364cf9e5074'
# BOT_TOKEN = '5905462454:AAGsOFWGpMNll3uBk0qT4bfuICxR19bi14Y'
PHONE_NUMBER = '+79375511073'

# bot = telebot.TeleBot(BOT_TOKEN)


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Я бот, созданный с использованием Telegram API.")


with TelegramClient('my_session', API_ID, API_HASH) as client:
    # Найдите ID пользователя @wserf
    username = 'dmakger'
    user = client.get_entity(username)
    print(user)

    if user:
        # Отправьте сообщение пользователю
        message = f'Привет, @{username}! Это сообщение отправлено через Telethon.'
        client.send_message(user, message)
    else:
        print(f'Пользователь {username} не найден.')


# bot.polling()
