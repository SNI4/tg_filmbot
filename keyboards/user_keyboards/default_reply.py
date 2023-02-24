from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_default():
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    ib1 = KeyboardButton(text='?')

    ikb.add(ib1)

    return ikb