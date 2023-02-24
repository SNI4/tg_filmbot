from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_checkbox() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True)

    ib1 = KeyboardButton(text="✅")

    return ikb.add(ib1)