from aiogram.dispatcher import FSMContext
from data.FSMs.search_film import FSMSF
from data.config import ADMIN_ID
from loader import dp, bot
from aiogram.types import Message
from requests import get
from bs4 import BeautifulSoup as bs


@dp.message_handler(state=FSMSF.search)
async def get_searched_film(message: Message, state: FSMContext):
    if message.text is not None:
        url = "https://podborfilma.com/?s=" + message.text.replace('\n', ' ').replace(' ', '+')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.99 Safari/537.36"
        }
        r = get(url, headers=headers)
        if r.status_code == 200:
            page = bs(r.text, 'html.parser')
            results = []
            for comment in page.find_all('ul', class_='children'):
                res = comment.find('div', class_="gpur-comment-review-text").text
                if "«" in res: results.append(res)
            await message.reply("Возможные варианты:\n\n" + "\n".join(results) if len(results) > 0 else "Ничего не найдено :(")
            await state.finish()

        else:
            await state.finish()
            await message.reply("Произошла ошибка! Попробуйте позже...")
            await bot.send_message(chat_id=ADMIN_ID, text=f"WARNING!\nУ пользователя {message.from_id}"
                                                          f"Ошибка при поиске фильма по описанию!\n"
                                                          f"Ссылка: {url}\nКод запроса: {r.status_code}")

    elif message.text is not None and message.text.lower() == "Отмена":
        await message.reply('отменено')
        await state.finish()

    else:
        await message.reply("не понял")