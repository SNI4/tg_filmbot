import re
from aiogram import types

from keyboards.user_keyboards.default_reply import create_default
from loader import dp, bot
from utils.json_worker.channels import get_channels, add_channel_sub
from utils.json_worker.users import add_user


async def validate_user(user_id: str, username: str) -> bool:
    subscribed_channels = 0
    for channel_id in (await get_channels()).keys():
        ucs = re.findall(r"\w*", str(await bot.get_chat_member(chat_id=channel_id, user_id=user_id)))

        try:
            if ucs[70] != 'left': subscribed_channels += 1
            await add_channel_sub(channel_id)

        except:
            if ucs[60] != 'left': subscribed_channels += 1
            await add_channel_sub(channel_id)

    if subscribed_channels == len((await get_channels()).keys()):
        await add_user(user_id=user_id, username=username)
        return True

    else: return False
