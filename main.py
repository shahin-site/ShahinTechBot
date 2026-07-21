#!/usr/bin/env python3
"""Main entry point for ShahinTechBot."""

import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from database import init_db

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/bot.log')
    ]
)

logger = logging.getLogger(__name__)


async def main() -> None:
    """Main function to run the bot."""
    logger.info('Starting ShahinTechBot...')
    
    # Initialize database
    await init_db()
    logger.info('Database initialized')
    
    # Create bot and dispatcher
    bot = Bot(token=settings.BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # TODO: Register routers here
    logger.info('Bot handlers registered')
    
    try:
        logger.info(f'Bot started polling (Debug: {settings.DEBUG})')
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logger.error(f'Error occurred: {e}', exc_info=True)
    finally:
        logger.info('Bot stopped')
        await bot.session.close()


if __name__ == '__main__':
    # Create logs directory if it doesn't exist
    Path('logs').mkdir(exist_ok=True)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Bot interrupted by user')
