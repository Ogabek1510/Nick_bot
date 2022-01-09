import logging
import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from data.config import ADMINS
from keyboards.inline.subscription import check_button
from keyboards.default.buttons import fonts_menu
from loader import dp, db, bot
from utils.misc import subscription


@dp.message_handler(CommandStart())
async def show_channels(message: types.Message):
    """name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor"
    await bot.send_message(chat_id=ADMINS[0], text=msg)"""



    for channel in CHANNELS:
        status = await subscription.check(user_id=message.from_user.id, channel=channel)
        if status:
            await message.answer(f"<i>👋 Salom, <b>{message.from_user.full_name}</b>\nO'zingizga yoqqan fontni tanlang!</i>", reply_markup=fonts_menu)
        else:
            channels_format = str()
            for channel in CHANNELS:
                chat = await bot.get_chat(channel)
                invite_link = await chat.export_invite_link()
                logging.info(invite_link)
                channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

            await message.answer(f"<b>Botdan foydalanish uchun, quyidagi kanallarga obuna bo'ling: </b>\n\n"
                         f"<i>{channels_format}</i>",
                         reply_markup=check_button,
                         disable_web_page_preview=True)

    msg = f"{message.from_user.full_name} bazaga qo'shildi"
    await bot.send_message(chat_id=ADMINS[0], text=msg)

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅ <i><b>{channel.title}</b> kanalga obuna bo'lgansiz!\n\nO'zingizga yoqqan fontni tanlang!</i>"
            await call.message.delete()
            await call.message.answer(result, reply_markup=fonts_menu, disable_web_page_preview=True)

        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌ <i><b>{channel.title}</b> kanalga obuna bo'lmagansiz. </i>"
                       f"<a href='{invite_link}'> <i><b>Obuna bo'ling!</b></i></a>\n\n")
            await call.message.answer(result, disable_web_page_preview=True)