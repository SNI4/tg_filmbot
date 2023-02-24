from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_admin_default():
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    ib1 = KeyboardButton(text='?')

    ikb.add(ib1)