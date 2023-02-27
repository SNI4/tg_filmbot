from json import load, dump


async def get_admins() -> dict:
    with open('data/admins.json', 'r', encoding='utf-8') as f: return load(f)


async def add_admin(username: str, user_id: str):
    try:
        with open('data/admins.json', 'w+', encoding='utf-8') as f:
            data = load(f)
            data[user_id] = username
            f.seek(0)
            dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()
    except Exception as e:
        raise Exception(e)


async def del_admin(user_id: str):
    try:
        with open('data/admins.json', 'w+', encoding='utf-8') as f:
            data = load(f)
            del data[user_id]
            f.seek(0)
            dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()
    except Exception as e:
        raise Exception(e)