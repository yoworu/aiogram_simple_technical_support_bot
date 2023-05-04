from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(F.from_user, Command(commands=['start', 'help']))
async def cmd_start_handler(message: Message) -> None:
    await message.answer(
        text=('Hello, I am <b>technical support bot</b>\n'
              'To start asking your questions type /question')
    )
