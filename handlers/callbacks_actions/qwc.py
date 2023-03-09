from loader import bot
from utils.json_worker.users import delete_admin, get_admins


async def action_qwc(callback):
    admin_to_delete_user_id = callback.data.split('?')[1]
    sender_user_id = callback.data.split('?')[2]
    deleted_admin_username = (await get_admins())[admin_to_delete_user_id]['username']
    await delete_admin(admin_to_delete_user_id)
    await callback.answer("Действие подтверждено")
    await callback.message.delete()
    await bot.send_message(chat_id=sender_user_id,
                           text=f"Ваше предложение удалить адммина {deleted_admin_username} было выполнено.")