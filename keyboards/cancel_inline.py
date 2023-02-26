from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_cancel_inline() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton(text="Выйти", callback_data="cancel")
    ikb.add(ib1)
    return ikb
