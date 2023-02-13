import re
from aiogram import types
from loader import dp, bot
from utils.json_worker.channels import get_channels
from utils.json_worker.users import add_user


@dp.callback_query_handler()
async def admin_vote_callback(callback: types.CallbackQuery):
    if callback.data.startswith('ck'):
        subscribed_channels = 0
        for channel_id in (await get_channels()).keys():
            ucs = re.findall(r"\w*", str(await bot.get_chat_member(chat_id=channel_id, user_id=callback.from_user.id)))

            try:
                if ucs[70] != 'left': subscribed_channels += 1
            except:
                if ucs[60] != 'left': subscribed_channels += 1

        if subscribed_channels == len((await get_channels()).keys()):
            await add_user(user_id=str(callback.message.from_user.id), username=callback.message.from_user.username)
            await callback.message.reply("Успешно", reply_markup=create_default())
