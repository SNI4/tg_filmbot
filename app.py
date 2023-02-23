from aiogram import executor
from loader import dp 
import handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
	await set_default_commands(dispatcher)
	print('The BOT started!')


async def on_shutdown(dispatcher):
	print('The BOT shutdown!')


if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)