from aiogram import types

from data.FSMs.add_film import FSMAF
from data.FSMs.auto_add_channel import FSMAAC
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.random_code import create_random_code
from keyboards.cancel_reply import create_cancel
from keyboards.user_keyboards.default_reply import create_default
from keyboards.user_keyboards.subscribe_channels import create_subscribe
from loader import dp
from utils.misc.isAdmin import isAdmin
from utils.misc.isUser import isUser
from utils.misc.markreplace import markdowned
from utils.validate_subscribes import validate_user


@dp.message_handler()
async def message_handle(message: types.Message):
    user_id = str(message.from_id)
    m = message.text.lower()

    if (m == "добавить канал") and (await isAdmin(user_id)):
        await message.reply("Перешлите сообщение из канала, который хотите добавить.", reply_markup=create_cancel())
        await FSMAAC.AddChannel.set()

    elif (m == "добавить фильм") and (await isAdmin(user_id)):
        await message.reply('Введите код, который хотите присвоить новому фильму\n||*Не более 4 цифр*||',
                            reply_markup=await create_random_code(),
                            parse_mode="MarkdownV2")
        await FSMAF.code.set()

    elif (m == "удалить канал") and (await isAdmin(user_id)):
        await message.reply("Выберите канал, который хотите убрать",
                            reply_markup=await create_subscribe(url=False, cancel=True))

    elif (m == "✅") and (not await isAdmin(user_id)):
        if not await isUser(user_id):
            res = await validate_user(user_id, message.from_user.username)
            await message.reply('success' if res else 'error')
    else:
        await message.reply(await markdowned('Я вас *не понял*.'),
                            reply_markup=create_default() if not await isAdmin(user_id) else create_admin_default(),
                            parse_mode='MarkdownV2')

