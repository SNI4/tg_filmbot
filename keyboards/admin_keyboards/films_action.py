from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_films_action() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text="Добавить фильм")
    ib2 = KeyboardButton(text="Удалить фильм")
    ib3 = KeyboardButton(text="Отмена")
    ikb.row(ib1, ib2).add(ib3)
    return ikb
