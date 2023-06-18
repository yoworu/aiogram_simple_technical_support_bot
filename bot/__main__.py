import logging
import asyncio

from redis.asyncio import Redis

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage

from handlers import start_router, question_router, answer_router
from structures.commands import commands_list
from config import BOT_TOKEN


async def main() -> None:
    redis = Redis() # working redis-server required
    redis_fsm = RedisStorage(redis)
    
    dp = Dispatcher(storage=redis_fsm)
    dp.include_routers(start_router, question_router, answer_router)

    bot = Bot(
        token=BOT_TOKEN,
        parse_mode='HTML'
    )
    await bot.set_my_commands(commands=commands_list)
    await bot.delete_webhook(drop_pending_updates=True)


    await dp.start_polling(bot, redis=redis)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%H:%M.%S'
    )
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
