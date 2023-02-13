from json import load, dump
from data.config import ADMIN_ID, ADMIN_USERNAME


async def get_channels() -> dict:
    with open('data/channels.json', 'r', encoding='utf-8') as f:
        data = load(f)
        data[str(ADMIN_ID)] = ADMIN_USERNAME
        return data


async def add_channel(title: str, channel_id: str):
    try:
        with open('data/admins.json', 'w+', encoding='utf-8') as f:
            data = load(f)
            data[channel_id] = title
            f.seek(0)
            dump(data, f)
            f.truncate()
    except Exception as e:
        raise Exception(e)


async def del_channel(channel_id):
    try:
        with open('data/admins.json', 'w+', encoding='utf-8') as f:
            data = load(f)
            del data[channel_id]
            f.seek(0)
            dump(data, f)
            f.truncate()
    except Exception as e:
        raise Exception(e)