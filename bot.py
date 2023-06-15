import logging
import asyncio

from aiogram import Dispatcher, Bot

from handlers import start_router, question_router, answer_router
from commands import commands_list

from config_reader import config
from storage import users_set

async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(start_router, question_router, answer_router)

    bot = Bot(
        token=config.bot_token.get_secret_value(),
        parse_mode='HTML'
    )
    await bot.set_my_commands(commands=commands_list)
    await bot.delete_webhook(drop_pending_updates=True)


    await dp.start_polling(bot, users_data=users_set)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s'
    )
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
