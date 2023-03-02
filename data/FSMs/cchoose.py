from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMCCHOOSE(StatesGroup):
    choose = State()