from aiogram import types
from aiogram.dispatcher import FSMContext
from data.FSMs.del_film import FSMDF
from loader import dp


@dp.message_handler(state=FSMDF.code)
async def get_delete_code(message: types.Message, state: FSMContext):
    try:
        code = int(message.text)
        if 0 <= code <= 9999:

    except:
        pass