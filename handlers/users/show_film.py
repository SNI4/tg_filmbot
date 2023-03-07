from aiogram import types
from keyboards.user_keyboards.film_link import create_film_link
from utils.json_worker.films import get_films
from utils.misc.markreplace import markdowned


async def film(message: types.Message, m, user_id):
    try:
        film_data = (await get_films())[m]
        film_message = f"*{m}*\n*{film_data['title']}*\n{film_data['description']}"
        await message.reply_photo(caption=await markdowned(film_message),
                                  reply_markup=create_film_link(
                                      url=True if film_data['link'] != 'nolink' else False,
                                      link=film_data['link'],
                                      user_id=user_id),
                                  photo=film_data['media'],
                                  parse_mode="MarkdownV2")
    except KeyError as e:
        await message.reply("key error")