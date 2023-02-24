from data.config import ADMIN_ID
from utils.json_worker.users import get_admins


async def isAdmin(user_id: str) -> bool:
    return True if (user_id in (await get_admins()).keys()) or (user_id == str(ADMIN_ID)) else False
