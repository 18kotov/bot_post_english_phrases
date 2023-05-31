import asyncio
import os
from aiogram import Bot, Dispatcher
from bot.handlers import basic

from settings import get_logger

logger = get_logger(__name__)

TOKEN = os.environ.get('TOKEN')
ADMIN_ID = os.environ.get('ADMIN_ID')
bot = Bot(token=TOKEN)


async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Бот выключен!")


async def start():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_router(basic.router)

    try:
        await dp.start_polling(bot)
    except Exception as error:
        logger.error(error)
    finally:
        await bot.session.close()


def main():
    asyncio.run(start())


if __name__ == '__main__':
    main()
