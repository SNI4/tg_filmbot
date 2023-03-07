from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.user_keyboards.default_reply import create_default
from utils.misc.isAdmin import isAdmin


async def choose_keyboard(user_id: str):
    return create_default() if not await isAdmin(user_id) else create_admin_default()