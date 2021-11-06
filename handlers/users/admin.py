from datetime import time

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    user = db.select_all_users()
    for user in user:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Botni rivojlantirishga o'z hissangizni qo'shing!\nBuning uchun botni do'stlaringizga ham tavsiya qiling")

    @dp.message_handler(text="/cleardb", user_id=ADMINS)
    async def get_all_users(message: types.Message):
        db.delete_users()
        await message.answer("Baza tozalandi!")