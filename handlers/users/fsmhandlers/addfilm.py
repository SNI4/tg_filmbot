from aiogram import types

from aiogram.dispatcher import FSMContext
from random import randint
from data.FSMs.add_film import FSMAF
from data.FSMs.auto_add_channel import FSMAAC
from data.FSMs.fchoose import FSMCHOOSE
from data.FSMs.manual_add_channel import FSMMAC
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.films_action import create_films_action
from keyboards.admin_keyboards.save_reply import create_save
from keyboards.cancel_inline import create_cancel_inline
from keyboards.cancel_reply import create_cancel
from keyboards.user_keyboards.default_reply import create_default
from loader import dp
from utils.json_worker.channels import add_channel, DublicateChannelError
from utils.json_worker.films import get_films, save_film
from utils.misc.markreplace import markdowned


@dp.message_handler(state=FSMAF.code)
async def get_film_code(message: types.Message, state: FSMContext):
    try:
        if message.text.isdigit() and int(message.text) <= 9999:
            if message.text in (await get_films()).keys(): raise Exception
            await state.update_data(code=message.text)
            await message.answer(await markdowned(f"Код фильма: *{message.text}*"),
                                 parse_mode="MarkdownV2")
            await message.reply('Теперь введите *название* фильма',
                                reply_markup=create_cancel(),
                                parse_mode="MarkdownV2")
            await FSMAF.name.set()

        elif message.text is not None and message.text.lower() == "случайный код":
            codes = (await get_films()).keys()
            code = str(randint(1, 9999))
            while code in codes: code = str(randint(1, 9999))

            await state.update_data(code=code)
            await message.answer(await markdowned(f"Код фильма: *{code}*"),
                                 parse_mode="MarkdownV2")
            await message.reply(await markdowned('Теперь введите *название* фильма'), reply_markup=create_cancel(),
                                parse_mode="MarkdownV2")
            await FSMAF.name.set()

        elif message.text is not None and message.text.lower() == "отмена":
            await state.finish()
            await message.reply("*Отменено*",
                                parse_mode="MarkdownV2")
            await message.answer("Выберите:",
                                 reply_markup=create_films_action())
            await FSMCHOOSE.choose.set()
        else:
            await message.reply(await markdowned("Введите *четырехзначное число*!"),
                                reply_markup=create_cancel(),
                                parse_mode="MarkdownV2")

    except Exception as e:
        await message.reply(await markdowned(f"*Произошла ошибка!*\n||{str(e)}||"),
                            parse_mode="MarkdownV2")


@dp.message_handler(state=FSMAF.name)
async def get_film_title(message: types.Message, state: FSMContext):
    try:
        if message.text.lower() == "отмена":
            await state.finish()
            await message.reply("*Отменено*",
                                parse_mode="MarkdownV2")
            await message.answer("Выберите:",
                                 reply_markup=create_films_action())
            await FSMCHOOSE.choose.set()

        else:
            await state.update_data(name=message.text)
            data = await state.get_data()
            await message.answer(await markdowned(f"Код фильма: *{data['code']}*\n"
                                                  f"Название фильма: *{data['name']}*"),
                                 parse_mode="MarkdownV2")
            await message.reply("Теперь отправьте *обложку* фильма",
                                reply_markup=create_cancel(),
                                parse_mode="MarkdownV2")
            await FSMAF.media.set()
    except Exception as e:
        await message.reply(await markdowned("Это не *текст*!"),
                            reply_markup=create_cancel(),
                            parse_mode="MarkdownV2")
        print(e)


@dp.message_handler(state=FSMAF.media, content_types=['any'])
async def get_film_media(message: types.Message, state: FSMContext):
    if message.photo:
        photo_id = message.photo[-1].file_id
        await state.update_data(media=photo_id)
        data = await state.get_data()
        await message.answer_photo(
            caption=await markdowned(f"Код фильма: *{data['code']}*\n"
                                     f"Название фильма: *{data['name']}*"),
            photo=data['media'], parse_mode="MarkdownV2")
        await message.reply("Теперь отправьте *описание* фильма",
                            reply_markup=create_cancel(),
                            parse_mode="MarkdownV2")
        await FSMAF.desc.set()

    elif message.text is not None and message.text.lower() == "отмена":
        await state.finish()
        await message.reply("*Отменено*",
                            parse_mode="MarkdownV2")
        await message.answer("Выберите:",
                             reply_markup=create_films_action())
        await FSMCHOOSE.choose.set()

    else:
        await message.answer(await markdowned('Отправьте *фото*!'),
                             reply_markup=create_cancel(),
                             parse_mode="MarkdownV2")


