from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "Botdan foydalanish uchun /start komandasini bosing va o'zingizga yoqqan fontni tanlang!",
            "Botdan qaytgan, tayyor bo'lgan fontdan nusxa olish uchun, ustiga bir marta bosing!")
    
    await message.answer("\n".join(text))
