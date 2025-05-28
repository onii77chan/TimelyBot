from aiogram import types, Router
from aiogram.filters import Command

from keyboards.keyboards import (
    main, inline_kb

)
start_menu_router = Router()


@start_menu_router.message(Command("start"))
async def start_menu(message: types.Message):
    await message.answer("start handler called", reply_markup=main)


@start_menu_router.message(Command("help"))
async def open_other_sites(message: types.Message):
    await message.answer(text="на какой сайт хотите перейти?", reply_markup=inline_kb)
