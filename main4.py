from telethon.sync import TelegramClient

# Замените на ваши данные
API_ID = 23947968
API_HASH = '22084828a6dd26359a937364cf9e5074'
PHONE_NUMBER = '+79375511073'

with TelegramClient('anon', API_ID, API_HASH) as client:
    username = 'MingHamill'
    print('yo')
    user = client.get_entity(username)
    print(user)

    if user:
        # Отправьте сообщение пользователю
        message = f'Привет, @{username}! Это сообщение отправлено через Telethon.'
        client.send_message(user, message)
    else:
        print(f'Пользователь {username} не найден.')
