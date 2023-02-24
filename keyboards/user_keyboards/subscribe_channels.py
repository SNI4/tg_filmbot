from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.json_worker.channels import get_channels


async def create_subscribe():
    ikb = InlineKeyboardMarkup(row_width=1)
    data = await get_channels()
    for channel_id in data.keys():
        ikb.add(InlineKeyboardButton(text=data[channel_id]['title'], url=data[channel_id]['link']))

    return ikb
