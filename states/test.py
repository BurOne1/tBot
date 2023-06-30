from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    test1 = State()
    test2 = State()


class Price(StatesGroup):
    test1 = State()


class Pumps(StatesGroup):
    test1 = State()


class Wilo(StatesGroup):
    test1 = State()
    test2 = State()


class General(StatesGroup):
    test1 = State()


class GoogleSheet(StatesGroup):
    test1 = State()

