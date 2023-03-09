from aiogram.dispatcher import FSMContext

from data.config import ADMIN_ID
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.delete_admin_confirm_inline import create_add_admin
from loader import dp, bot
from aiogram import types
from data.FSMs.add_admin import FSMAD
from utils.json_worker.users import add_user, give_admin, get_users
from utils.misc.get_keyboard import choose_keyboard
from utils.misc.isAdmin import isAdmin
from utils.misc.isUser import isUser


@dp.message_handler(state=FSMAD.user_id)
async def adding_admin(message: types.Message, state: FSMContext):
    user_id = str(message.forward_from.id) if message.forward_from else message.text

    if message.text.lower() == "отмена":
        await message.reply('qq', reply_markup=create_admin_default())
        await state.finish()

    elif await isAdmin(user_id) or not await isUser(user_id):
        await message.reply("Ошибка! \nлибо уже админ\nлибо неверный id\nлибо не зарегестрирован в боте")
        await state.finish()

    else:
        data = await get_users()
        await message.reply(f"Вы выбрали пользователя @{data[user_id]['username']}")
        await state.update_data(user_id=user_id)
        await message.answer("Confirm?")
        await FSMAD.confirm.set()


@dp.message_handler(state=FSMAD.confirm)
async def add_admin_confirm(message: types.message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.reply('qq', await choose_keyboard(str(message.from_id)))
        await state.finish()

    elif message.text is not None and message.text.lower() == "yes":
        adm_user_id = (await state.get_data())['user_id']
        adm_username = (await get_users())[adm_user_id]['username']
        await bot.send_message(chat_id=ADMIN_ID,
                               text=f"подтвердите добавление админа @{adm_username}",
                               reply_markup=create_add_admin(user_id=adm_user_id,
                                                             sender_user_id=str(message.from_id)))
        await message.reply('отправлено на проверку', reply_markup=create_admin_default())
        await state.finish()
    else:
        await message.reply('cancelled', reply_markup=create_admin_default())
        await state.finish()
