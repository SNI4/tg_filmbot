from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.FSMs.auto_add_channel import FSMAAC
from keyboards.cancel_reply import create_cancel
from keyboards.default_reply import create_default
from loader import dp
from utils.isAdmin import isAdmin
from utils.json_worker.channels import add_channel


@dp.message_handler(content_types=['any'])
async def message_handle(message: types.Message):
    user_id = str(message.from_id)
    m = message.text.lower()

    if (m == "добавить канал") and (await isAdmin(user_id)):
        await message.reply("Перешлите сообщение из канала, который хотите добавить.", reply_markup=create_cancel())
        await FSMAAC.AddChannel.set()

    else:
        await message.reply("123")

