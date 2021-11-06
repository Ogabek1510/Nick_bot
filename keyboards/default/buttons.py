from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons = [
    'ᗰᏆᖇᗩᏦᏆ', 'ᴍɪʀᴀᴋɪ', 'мιяαкι', 'MĨŔÁĶĨ',
    '𝔐𝐼𝕽𝓐𝜿𝐼', 'mͫiͥrͬaⷶkᷜiͥͭ-', 'M͜͡ꦿI͜͡ꦿR͜͡ꦿA͜͡ꦿK͜͡ꦿI͜͡ꦿ', '͜͡M͜͡I͜͡R͜͡A͜͡K͜͡I͜͡',
    '🅜🅘🅡🅐🅚🅘', 'ⓜⓘⓡⓐⓚⓘ', 'M҈ I҈ R҈ A҈ K҈ I҈', 'M҉ I҉ R҉ A҉ K҉ I҉',
    'ꪑꪱꪚꪋઝꪱ', 'M⃟ I⃟ R⃟ A⃟ K⃟ I⃟', 'm̷i̷r̷a̷k̷i̷', '🄼🄸🅁🄰🄺🄸', 'ɱίરλκί',
    'ᴹᴵᴿᴬᴷᴵ', 'ᎷᏆᎡᎪᏦᏆ', 'ꪑⲒℜꪋḰⲒ', 'm꙰ i꙰ r꙰ a꙰ k꙰ i꙰', '🇲 🇮 🇷 🇦 🇰 🇮'
]

fonts_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
for key in menu_buttons:
    fonts_menu.insert(KeyboardButton(text=key))


back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Ortga'),
        ],
    ],
    resize_keyboard=True
)