import logging
from aiogram import Router, Bot, F, html
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from fsm import QuestionStates

from config_reader import config

question_router = Router()


@question_router.message(Command('question'))
async def start_asking_question_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(QuestionStates.waiting_for_question)
    await message.answer(
        text=('Ok, I am waiting for question!\n\n'
              '<i>Note: the message can contain no more than 250 characters</i>')
    )


@question_router.message(QuestionStates.waiting_for_question, Command('cancel'))
async def cancel_question_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Question cancelled")
    await state.clear()


@question_router.message(QuestionStates.waiting_for_question, F.text.func(len) <= 250)
async def get_question_handler(message: Message, state: FSMContext, bot: Bot, users_data: set) -> None:
    
    await bot.forward_message(
        chat_id=config.main_chat_id,
        from_chat_id=message.from_user.id,
        message_id=message.message_id,
    )
    users_data.add(message.from_user.id)
    logging.info(users_data)
    await message.answer("Question sent")
    await state.clear()


@question_router.message(QuestionStates.waiting_for_question)
async def too_long_question_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=(f'The message can contain no more than 250 characters\n'
              f'Your message contains {len(message.text)}/250 characters')
    )
