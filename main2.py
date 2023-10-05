import asyncio

from telethon.sync import TelegramClient

# Замените на ваши данные
API_ID = 23947968
API_HASH = '22084828a6dd26359a937364cf9e5074'
# BOT_TOKEN = '5905462454:AAGsOFWGpMNll3uBk0qT4bfuICxR19bi14Y'
PHONE_NUMBER = '+79375511073'


async def main():
    client = TelegramClient(str(API_ID), API_ID, API_HASH)
    await client.start()
    assert await client.connect()
    if not client.is_user_authorized():
        await client.send_code_request(PHONE_NUMBER)
        me = await client.sign_in(PHONE_NUMBER, input('Enter code: '))
        print(me)


if __name__ == '__main__':
    asyncio.run(main())
