from aiogram import types

from keyboards.user_keyboards.checkbox_inline import create_checkbox
from keyboards.user_keyboards.subscribe_channels import create_subscribe
from loader import dp
from utils.json_worker.channels import get_channels
from utils.json_worker.users import add_user
from utils.misc.get_keyboard import choose_keyboard
from utils.misc.isAdmin import isAdmin
from utils.misc.isUser import isUser


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not await isAdmin(str(message.from_id)):
        if not await isUser(str(message.from_id)):
            if len((await get_channels()).keys()) > 0:
                await message.reply('Чтобы начать пользоваться ботом, ты должен подпиcаться на ↓эти↓ каналы',
                                    reply_markup=await create_subscribe())
                await message.answer('Нажми на кнопку, когда будешь готов продолжить',
                                     reply_markup=create_checkbox())
            else:
                await add_user(user_id=str(message.from_id), username=message.from_user.username)
                await message.reply("Вы успешно зарегестрированы!",
                                    reply_markup=await choose_keyboard(str(message.from_id)))

        else:
            pass

    else:
        pass
