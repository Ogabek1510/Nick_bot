from aiogram import types
from data.fonts import *
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import fonts_menu, back
from keyboards.inline.decoration import next_button
from states.fontStates import Fonts
from loader import dp

font_txt = "📝️ <b>Biror so'z yoki matn kiriting!</b>"
back_txt = "🏠 <b>Asosiy menyudasiz!</b>"

@dp.message_handler(text=('🔙 Ortga'))
async def go_back(message: types.Message):
    await message.answer(back_txt, reply_markup=fonts_menu)


@dp.message_handler(text=('ᗰᏆᖇᗩᏦᏆ'))
async def font1(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_1.set()

@dp.message_handler(state=Fonts.font_1)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_1(message.text))


@dp.message_handler(text=('ᴍɪʀᴀᴋɪ'))
async def font2(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_2.set()

@dp.message_handler(state=Fonts.font_2)
async def calling(message: types.Message, state: FSMContext):
    if message.text == '🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_2(message.text))


@dp.message_handler(text=('мιяαкι'))
async def font3(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_3.set()

@dp.message_handler(state=Fonts.font_3)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_3(message.text))


@dp.message_handler(text=('MĨŔÁĶĨ'))
async def font4(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_4.set()

@dp.message_handler(state=Fonts.font_4)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_4(message.text))


@dp.message_handler(text=('𝔐𝐼𝕽𝓐𝜿𝐼'))
async def font5(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_5.set()

@dp.message_handler(state=Fonts.font_5)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_5(message.text))


@dp.message_handler(text=('mͫiͥrͬaⷶkᷜiͥͭ-'))
async def font6(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_6.set()

@dp.message_handler(state=Fonts.font_6)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_6(message.text))


@dp.message_handler(text=('M͜͡ꦿI͜͡ꦿR͜͡ꦿA͜͡ꦿK͜͡ꦿI͜͡ꦿ'))
async def font7(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_7.set()

@dp.message_handler(state=Fonts.font_7)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_7(message.text))


@dp.message_handler(text=('͜͡M͜͡I͜͡R͜͡A͜͡K͜͡I͜͡'))
async def font8(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_8.set()

@dp.message_handler(state=Fonts.font_8)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_8(message.text))


@dp.message_handler(text=('🅜🅘🅡🅐🅚🅘'))
async def font9(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_9.set()

@dp.message_handler(state=Fonts.font_9)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_9(message.text))


@dp.message_handler(text=('ⓜⓘⓡⓐⓚⓘ'))
async def font10(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_10.set()

@dp.message_handler(state=Fonts.font_10)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_10(message.text))


@dp.message_handler(text=('M҈ I҈ R҈ A҈ K҈ I҈'))
async def font11(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_11.set()

@dp.message_handler(state=Fonts.font_11)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_11(message.text))


@dp.message_handler(text=('M҉ I҉ R҉ A҉ K҉ I҉'))
async def font12(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_12.set()

@dp.message_handler(state=Fonts.font_12)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_12(message.text))


@dp.message_handler(text=('ꪑꪱꪚꪋઝꪱ'))
async def font13(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_13.set()

@dp.message_handler(state=Fonts.font_13)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_13(message.text))


@dp.message_handler(text=('M⃟ I⃟ R⃟ A⃟ K⃟ I⃟'))
async def font14(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_14.set()

@dp.message_handler(state=Fonts.font_14)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_14(message.text))


@dp.message_handler(text=('m̷i̷r̷a̷k̷i̷'))
async def font15(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_15.set()

@dp.message_handler(state=Fonts.font_15)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_15(message.text))


@dp.message_handler(text=('🄼🄸🅁🄰🄺🄸'))
async def font16(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_16.set()

@dp.message_handler(state=Fonts.font_16)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_16(message.text))


@dp.message_handler(text=('ɱίરλκί'))
async def font17(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_17.set()

@dp.message_handler(state=Fonts.font_17)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_17(message.text))


@dp.message_handler(text=('ᴹᴵᴿᴬᴷᴵ'))
async def font18(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_18.set()

@dp.message_handler(state=Fonts.font_18)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_18(message.text))



@dp.message_handler(text=('ᎷᏆᎡᎪᏦᏆ'))
async def font19(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_19.set()

@dp.message_handler(state=Fonts.font_19)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_19(message.text))


@dp.message_handler(text=('ꪑⲒℜꪋḰⲒ'))
async def font20(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_20.set()

@dp.message_handler(state=Fonts.font_20)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_20(message.text))



@dp.message_handler(text=('m꙰ i꙰ r꙰ a꙰ k꙰ i꙰'))
async def font21(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_21.set()

@dp.message_handler(state=Fonts.font_21)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_21(message.text))



@dp.message_handler(text=('MᤢྀIᤢྀRᤢྀAᤢྀKᤢྀIᤢྀ'))
async def font22(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_22.set()

@dp.message_handler(state=Fonts.font_22)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_22(message.text))



@dp.message_handler(text=('🇲 🇮 🇷 🇦 🇰 🇮'))
async def font23(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_23.set()

@dp.message_handler(state=Fonts.font_23)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_23(message.text))



@dp.message_handler(text=('ⓜⓘⓡⓐⓚⓘ'))
async def font24(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_24.set()

@dp.message_handler(state=Fonts.font_24)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_24(message.text))



@dp.message_handler(text=('͜͡🅜͜͡🅘͜͡🅡͜͡🅐͜͡🅚͜͡🅘͜͡'))
async def font25(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_25.set()

@dp.message_handler(state=Fonts.font_25)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_25(message.text))



@dp.message_handler(text=('m̷̷i̷̷r̷̷a̷̷k̷̷i̷̷'))
async def font26(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_26.set()

@dp.message_handler(state=Fonts.font_26)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_26(message.text))


@dp.message_handler(text=('ᴍ࿆ᮀɪ࿆ᮀʀ࿆ᮀᴀ࿆ᮀᴋ࿆ᮀɪ࿆ᮀ'))
async def font27(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_27.set()

@dp.message_handler(state=Fonts.font_27)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_27(message.text))


@dp.message_handler(text=('ⲙྀᤢiྀᤢrྀᤢᥲྀᤢκྀᤢiྀᤢ'))
async def font28(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_28.set()

@dp.message_handler(state=Fonts.font_28)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_28(message.text))


@dp.message_handler(text=('ⲙོ͢iོ͢rོ͢ᥲོ͢κོ͢iོ͢'))
async def font29(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_29.set()

@dp.message_handler(state=Fonts.font_29)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_29(message.text))


@dp.message_handler(text=('𝓜𝓲𝓻𝓪𝓴𝓲'))
async def font30(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_30.set()

@dp.message_handler(state=Fonts.font_30)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_30(message.text))


@dp.message_handler(text=('𝕸𝖎𝖗𝖆𝖐𝖎'))
async def font31(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_31.set()

@dp.message_handler(state=Fonts.font_31)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_31(message.text))


@dp.message_handler(text=('𝕄𝕚𝕣𝕒𝕜𝕚'))
async def font32(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_32.set()

@dp.message_handler(state=Fonts.font_32)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(font_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_32(message.text))


@dp.message_handler(text=('𝑀𝑖𝑟𝑎𝑘𝑖'))
async def font33(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_33.set()

@dp.message_handler(state=Fonts.font_33)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    elif message.text=='/start':
        await message.answer(f"Salom, {message.from_user.full_name}\nO'zingizga yoqqan fontni tanlang!", reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_33(message.text))


@dp.message_handler(text=('ᗰᖗᖇᗣᏦᖗ'))
async def font34(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.font_34.set()

@dp.message_handler(state=Fonts.font_34)
async def calling(message: types.Message, state: FSMContext):
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.reply(Font_34())


@dp.message_handler(text=("Ko'rinmas nik"))
async def hide_font(message: types.Message):
    await message.answer("<code>ㅤㅤㅤ</code>", reply_markup=fonts_menu)


@dp.message_handler(text=('Bezaklar'))
async def beauty(message: types.Message):
    await message.answer(font_txt, reply_markup=back)
    await Fonts.beauty.set()

@dp.message_handler(state=Fonts.beauty)
async def Decor(message: types.Message, state: FSMContext):
    sym = ['༺txt༻', '꧁༺txt༻꧂', ' ★᭄ꦿ᭄ꦿtxt★᭄ꦿ᭄ꦿ', '🌸 ⃝❤️txt🖤 ⃝🌸', '꯭꯭➣꯭꯭꙰🦋꙰🌸꙰ txt🌸꙰🕊️꙰',
           '𖣘‌ ‌✯txt✯‌ ‌𖣘', '1ᬼ⃝⃟⃘⃬꙰꙲꯭❤️⃝⃟⃬⃩🌸txt🌸⃝⃟⃘⃬꙰꙲꯭꯭❤️⃝⃟⃬⃩', '꯭🧸⃝🍫⃝  ꯭❀txt❀꯭ ᬼ꯭⃝⃪⃡🌸⃝🐻',
           '꧁🌺●•txt•●🌺꧂', '✸ ู๊ ู๊ ู๊ ู๊✪txt✪ ู๊ ู๊ ู๊ ู๊✸', '🌸   ♡ΞtxtΞ♡ ู๊ ู๊ ู๊🌸']
    global nicks
    nicks = (Decoration(message.text, sym))
    if message.text=='🔙 Ortga':
        await message.answer(back_txt, reply_markup=fonts_menu)
        await state.finish()
    else:
        await message.answer(nicks[0], reply_markup=next_button)

@dp.callback_query_handler(text="next", state=Fonts.beauty)
async def Checker(call: types.CallbackQuery):
    for text in nicks:
        await call.message.answer(text, reply_markup=next_button)
