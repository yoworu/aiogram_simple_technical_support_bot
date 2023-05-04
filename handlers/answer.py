import logging

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.types import ChatMemberAdministrator
from storage import users_set

answer_router = Router()


@answer_router.message(
    F.reply_to_message.forward_from.id.in_(users_set)
)
async def send_answer_handler(message: Message, bot: Bot, users_data: set) -> None:
    await bot.copy_message(
        chat_id=message.reply_to_message.forward_from.id,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )
    
    logging.info(message.chat.get_administrators(), message.chat.get_member(message.from_user.id))
    
    users_data.discard(message.reply_to_message.forward_from.id)
    logging.info(users_data)
    await message.answer("Answer sent")

