from data.config import ADMIN_ID
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.delete_admin_confirm_inline import create_deleted_admin
from loader import bot
from utils.json_worker.users import delete_admin, get_admins


async def action_da(callback):
    user_id = callback.data.split('?')[1]
    sender_user_id = callback.data.split('?')[2]
    username = (await get_admins())[user_id]['username']

    if sender_user_id == str(ADMIN_ID):
        await delete_admin(user_id)
        await callback.answer(f"Админ {username} успешно удален")

    elif sender_user_id == user_id:
        await callback.message.answer("Невозможно удалить самого себя!",
                                      reply_markup=create_admin_default())
    else:
        await bot.send_message(chat_id=ADMIN_ID,
                               text=f"подтвердите удаление админа {username}",
                               reply_markup=create_deleted_admin(user_id=user_id,
                                                                 sender_user_id=sender_user_id))
        await callback.answer("Действие отправлено на модерацию")
