from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMCCCHOOSE(StatesGroup):
    choose = State()
