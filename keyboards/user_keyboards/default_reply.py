from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_default() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text="Найти по коду")
    ib2 = KeyboardButton(text="Найти по описанию")
    ikb.add(ib1, ib2)
    return ikb
