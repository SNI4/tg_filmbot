from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_film_link(url: bool = False, link: str = "", user_id: str = "") -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1, )
    ib1 = InlineKeyboardButton(text="Смотреть бесплатно", url=link)
    ib2 = InlineKeyboardButton(text="Меню", callback_data=f"cancel?{user_id}")
    ikb.add(ib2)
    return ikb.add(ib1) if url else ikb
