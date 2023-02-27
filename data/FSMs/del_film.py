from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMDF(StatesGroup):
    code = State()