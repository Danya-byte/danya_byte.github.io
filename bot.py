import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *


# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен вашего бота
BOT_TOKEN = '6800248117:AAGbDUNTAQI9WYPlttw5hGSdUMUqh5SJ9LU'


def start(bot, update):
    keyboard = [
        [InlineKeyboardButton("Поиск фильмов",
                              url="https://danya-byte.github.io/danya_byte.github.io/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Я бот для поиска фильмов. Используй кнопку ниже для поиска.', reply_markup=reply_markup)


def main():
    updater = Updater(BOT_TOKEN, use_context=False)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
