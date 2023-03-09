from aiogram import types

from handlers.callbacks_actions.Aadd import action_Aadd
from handlers.callbacks_actions.Adec import action_Adec
from loader import dp
from handlers.callbacks_actions.cancel import action_cancel
from handlers.callbacks_actions.cd import action_cd
from handlers.callbacks_actions.da import action_da
from handlers.callbacks_actions.qwc import action_qwc
from handlers.callbacks_actions.qwd import action_qwd


@dp.callback_query_handler()
async def callback_actions(callback: types.CallbackQuery):
    if callback.data.startswith("da"):
        await action_da(callback)

    elif callback.data.startswith("qwc"):
        await action_qwc(callback)

    elif callback.data.startswith("qwd"):
        await action_qwd(callback)

    elif callback.data.startswith("cd"):
        await action_cd(callback)

    elif callback.data.startswith("Aadd"):
        await action_Aadd(callback)

    elif callback.data.startswith("Adec"):
        await action_Adec(callback)

    elif callback.data.startswith("cancel"):
        await action_cancel(callback)

