from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from structures.messages import START_MSG

start_router = Router()


@start_router.message(F.from_user, Command(commands=['start', 'help']))
async def cmd_start_handler(message: Message) -> None:
    await message.answer(
        text=START_MSG
    )


@start_router.message(~F.chat.type.in_('private'), Command('getchatid'))
async def get_chat_id(message: Message):
    await message.answer(message.chat.id)
