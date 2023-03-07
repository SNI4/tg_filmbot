from aiogram.dispatcher import FSMContext

from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from loader import dp
from aiogram import types
from data.FSMs.add_admin import FSMAD
from utils.json_worker.users import add_user, give_admin, get_users
from utils.misc.get_keyboard import choose_keyboard
from utils.misc.isAdmin import isAdmin
from utils.misc.isUser import isUser


@dp.message_handler(state=FSMAD.user_id)
async def adding_admin(message: types.Message, state: FSMContext):
    user_id = str(message.forward_from.id) if message.forward_from else message.text

    if await isAdmin(user_id):
        await message.reply("Этот пользователь уже является администратором!")
        await state.finish()

    elif not await isUser(user_id):
        await message.reply("Этот пользователь не зарегестрирован в боте!")
        await state.finish()

    else:
        data = await get_users()
        await message.reply(f"Вы выбрали пользователя {data[user_id]['username']}")
        await state.update_data(user_id=user_id)
        await message.answer("Confirm?")
        await FSMAD.confirm.set()


@dp.message_handler(state=FSMAD.confirm)
async def add_admin_confirm(message: types.message, state: FSMContext):
    if message.text is not None and message.text.lower() == "yes":
        data = await state.get_data()
        await give_admin(user_id=data['user_id'])
        await message.reply('success!', reply_markup=create_admin_default())
        await state.finish()

    else:
        await message.reply('cancelled', reply_markup=create_admin_default())
        await state.finish()
