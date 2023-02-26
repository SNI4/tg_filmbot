from aiogram import types
from aiogram.dispatcher import FSMContext
from data.FSMs.add_film import FSMAF
from keyboards.cancel_reply import create_cancel
from loader import dp
from utils.misc.markreplace import markdowned


@dp.callback_query_handler(state=FSMAF)
async def rk_callback(callback: types.CallbackQuery, state: FSMContext):
    print('debug')
    if callback.data.startswith('rk'):
        code = callback.data.split('?')[1]
        await state.update_data(code=code)
        await callback.message.answer(await markdowned(f"Код фильма: *{code}*"))
        await callback.message.reply("Теперь введите *название* фильма", reply_markup=create_cancel(),
                                     parse_mode="MarkdownV2")
        await FSMAF.name.set()

    elif callback.data == "manualcode":
        await callback.message.answer(await markdowned("Введите *код* фильма\n||Используйте только цифры >=0<=9999||"),
                                      reply_markup=create_cancel(), parse_mode="MarkdownV2")
        await FSMAF.code.set()

