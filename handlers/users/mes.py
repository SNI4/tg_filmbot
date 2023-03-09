from aiogram import types

from data.FSMs.achoose import FSMCCCHOOSE
from data.FSMs.add_film import FSMAF
from data.FSMs.auto_add_channel import FSMAAC
from data.FSMs.cchoose import FSMCCHOOSE
from data.FSMs.del_film import FSMDF
from data.FSMs.fchoose import FSMCHOOSE
from data.FSMs.search_film import FSMSF
from handlers.users.show_film import film
from handlers.users.start import start
from keyboards.admin_keyboards.add_film_code import film_code_choose
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.admins_actions import create_admins_action
from keyboards.admin_keyboards.channels_action import create_channels_action
from keyboards.admin_keyboards.films_action import create_films_action
from keyboards.admin_keyboards.random_code import create_random_code
from keyboards.cancel_reply import create_cancel
from keyboards.user_keyboards.default_reply import create_default
from keyboards.user_keyboards.film_link import create_film_link
from keyboards.user_keyboards.subscribe_channels import create_subscribe
from loader import dp
from utils.json_worker.films import get_films
from utils.misc.get_keyboard import choose_keyboard
from utils.misc.get_stars import get_stars
from utils.misc.isAdmin import isAdmin
from utils.misc.isUser import isUser
from utils.misc.markreplace import markdowned
from utils.validate_subscribes import validate_user


@dp.message_handler()
async def message_handle(message: types.Message):
    user_id = str(message.from_id)
    m = message.text.lower()

    if (m == "фильмы") and (await isAdmin(user_id)):
        await message.reply("Выберите:",
                            reply_markup=create_films_action())
        await FSMCHOOSE.choose.set()

    elif (m == "рекламные каналы") and (await isAdmin(user_id)):
        await message.reply("Выберите:",
                            reply_markup=create_channels_action())
        await FSMCCHOOSE.choose.set()

    elif (m == "админы") and (await isAdmin(user_id)):
        await message.reply("Выберите:",
                            reply_markup=create_admins_action())
        await FSMCCCHOOSE.choose.set()

    elif m == "найти по описанию":
        await message.reply("введите поавл")
        await FSMSF.search.set()

    elif (m == "✅") and (not await isUser(user_id)):
        res = await validate_user(user_id, message.from_user.username)
        await message.reply('success' if res else 'error')

    elif m.isdigit():
        await film(message, m, user_id)
        await message.reply(get_stars(int(message.text)))

    elif m == "найти по коду":
        await message.answer("Для того чтобы найти фильм, просто отправьте мне его код.")

    else:
        if await isUser(user_id):
            await message.reply(await markdowned('Я вас *не понял*.'),
                                reply_markup=await choose_keyboard(user_id),
                                parse_mode='MarkdownV2')

        else:
            await start(message)