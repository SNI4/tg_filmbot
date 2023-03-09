from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_deleted_admin(user_id: str, sender_user_id: str):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text="Подтвердить", callback_data=f"qwc?{user_id}?{sender_user_id}")
    ib2 = InlineKeyboardButton(text="Отклонить", callback_data=f"qwd?{user_id}?{sender_user_id}")
    return ikb.add(ib1, ib2)


def create_add_admin(user_id: str, sender_user_id: str):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text="Подтвердить", callback_data=f"Aadd?{user_id}?{sender_user_id}")
    ib2 = InlineKeyboardButton(text="Отклонить", callback_data=f"Adec?{user_id}?{sender_user_id}")
    return ikb.add(ib1, ib2)

