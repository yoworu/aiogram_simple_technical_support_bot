from redis.asyncio import Redis

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from structures.messages import (
    QUESTION_START_MSG,
    QUESTION_CANCEL_MSG,
    QUESTION_SENT_MSG,
    QUESTION_LONG_MSG
)


from config import MAIN_CHAT_ID

from fsm import QuestionStates

question_router = Router()
question_router.message.filter(F.chat.type == 'private')


@question_router.message(Command('question'))
async def start_asking_question_handler(message: Message,
                                        state: FSMContext) -> None:
    await state.set_state(QuestionStates.waiting_for_question)
    await message.answer(
        text=QUESTION_START_MSG
    )


@question_router.message(QuestionStates.waiting_for_question, Command('cancel'))
async def cancel_question_handler(message: Message,
                                  state: FSMContext) -> None:
    await message.answer(QUESTION_CANCEL_MSG)
    await state.clear()


@question_router.message(QuestionStates.waiting_for_question, F.text.func(len) <= 250)
async def get_question_handler(message: Message,
                               state: FSMContext,
                               bot: Bot,
                               redis: Redis) -> None:
    await bot.forward_message(
        chat_id=MAIN_CHAT_ID,
        from_chat_id=message.from_user.id,
        message_id=message.message_id,
    )

    await redis.append(message.from_user.id, message.from_user.username)
    await message.answer(QUESTION_SENT_MSG)
    await state.clear()


@question_router.message(QuestionStates.waiting_for_question)
async def too_long_question_handler(message: Message) -> None:
    await message.answer(
        text=QUESTION_LONG_MSG.format(len(message.text))
    )
