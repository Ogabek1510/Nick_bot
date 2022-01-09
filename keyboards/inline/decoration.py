from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

next_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Keyingi", callback_data="next")
    ]]
)