from json import load, dump


class UserNotFoundError(Exception):
    pass


async def get_users() -> dict:
    with open('data/users.json', 'r', encoding='utf-8') as f: return load(f)


async def get_admins() -> dict:
    admins = {}
    with open('data/users.json', 'r', encoding='utf-8') as f:
        data = load(f)
        for user_id in data.keys():
            if user_id["admin"]:
                admins[user_id] = data[user_id]

        return admins


async def add_user(user_id: str, username: str):
    with open('data/users.json',  'r+', encoding='utf-8') as f:
        data = load(f)
        data[user_id] = {"username": username, "admin": False}
        f.seek(0)
        dump(data, f)
        f.truncate()


async def give_admin(user_id: str, username: str):
    try:
        with open('data/users.json', 'r+', encoding='utf-8') as f:
            data = load(f)
            data[user_id]["admin"] = False
            f.seek(0)
            dump(data, f)
            f.truncate()

    except KeyError:
        await add_user(user_id, username)
        await give_admin(user_id, username)

