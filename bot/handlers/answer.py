from redis.asyncio import Redis

from aiogram import Router, Bot, F
from aiogram.types import Message

from structures.messages import ANSWER_SENT_MSG

answer_router = Router()


@answer_router.message(F.reply_to_message.forward_from.id)
async def send_answer_handler(message: Message,
                              bot: Bot,
                              redis: Redis) -> None:
    forward_user_id = message.reply_to_message.forward_from.id
    user = await redis.get(forward_user_id)
    if user:        
        await bot.copy_message(
            chat_id=forward_user_id,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )        
        await redis.delete(forward_user_id)
        await message.answer(ANSWER_SENT_MSG)
