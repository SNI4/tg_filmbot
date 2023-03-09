from loader import bot
from utils.json_worker.users import delete_admin, get_admins, get_users, give_admin


async def action_Aadd(callback):
    admin_to_add_user_id = callback.data.split('?')[1]
    sender_user_id = callback.data.split('?')[2]
    add_admin_username = (await get_users())[admin_to_add_user_id]['username']
    await give_admin(admin_to_add_user_id)
    await callback.answer("Действие подтверждено")
    await callback.message.delete()
    await bot.send_message(chat_id=sender_user_id,
                           text=f"Ваше предложение добавить адммина {add_admin_username} было выполнено.")