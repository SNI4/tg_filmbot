from json import dump


def main(f):
    data = {}
    for i in range(1, 1001):
        data[str(i)] = {
            "title": "алвыь",
            "media": "AgACAgIAAxkBAAIGQWQAAd4g9pBmujpY8UIBmsis-i_2jwACRsIxGzPpCEjnuDDlUUXGIQEAAwIAA3kAAy4E",
            "description": "ылвдаьвлыдаьлвыд\nЛаьвыдлаьывлдаьыв",
            "link": "https://google.com"
        }
    dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    with open('films.json', 'w', encoding='utf-8') as f:
        main(f)
