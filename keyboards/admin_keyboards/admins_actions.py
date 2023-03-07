from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_admins_action() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text="Добавить админа")
    ib2 = KeyboardButton(text="Удалить админа")
    ib3 = KeyboardButton(text="Отмена")
    ikb.row(ib1, ib2).add(ib3)
    return ikb
