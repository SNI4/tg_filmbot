from utils.misc.get_keyboard import choose_keyboard


async def action_cancel(callback):
    user_id = callback.data.split('?')[1]
    await callback.message.reply('Добро пожаловать',
                                 reply_markup=await choose_keyboard(user_id))