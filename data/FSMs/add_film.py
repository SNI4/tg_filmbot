from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMAF(StatesGroup):
    code = State()
    name = State()
    media = State()
    desc = State()
    link = State()
