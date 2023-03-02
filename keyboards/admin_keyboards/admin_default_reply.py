from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_admin_default():
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    ib1 = KeyboardButton(text='Рекламные каналы')
    ib2 = KeyboardButton(text='Фильмы')

    ikb.add(ib1).add(ib2)
    return ikb
