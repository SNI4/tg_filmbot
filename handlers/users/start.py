from aiogram import types

from keyboards.checkbox_inline import create_checkbox
from loader import dp
from utils.json_worker.channels import get_channels
from utils.json_worker.users import *


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
	if str(message.from_id) not in (await get_admins()).keys():
		if str(message.from_id) not in (await get_users()).keys():

			txt = 'Чтобы начать пользоваться ботом, ты должен подписаться на эти каналы:\n' + \
				'\n'.join([key["link"] for key in (await get_channels()).keys()]) + \
				'\nПосле того как подпишешься, нажми на кнопку "✅"'

			await message.reply(txt, reply_markup=create_checkbox())

		else:
			pass


	else:
		pass