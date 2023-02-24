from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.json_worker.channels import get_channels


async def create_subscribe(url: bool = True, cancel: bool = False) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    data = await get_channels()
    for channel_id in data.keys():
        if url: ikb.add(InlineKeyboardButton(text=data[channel_id]['title'], url=data[channel_id]['link']))
        else: ikb.add(InlineKeyboardButton(text=data[channel_id]['title'],
                                           callback_data='cd?'+channel_id))

    if cancel: ikb.add(InlineKeyboardButton(text='Выйти', callback_data='cancel'))
    return ikb
