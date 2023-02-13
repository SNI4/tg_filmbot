from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def create_checkbox(string: str) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)

    ib1 = InlineKeyboardButton(text="✅",
                               callback_data=f"ck-{string}"
                               )

    return ikb.add(ib1)