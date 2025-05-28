from aiogram import Router, types
from aiogram.filters import Command

quiz_router = Router()


@quiz_router.message(Command("asd"))
async def send_quiz(message: types.Message):
    await message.reply("222")
