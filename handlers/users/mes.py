from aiogram import types
from loader import dp


@dp.message_handler()
async def handl(message: types.Message):
    await message.answer(message)