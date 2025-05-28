from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton

)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="отправить уведомления"), KeyboardButton(text="123")]

], resize_keyboard=True, one_time_keyboard=True)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="open youtube", url="https://www.youtube.com")],
        [InlineKeyboardButton(text="open google", url="https://www.google.com")]]
)
