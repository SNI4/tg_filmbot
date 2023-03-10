from json import load, dump

from data.config import ADMIN_ID


class UserNotFoundError(Exception):
    pass


async def get_users() -> dict:
    with open('data/users.json', 'r', encoding='utf-8') as f: return load(f)


async def get_admins(skip_cadmin: bool = False) -> dict:
    admins = {}
    with open('data/users.json', 'r', encoding='utf-8') as f:
        data = load(f)
        for user_id in data.keys():
            if data[user_id]["admin"]:
                admins[user_id] = data[user_id]
        if skip_cadmin: admins.pop(str(ADMIN_ID))
        return admins


async def add_user(user_id: str, username: str, admin: bool = False):
    with open('data/users.json',  'r+', encoding='utf-8') as f:
        data = load(f)
        data[user_id] = {"username": username, "admin": admin}
        f.seek(0)
        dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()


async def delete_admin(user_id: str):
    with open('data/users.json', 'r+', encoding='utf-8') as f:
        data = load(f)
        data[user_id]["admin"] = False
        f.seek(0)
        dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()


async def give_admin(user_id: str):
    try:
        with open('data/users.json', 'r+', encoding='utf-8') as f:
            data = load(f)
            data[user_id]["admin"] = True
            f.seek(0)
            dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()
            return True

    except KeyError:
        return False

