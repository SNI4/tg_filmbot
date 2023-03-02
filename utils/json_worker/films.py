from json import dump, load


async def get_films() -> dict:
    with open('data/films.json', 'r', encoding='utf-8') as f:
        data = load(f)
        return data


async def save_film(code: str, title: str, media_id: str, desc: str, link: str):
    with open('data/films.json', 'r+', encoding='utf-8') as f:
        data = load(f)
        if code in data.keys():
            raise Exception("DublicateFilmError")
        else:
            data[code] = {
                'title': title,
                'media': media_id,
                'description': desc,
                'link': link
            }
            f.seek(0)
            dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()


async def delete_film(code: str):
    with open('data/films.json', 'r+', encoding='utf-8') as f:
        data = load(f)
        del data[code]
        f.seek(0)
        dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()
