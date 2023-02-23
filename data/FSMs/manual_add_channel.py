from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMMAC(StatesGroup):
    id = State()
    title = State()
    link = State()
