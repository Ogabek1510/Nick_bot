from aiogram import types
from data.fonts import *
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import fonts_menu, back
from states.fontStates import Fonts
from loader import dp


@dp.message_handler(text=('🔙 Ortga'))
async def go_back(message: types.Message):
    await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)


@dp.message_handler(text=('ᗰᏆᖇᗩᏦᏆ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_1.set()

@dp.message_handler(state=Fonts.font_1)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    #elif message.text=='/start':
    #    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_1(message.text))


@dp.message_handler(text=('ᴍɪʀᴀᴋɪ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_2.set()

@dp.message_handler(state=Fonts.font_2)
async def calling(message: types.Message, state: FSMContext):
    if message.text == '🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_2(message.text))


@dp.message_handler(text=('мιяαкι'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_3.set()

@dp.message_handler(state=Fonts.font_3)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_3(message.text))


@dp.message_handler(text=('MĨŔÁĶĨ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_4.set()

@dp.message_handler(state=Fonts.font_4)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_4(message.text))


@dp.message_handler(text=('𝔐𝐼𝕽𝓐𝜿𝐼'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_5.set()

@dp.message_handler(state=Fonts.font_5)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_5(message.text))


@dp.message_handler(text=('mͫiͥrͬaⷶkᷜiͥͭ-'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_6.set()

@dp.message_handler(state=Fonts.font_6)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_6(message.text))


@dp.message_handler(text=('M͜͡ꦿI͜͡ꦿR͜͡ꦿA͜͡ꦿK͜͡ꦿI͜͡ꦿ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_7.set()

@dp.message_handler(state=Fonts.font_7)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_7(message.text))


@dp.message_handler(text=('͜͡M͜͡I͜͡R͜͡A͜͡K͜͡I͜͡'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_8.set()

@dp.message_handler(state=Fonts.font_8)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_8(message.text))


@dp.message_handler(text=('🅜🅘🅡🅐🅚🅘'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_9.set()

@dp.message_handler(state=Fonts.font_9)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_9(message.text))


@dp.message_handler(text=('ⓜⓘⓡⓐⓚⓘ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_10.set()

@dp.message_handler(state=Fonts.font_10)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_10(message.text))


@dp.message_handler(text=('M҈ I҈ R҈ A҈ K҈ I҈'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_11.set()

@dp.message_handler(state=Fonts.font_11)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_11(message.text))


@dp.message_handler(text=('M҉ I҉ R҉ A҉ K҉ I҉'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_12.set()

@dp.message_handler(state=Fonts.font_12)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_12(message.text))


@dp.message_handler(text=('ꪑꪱꪚꪋઝꪱ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_13.set()

@dp.message_handler(state=Fonts.font_13)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_13(message.text))


@dp.message_handler(text=('M⃟ I⃟ R⃟ A⃟ K⃟ I⃟'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_14.set()

@dp.message_handler(state=Fonts.font_14)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_14(message.text))


@dp.message_handler(text=('m̷i̷r̷a̷k̷i̷'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_15.set()

@dp.message_handler(state=Fonts.font_15)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_15(message.text))


@dp.message_handler(text=('🄼🄸🅁🄰🄺🄸'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_16.set()

@dp.message_handler(state=Fonts.font_16)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_16(message.text))


@dp.message_handler(text=('ɱίરλκί'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_17.set()

@dp.message_handler(state=Fonts.font_17)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_17(message.text))


@dp.message_handler(text=('ᴹᴵᴿᴬᴷᴵ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_18.set()

@dp.message_handler(state=Fonts.font_18)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_18(message.text))



@dp.message_handler(text=('ᎷᏆᎡᎪᏦᏆ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_19.set()

@dp.message_handler(state=Fonts.font_19)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_19(message.text))


@dp.message_handler(text=('ꪑⲒℜꪋḰⲒ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_20.set()

@dp.message_handler(state=Fonts.font_20)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_20(message.text))



@dp.message_handler(text=('m꙰ i꙰ r꙰ a꙰ k꙰ i꙰'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_21.set()

@dp.message_handler(state=Fonts.font_21)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_21(message.text))



@dp.message_handler(text=('MᤢྀIᤢྀRᤢྀAᤢྀKᤢྀIᤢྀ'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_22.set()

@dp.message_handler(state=Fonts.font_22)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_22(message.text))



@dp.message_handler(text=('🇲 🇮 🇷 🇦 🇰 🇮'))
async def font1(message: types.Message):
    await message.answer("Biror so'z yoki matn kiriting!", reply_markup=back)
    await Fonts.font_23.set()

@dp.message_handler(state=Fonts.font_23)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer("Asosiy menyudasiz!", reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=fonts_menu)
    else:
        await message.reply(Font_23(message.text))