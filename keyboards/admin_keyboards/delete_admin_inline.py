from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.json_worker.users import get_admins


def admins_to_delete(admins: dict, sender_user_id: str):
    ikb = InlineKeyboardMarkup()
    for admin_id in admins.keys():
        ikb.add(InlineKeyboardMarkup(text=admins[admin_id]['username'], callback_data=f"da?{admin_id}?{sender_user_id}"))

    return ikb
