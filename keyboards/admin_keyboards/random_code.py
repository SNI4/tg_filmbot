from random import randint
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_random_code(codes) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=2)
    code = randint(1, 9999)
    while code in codes:
        code = randint(1, 9999)
    ikb.add(InlineKeyboardButton(text="Случайный код", callback_data='rk?'+str(code)))
    ikb.add(InlineKeyboardButton(text="Ввести код вручную", callback_data='manualcode'))
    return ikb
