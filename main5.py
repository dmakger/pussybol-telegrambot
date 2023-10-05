import logging

import tg
from tg import Update
from tg.ext import filters, CommandHandler, CallbackContext, Application, MessageHandler

# Уровни разговора
from tg.data import BOT_TOKEN

REQUEST_TEXT = 1


# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    context.user_data.clear()
    await update.message.reply_text(
        f"Привет, {user.mention_html()}!\n\n"
        "Отправь мне текстовое сообщение, нажав на кнопку ниже.",
        reply_markup=tg.ForceReply(selective=True)
    )
    return REQUEST_TEXT


# Функция для получения текста
def get_text(update: Update, context: CallbackContext) -> int:
    user = update.effective_user
    text = update.message.text
    update.message.reply_text(
        f"Спасибо за ваш текст: {text}\n"
        f"Чтобы отправить еще текст, нажмите на кнопку ниже.",
        reply_markup=tg.ForceReply(selective=True)
    )
    return REQUEST_TEXT


# Функция для обработки ошибок
async def error(update: Update, context: CallbackContext):
    logging.error(f"Update {update} caused error {context.error}")


def main():
    # Инициализация бота
    # bot = Bot(token=BOT_TOKEN)
    #
    # update_queue = asyncio.Queue()
    # updater = Updater(bot=bot, update_queue=update_queue)

    # Получение диспетчера для регистрации обработчиков
    # dp = updater
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавление обработчиков команд
    application.add_handler(CommandHandler("start", start))

    # Добавление обработчика текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_text))

    # Добавление обработчика ошибок
    application.add_error_handler(error)

    # Запуск бота
    application.run_polling()


if __name__ == "__main__":
    main()
