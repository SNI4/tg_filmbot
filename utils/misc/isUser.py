from utils.json_worker.users import get_users


async def isUser(user_id: str) -> bool:
    return True if (user_id in (await get_users()).keys()) else False
