from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_cancel() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text="Отмена")

    return ikb.add(ib1)