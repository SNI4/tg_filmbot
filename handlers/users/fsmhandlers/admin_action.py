from aiogram import types
from aiogram.dispatcher import FSMContext

from data.FSMs.achoose import FSMCCCHOOSE
from data.FSMs.add_admin import FSMAD
from data.FSMs.add_film import FSMAF
from data.FSMs.del_film import FSMDF
from data.FSMs.fchoose import FSMCHOOSE
from data.config import ADMIN_ID
from keyboards.admin_keyboards.add_film_code import film_code_choose
from keyboards.admin_keyboards.admin_default_reply import create_admin_default
from keyboards.admin_keyboards.delete_admin_inline import admins_to_delete
from keyboards.cancel_reply import create_cancel
from loader import dp
from utils.json_worker.films import get_films
from utils.json_worker.users import get_admins, delete_admin
from utils.misc.isAdmin import isAdmin
from utils.misc.markreplace import markdowned


@dp.message_handler(state=FSMCCCHOOSE.choose)
async def get_adm_action(message: types.Message, state: FSMContext):
    user_id = str(message.from_id)
    m = message.text.lower()

    if (m == "добавить админа") and (await isAdmin(user_id)):
        await message.reply("перешлите сообщ или введите его айди",
                            reply_markup=create_cancel())
        await state.finish()
        await FSMAD.user_id.set()

    elif (m == "удалить админа") and (await isAdmin(user_id)):
        await state.finish()
        if len((await get_admins(skip_cadmin=True)).keys()) > 0:
            await message.reply("выбери",
                                reply_markup=admins_to_delete(await get_admins(skip_cadmin=True), user_id))
        else:
            await message.reply("нету админов для удаления", reply_markup=create_admin_default())

    elif (m == "отмена") and (await isAdmin(user_id)):
        await message.reply("отменено")
        await state.finish()
        await message.answer(await markdowned("*Добро пожаловать!*"),
                             reply_markup=create_admin_default(),
                             parse_mode="MarkdownV2")

    else:
        await message.reply("непон")
