from aiogram import types

from aiogram.dispatcher import FSMContext

from data.FSMs.add_film import FSMAF
from data.FSMs.auto_add_channel import FSMAAC
from data.FSMs.manual_add_channel import FSMMAC
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.cancel_inline import create_cancel_inline
from keyboards.cancel_reply import create_cancel
from keyboards.user_keyboards.default_reply import create_default
from loader import dp
from utils.json_worker.channels import add_channel, DublicateChannelError
from utils.json_worker.films import get_films
from utils.misc.markreplace import markdowned


@dp.message_handler(state=FSMAF.code)
async def get_film_code(message: types.Message, state: FSMContext):
    try:
        if message.text.isdigit() and int(message.text) <= 9999:
            if message.text in (await get_films()).keys(): raise Exception
            await state.update_data(code=message.text)
            await message.answer(await markdowned("Код фильма: " + message.text))
            await message.reply('Теперь введите название фильма', reply_markup=create_cancel_inline())
            await FSMAF.name.set()

    except:
        await message.reply(await markdowned("*Произошла ошибка!*\n||Возможно, вы ввели не *цифры*,"
                                             "либо фильм с таким кодом уже существует!||"),
                            parse_mode="MarkdownV2")
