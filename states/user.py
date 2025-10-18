from aiogram.fsm.state import StatesGroup, State


class PartnerState(StatesGroup):
    fullname = State()
    job = State()
    contact = State()
    address = State()
    price = State()
    study_or_work = State()
    time = State()
    goal = State()