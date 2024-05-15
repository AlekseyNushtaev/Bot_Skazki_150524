import asyncio
import logging
from handlers import handlers_main, handlers_repka

from aiogram import Dispatcher, Bot

from config import TG_TOKEN

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    logging.info('Starting bot')

    bot = Bot(token=TG_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(handlers_main.router)
    dp.include_router(handlers_repka.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

