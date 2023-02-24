from json import load, dump
from data.config import ADMIN_ID, ADMIN_USERNAME


class DublicateChannelError(Exception):
    pass


async def get_channels() -> dict:
    with open('data/channels.json', 'r', encoding='utf-8') as f:
        data = load(f)
        return data


async def add_channel(channel_id: str, title: str, username: str, subs=0):
    link = username if "t.me/" in username else "t.me/" + username

    try:
        with open('data/channels.json', 'r+', encoding='utf-8') as f:
            data = load(f)

            if channel_id in data.keys():
                raise DublicateChannelError("This channel already exist!")

            data[channel_id] = {"title": title, "link": link, "subscribers": subs}
            f.seek(0)
            dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()

    except Exception as e:
        raise Exception(e)


async def add_channel_sub(channel_id: str):
    try:
        with open('data/channels.json', 'r+', encoding='utf-8') as f:
            data = load(f)
            data[channel_id]["subscribers"] += 1
            f.seek(0)
            dump(data, f)
            f.truncate()

    except Exception as e:
        raise Exception(e)


async def del_channel(channel_id):
    try:
        with open('data/channels.json', 'r+', encoding='utf-8') as f:
            data = load(f)
            del data[channel_id]
            f.seek(0)
            dump(data, f)
            f.truncate()
    except Exception as e:
        raise Exception(e)
