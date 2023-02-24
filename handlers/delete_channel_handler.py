import re
from aiogram import types
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.user_keyboards.subscribe_channels import create_subscribe
from loader import dp, bot
from utils.json_worker.channels import get_channels, add_channel_sub, del_channel
from utils.json_worker.users import add_user
from utils.misc.markreplace import markdowned


@dp.callback_query_handler()
async def admin_vote_callback(callback: types.CallbackQuery):
    if callback.data.startswith('cd'):
        try:
            data = await get_channels()
            channel_id = callback.data.split('?')[1]
            channel_title = data[channel_id]['title']
            await del_channel(channel_id)
            await callback.message.answer(await markdowned(f'Канал *{channel_title}* успешно удален!'),
                                          reply_markup=await create_subscribe(url=False, cancel=True),
                                          parse_mode="MarkdownV2")

        except Exception as e:
            await callback.message.reply('ERROR!\n' + str(e))

    elif callback.data == "cancel":
        await callback.message.reply('Добро пожаловать', reply_markup=create_admin_default())
