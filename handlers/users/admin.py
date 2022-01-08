from datetime import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import fonts_menu, back
from data.config import ADMINS
from loader import dp, db, bot
from states.adminStates import AdminCommands


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.count_users()[0]
    await message.answer(text=f"Bazada {users} ta foydalanuvchi bor")

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    await message.answer("Reklamani obunachilarga yuborishingiz mumkin!", reply_markup=back)
    await AdminCommands.adsMenu.set()

@dp.message_handler(state=AdminCommands.adsMenu, user_id=ADMINS)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        user = db.select_all_users()
        for user in user:
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text=message.text)
    await message.answer("<b>Reklama obunachilarga yuborildi!</b>")

@dp.message_handler(text="/cleardb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")