
# MAIN IMPORTS
import asyncio
import aiogram
from aiogram import Bot, types, Dispatcher
from config import BOT_TOKEN


# HANDLERS IMPORTS
from handlers import start_menu
from handlers import quiz


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


"""HANDLERS_REGISTRATION"""
dp.include_router(start_menu.start_menu_router)
dp.include_router(quiz.quiz_router)


async def main():
    print("Bot Started")
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot is shutting down...')
