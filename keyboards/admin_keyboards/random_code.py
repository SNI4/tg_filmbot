from random import randint
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.json_worker.films import get_films


async def create_random_code(cancel: bool = True) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    code = randint(1, 9999)
    while code in (await get_films()).keys():
        code = randint(1, 9999)
    if cancel: ikb.add(InlineKeyboardButton(text='Выйти', callback_data='cancel'))
    ikb.add(InlineKeyboardButton(text="Случайный код", callback_data='rk?'+str(code)))
    return ikb
