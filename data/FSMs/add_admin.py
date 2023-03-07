from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMAD(StatesGroup):
    user_id = State()
    confirm = State()
