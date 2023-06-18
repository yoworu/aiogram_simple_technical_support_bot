from aiogram.fsm.state import StatesGroup, State


class QuestionStates(StatesGroup):
    waiting_for_question = State()
    