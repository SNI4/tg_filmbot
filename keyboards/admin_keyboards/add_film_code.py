from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def film_code_choose() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text="Случайный код")
    ib2 = KeyboardButton(text="Отмена")
    ikb.add(ib1, ib2)
    return ikb
