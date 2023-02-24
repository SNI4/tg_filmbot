from aiogram import types

from keyboards.user_keyboards.checkbox_inline import create_checkbox
from keyboards.user_keyboards.subscribe_channels import create_subscribe
from loader import dp
from utils.misc.isAdmin import isAdmin
from utils.json_worker.users import *
from utils.misc.isUser import isUser


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not await isAdmin(str(message.from_id)):
        if not await isUser(str(message.from_id)):
            await message.reply('Чтобы начать пользоваться ботом, ты должен подпиcаться на ↓эти↓ каналы', reply_markup=await create_subscribe())
            await message.reply('Нажми на кнопку, когда будешь готов продолжить', reply_markup=create_checkbox())

        else:
            pass

    else:
        pass
