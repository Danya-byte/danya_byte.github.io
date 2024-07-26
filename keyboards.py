from aiogram.types import WebAppInfo
from aiogram import types
from telebot import callback_data
from telebot.callback_data import CallbackData
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

web_app = WebAppInfo(url='https://danya-byte.github.io/danya_byte.github.io/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Site', web_app=web_app)]
    ],
    resize_keyboard=True
)
cb=CallbackData('btn', 'action')
key=InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton('Pay', callback_data='btn:buy')]]
)
