from json import load, dump

class UserNotFoundError(Exception):
    pass

async def get_users() -> dict:
    with open('data/users.json', 'r', encoding='utf-8') as f: return load(f)


async def add_user(user_id: str, username: str):
    with open('data/users.json',  'w+', encoding='utf-8') as f:
        data = load(f)
        data[user_id] = {"username": username}
        f.seek(0)
        dump(data, f)
        f.truncate()
