from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_channels_action() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text="Добавить канал")
    ib2 = KeyboardButton(text="Удалить канал")
    ib3 = KeyboardButton(text="Отмена")
    ikb.row(ib1, ib2).add(ib3)
    return ikb