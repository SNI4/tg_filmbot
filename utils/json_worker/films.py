from json import dump, load


async def get_films() -> dict:
    with open('data/films.json', 'r', encoding='utf-8') as f:
        data = load(f)
        return data


