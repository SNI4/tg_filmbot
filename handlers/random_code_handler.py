from aiogram import types
from aiogram.dispatcher import FSMContext
from data.FSMs.add_film import FSMAF
from keyboards.cancel_reply import create_cancel
from loader import dp


@dp.callback_query_handler(state=FSMAF)
async def admin_vote_callback(callback: types.CallbackQuery, state: FSMContext):
    if callback.data.startswith('rk'):
        code = callback.data.split('?')[1]
        await state.update_data(code=code)
        await callback.message.answer(("Код фильма: " + code))
        await callback.message.reply('Теперь введите название фильма', reply_markup=create_cancel())
        await FSMAF.name.set()
