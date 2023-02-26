from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_save():
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text="Сохранить")
    ib2 = KeyboardButton(text="Выйти")
    ikb.add(ib1).row(ib2)
    return ikb
