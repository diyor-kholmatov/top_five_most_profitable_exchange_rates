import asyncio

from aiogram import Bot, Dispatcher
#from aiogram.types import Message
from config import Config
from data_base import pg_db
from aiogram.utils import executor
from scrapingfile import dollar_exchange_rate, euro_exchange_rate

bot = Bot(token=Config.token)
dp = Dispatcher(bot=bot)


async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
        dollar_exchange_rate.main()
        euro_exchange_rate.main()
        print('Bot run')
    except(KeyboardInterrupt, SystemExit):
        print('Bot stop')
