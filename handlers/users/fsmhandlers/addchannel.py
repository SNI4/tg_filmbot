from aiogram import types

from aiogram.dispatcher import FSMContext

from data.FSMs.auto_add_channel import FSMAAC
from data.FSMs.cchoose import FSMCCHOOSE
from data.FSMs.fchoose import FSMCHOOSE
from data.FSMs.manual_add_channel import FSMMAC
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.channels_action import create_channels_action
from keyboards.admin_keyboards.films_action import create_films_action
from keyboards.cancel_reply import create_cancel
from keyboards.user_keyboards.default_reply import create_default
from loader import dp
from utils.json_worker.channels import add_channel, DublicateChannelError
from utils.misc.markreplace import markdowned


@dp.message_handler(state=FSMAAC.AddChannel, content_types=['any'])
async def get_channel_to_add(message: types.Message, state: FSMContext):
    if message.text and message.text.lower() == "отмена":
        await message.reply("Отменено")
        await state.finish()
        await message.answer("Выберите:", reply_markup=create_channels_action())
        await FSMCCHOOSE.choose.set()

    elif message.forward_from_chat:
        if message.forward_from_chat.type == "channel":

            if not message.forward_from_chat.username:
                await message.reply('Не удалось получить ссылку на канал. Попробуйте вручную')
                await message.answer("Введите ID канала", reply_markup=create_cancel())
                await FSMMAC.id.set()

            else:
                try:
                    await add_channel(channel_id=str(message.forward_from_chat.id),
                                      title=message.forward_from_chat.title,
                                      username=message.forward_from_chat.username)

                    await message.reply(await markdowned(f"Канал *{message.forward_from_chat.title}* успешно добавлен!"),
                                        reply_markup=create_admin_default(),
                                        parse_mode="MarkdownV2")
                    await state.finish()

                except Exception as e:
                    await message.reply(f'ERROR!\n{e}',
                                        reply_markup=create_admin_default())

    else:
        await message.reply("Перешлите сообщение из канала!", reply_markup=create_cancel())


@dp.message_handler(state=FSMMAC.id)
async def manually_add_channel_id(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.reply("Отменено")
        await state.finish()
        await message.answer("Выберите:",
                             reply_markup=create_channels_action())
        await FSMCCHOOSE.choose.set()

    else:
        try:
            await state.update_data(id=message.text)
            await message.answer("ID Канала: " + message.text,
                                 reply_markup=create_cancel())
            await message.reply("Теперь введите название канала")
            await FSMMAC.title.set()

        except Exception as e:
            await message.reply("ERROR!\n" + str(e))


@dp.message_handler(state=FSMMAC.title)
async def manually_add_channel_title(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.reply("Отменено")
        await state.finish()
        await message.answer("Выберите:",
                             reply_markup=create_channels_action())
        await FSMCCHOOSE.choose.set()

    else:
        try:
            await state.update_data(title=message.text)
            data = await state.get_data()
            await message.answer(f"ID канала: {data['id']}\nНазвание канала: {data['title']}",
                                 reply_markup=create_cancel())
            await message.reply("Теперь введите ссылку на канал")
            await FSMMAC.link.set()

        except Exception as e:
            await message.reply("ERROR!\n" + str(e))


@dp.message_handler(state=FSMMAC.link)
async def manually_add_channel_link(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.reply("Отменено")
        await state.finish()
        await message.answer("Выберите:",
                             reply_markup=create_channels_action())
        await FSMCCHOOSE.choose.set()

    else:
        try:
            await state.update_data(link=message.text)
            data = await state.get_data()
            await message.reply(f"ID канала: {data['id']}\nНазвание канала: {data['title']}\nСсылка на канал: {data['link']}",
                                reply_markup=create_cancel())
            await add_channel(channel_id=data['id'], title=data['title'], username=data['link'])

            await message.reply(await markdowned(f"Канал *{data['title']}* успешно добавлен!"),
                                reply_markup=create_admin_default(),
                                parse_mode="MarkdownV2")

            await state.finish()

        except Exception as e:
            await message.reply(str(e) + "!", reply_markup=create_admin_default())
            await state.finish()