@dp.message_handler(state=FSMAF.desc)
async def get_film_description(message: types.Message, state: FSMContext):
    if message.text is not None and message.text.lower() == "отмена":
        await state.finish()
        await message.reply("*Отменено*",
                            parse_mode="MarkdownV2")
        await message.answer("Выберите:",
                             reply_markup=create_films_action())
        await FSMCHOOSE.choose.set()

    else:
        await state.update_data(desc=message.text)
        data = await state.get_data()
        await message.answer_photo(caption=await markdowned(f"Код фильма: *{data['code']}*\n"
                                                            f"Название фильма: *{data['name']}*\n"
                                                            f"Описание фильма: *{data['desc']}*"),
                                   photo=data['media'], parse_mode="MarkdownV2")
        await message.reply(await markdowned("Теперь отправьте *ссылку для просмотра фильма*"
                                             "\n||Если таковой не имеется, то отправьте "
                                             "что угодно. Ссылка проверяется по||"),
                            reply_markup=create_cancel(),
                            parse_mode="MarkdownV2")
        await FSMAF.link.set()


@dp.message_handler(state=FSMAF.link)
async def get_film_link(message: types.Message, state: FSMContext):
    if message.text is not None and message.text.lower() == "отмена":
        await state.finish()
        await message.reply("*Отменено*",
                            parse_mode="MarkdownV2")
        await message.answer("Выберите:",
                             reply_markup=create_films_action())
        await FSMCHOOSE.choose.set()

    elif message.text is not None:
        if "https://" in message.text:
            await state.update_data(link=message.text)
            data = await state.get_data()
            await message.answer_photo(caption=await markdowned(f"Код фильма: *{data['code']}*\n"
                                                                f"Название фильма: *{data['name']}*"
                                                                f"Описание фильма: *{data['desc']}*"
                                                                f"Ссылка на фильм: "
                                                                f"||P.S. Ссылка будет в виде *кнопки*||"),
                                       photo=data['media'],
                                       parse_mode="MarkdownV2")

            await message.reply("Сохраняем?",
                                reply_markup=create_save())
            await FSMAF.confirm.set()

        else:
            await state.update_data(link="nolink")
            data = await state.get_data()
            m = await message.answer_photo(caption=await markdowned(f"Код фильма: *{data['code']}*\n"
                                                                    f"Название фильма: *{data['name']}*\n"
                                                                    f"Описание фильма: *{data['desc']}*\n"),
                                           photo=data['media'],
                                           parse_mode="MarkdownV2")

            await m.reply("Сохраняем?", reply_markup=create_save())
            await FSMAF.confirm.set()
    else:
        await message.reply("Ты отправил какую то *хуйню*! Попробуй еще раз.",
                            reply_markup=create_cancel(),
                            parse_mode="MarkdownV2")


@dp.message_handler(state=FSMAF.confirm)
async def get_confirmation(message: types.Message, state: FSMContext):
    if message.text is not None and message.text.lower() == "сохранить":
        try:
            data = await state.get_data()
            await save_film(code=data['code'], title=data['name'], media_id=data['media'],
                            desc=data['desc'], link=data['link'])
            await message.reply(await markdowned(f"Фильм *{data['name']}* успешно *добавлен!*"),
                                parse_mode="MarkdownV2")
            await message.answer("*Добро пожаловать*",
                                 reply_markup=create_admin_default(),
                                 parse_mode="MarkdownV2")
            await state.finish()

        except Exception as e:
            await message.reply(await markdowned(f"*Произошла ошибка!*\n||{str(e)}||"),
                                parse_mode="MarkdownV2")

    elif message.text is not None and message.text.lower() == "выход":
        await state.finish()
        await message.reply("*Отменено*",
                            parse_mode="MarkdownV2")
        await message.answer("Выберите:",
                             reply_markup=create_films_action())
        await FSMCHOOSE.choose.set()
    else:
        await message.reply(await markdowned("Ты отправил какую то *хуйню*! Попробуй еще раз."),
                            reply_markup=create_cancel(), parse_mode="MarkdownV2")
