from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_admin_default():
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    ib1 = KeyboardButton(text='Добавить канал')
    ib2 = KeyboardButton(text='Удалить канал')
    ib3 = KeyboardButton(text='Добавить фильм')

    ikb.add(ib1).add(ib2).add(ib3)

    return ikb
