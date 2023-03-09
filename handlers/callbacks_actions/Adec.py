from loader import bot
from utils.json_worker.users import delete_admin, get_admins, get_users


async def action_Adec(callback):
    admin_user_id = callback.data.split('?')[1]
    admin_username = (await get_users())[admin_user_id]['username']
    sender_user_id = callback.data.split('?')[2]
    await callback.answer("Действие отклонено")
    await callback.message.delete()
    await bot.send_message(chat_id=sender_user_id,
                           text=f"Ваше предложение добавить адммина {admin_username} было отклонено.")