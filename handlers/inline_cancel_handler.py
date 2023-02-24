from aiogram import types
from aiogram.dispatcher import FSMContext

from data.FSMs.add_film import FSMAF
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from loader import dp


@dp.callback_query_handler(state=FSMAF)
async def inlin_cancel_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "admin_cancel":
        await state.finish()
        await callback.message.answer("*Добро пожаловать*", reply_markup=create_admin_default())
