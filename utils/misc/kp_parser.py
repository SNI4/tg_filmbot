from bs4 import BeautifulSoup as bs
from requests import get

from utils.misc.get_stars import get_stars


def parse_kp(content_id: str):
    link = f"https://rating.kinopoisk.ru/{content_id}.xml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.99 Safari/537.36"
    }
    r = get(link, headers=headers)
    if r.status_code == 200:
        page = bs(r.text, features="xml")
        kp = "КиноПоиск: " + page.find("kp_rating").text + '\n' + get_stars(round(float(page.find("kp_rating").text)))
        imdb = "IMDB: " + page.find("imdb_rating").text + '\n' + get_stars(round(float(page.find("imdb_rating").text)))
        return f"{kp}\n{imdb}"

    else:
        raise Exception("KP isn't working!")


def check_kp(content_id: str) -> bool:
    link = f"https://rating.kinopoisk.ru/{content_id}.xml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.99 Safari/537.36"
    }
    return True if get(link, headers=headers).status_code == 200 else False
