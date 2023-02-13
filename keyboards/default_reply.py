from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

ib1 = KeyboardButton(text='?')

ikb.add(ib1)