from aiogram import types
from loader import dp
from utils.json_worker.admins import *
from utils.json_worker.users import *


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
	if str(message.from_id) not in (await get_admins()).keys():
		if str(message.from_id) not in (await get_users()).keys():
			pass


		else:
			pass


	else:
		pass