from aiogram import types
from aiogram.dispatcher import FSMContext
from data.FSMs.del_film import FSMDF
from data.FSMs.fchoose import FSMCHOOSE
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.films_action import create_films_action
from keyboards.cancel_reply import create_cancel
from loader import dp
from utils.json_worker.films import get_films
from utils.json_worker.films import delete_film
from utils.misc.markreplace import markdowned


@dp.message_handler(state=FSMDF.code)
async def get_delete_film(message: types.Message, state: FSMContext):
    try:
        if message.text is not None and message.text.lower() == "отмена":
            await message.reply('Отменено')
            await state.finish()
            await message.answer(await markdowned("Выберите"),
                                 reply_markup=create_films_action(),
                                 parse_mode="MarkdownV2")
            await FSMCHOOSE.choose.set()

        else:
            film_title = (await get_films())[message.text]['title']
            await delete_film(code=message.text)
            await message.reply(await markdowned(f"Фильм *{film_title}* успешно удален!"), parse_mode="MarkdownV2")
            await state.finish()
            await message.answer(await markdowned("Добро пожаловать!"),
                                 reply_markup=create_admin_default(),
                                 parse_mode="MarkdownV2")

    except:
        await message.reply(await markdowned("Фильма с таким кодом *не существует!*"),
                            reply_markup=create_cancel(),
                            parse_mode="MarkdownV2")
