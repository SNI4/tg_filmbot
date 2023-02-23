from aiogram import types

from aiogram.dispatcher import FSMContext

from data.FSMs.auto_add_channel import FSMAAC
from data.FSMs.manual_add_channel import FSMMAC
from keyboards.cancel_reply import create_cancel
from keyboards.default_reply import create_default
from loader import dp
from utils.json_worker.channels import add_channel


@dp.message_handler(state=FSMAAC.AddChannel, content_types=['any'])
async def save_channelx(message: types.Message, state: FSMContext):
    if message.forward_from_chat.type == "channel":

        if not message.forward_from_chat.username:
            await message.reply('Не удалось получить ссылку на канал. Попробуйте вручную')
            await message.answer("Введите ID канала", reply_markup=create_cancel())
            await FSMMAC.id.set()

        else:
            try:
                await message.reply(message.forward_from_chat.id)
                await add_channel(channel_id=str(message.forward_from_chat.id),
                                  title=message.forward_from_chat.title,
                                  username=message.forward_from_chat.username)

                await message.reply("Канал " + message.forward_from_chat.title + " успешно добавлен!")
                await state.finish()

            except Exception as e:
                await message.reply(f'ERROR!\n{e}')

    elif message.text.lower() == "отмена":

        await message.reply("Отменено", reply_markup=create_default())
        await state.finish()

    else:
        await message.reply("Перешлите сообщение из канала!", reply_markup=create_cancel())


@dp.message_handler(state=FSMMAC.id)
async def manually_add_channel_id(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.reply("Отменено", reply_markup=create_default())
        await state.finish()

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
        await message.reply("Отменено", reply_markup=create_default())
        await state.finish()

    else:
        try:
            await state.update_data(title=message.text)
            await message.answer(f"ID канала: {FSMMAC.id}\nНазвание канала: {FSMMAC.title}",
                                 reply_markup=create_cancel())
            await message.reply("Теперь введите ссылку на канал")
            await FSMMAC.link.set()

        except Exception as e:
            await message.reply("ERROR!\n" + str(e))


@dp.message_handler(state=FSMMAC.link)
async def manually_add_channel_link(message: types.Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.reply("Отменено", reply_markup=create_default())
        await state.finish()

    else:
        try:
            await state.update_data(title=message.text)
            await message.reply(f"ID канала: {FSMMAC.id}\nНазвание канала: {FSMMAC.title}\nID Канала: {FSMMAC.id}",
                                reply_markup=create_cancel())

            await add_channel(channel_id=FSMMAC.id, title=FSMMAC.title, username=FSMMAC.link)
            await message.reply("Канал " + FSMMAC.title + " успешно добавлен!")
        except Exception as e:
            await message.reply("ERROR!\n" + str(e))
