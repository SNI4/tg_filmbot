from aiogram import types
from aiogram.dispatcher import FSMContext

from data.FSMs.add_film import FSMAF
from data.FSMs.auto_add_channel import FSMAAC
from data.FSMs.cchoose import FSMCCHOOSE
from data.FSMs.del_film import FSMDF
from data.FSMs.fchoose import FSMCHOOSE
from keyboards.admin_keyboards.add_film_code import film_code_choose
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.cancel_reply import create_cancel
from keyboards.user_keyboards.subscribe_channels import create_subscribe
from loader import dp
from utils.json_worker.films import get_films
from utils.misc.isAdmin import isAdmin
from utils.misc.markreplace import markdowned


@dp.message_handler(state=FSMCCHOOSE.choose)
async def get_film_action(message: types.Message, state: FSMContext):
    user_id = str(message.from_id)
    m = message.text.lower()

    if (m == "добавить канал") and (await isAdmin(user_id)):
        await message.reply("Перешлите сообщение из канала, который хотите добавить.", reply_markup=create_cancel())
        await state.finish()
        await FSMAAC.AddChannel.set()

    elif (m == "удалить канал") and (await isAdmin(user_id)):
        await state.finish()
        await message.reply("Выберите канал, который хотите убрать",
                            reply_markup=await create_subscribe(url=False, cancel=True))

    elif (m == "отмена") and (await isAdmin(user_id)):
        await message.reply("отменено")
        await state.finish()
        await message.answer(await markdowned("*Добро пожаловать!*"),
                             reply_markup=create_admin_default(),
                             parse_mode="MarkdownV2")
    else:
        await message.reply('непон')
