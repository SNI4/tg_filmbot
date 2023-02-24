from aiogram import types

from data.FSMs.auto_add_channel import FSMAAC
from keyboards.cancel_reply import create_cancel
from loader import dp
from utils.misc.isAdmin import isAdmin
from utils.misc.isUser import isUser
from utils.validate_subscribes import validate_user


@dp.message_handler(content_types=['any'])
async def message_handle(message: types.Message):
    user_id = str(message.from_id)
    m = message.text.lower()

    if (m == "добавить канал") and (await isAdmin(user_id)):
        await message.reply("Перешлите сообщение из канала, который хотите добавить.", reply_markup=create_cancel())
        await FSMAAC.AddChannel.set()

    elif (m == "✅") and (not await isAdmin(user_id)):
        if not await isUser(user_id):
            res = await validate_user(user_id, message.from_user.username)
            await message.reply('success' if res else 'error')
    else:
        await message.reply("123")

