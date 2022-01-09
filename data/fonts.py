def Changer (fonts, word):
    for key, value in fonts.items():
        word = word.replace(key, value)
    return (f'<code>{word}</code>')

def Font_1 (text):
    fonts = {
        'a':'ᗩ', 'b':'ᗷ', 'c':'ᑕ', 'd':'ᗞ',
        'e':'ᗴ', 'f':'ᖴ', 'g':'Ꮐ', 'h':'ᕼ',
        'i':'Ꮖ', 'j':'ᒍ', 'k':'Ꮶ', 'l':'Ꮮ',
        'm':'ᗰ', 'n':'ᑎ', 'o':'ᝪ', 'p':'ᑭ',
        'q':'ᑫ', 'r':'ᖇ', 's':'ᔑ', 't':'Ꭲ',
        'u':'ᑌ', 'v':'ᐯ', 'w':'ᗯ', 'x':'᙭',
        'y':'Ꭹ', 'z':'Ꮓ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_2 (text):
    fonts = {
        'a':'ᴀ', 'b':'ʙ', 'c':'ᴄ', 'd':'ᴅ',
        'e':'ᴇ', 'f':'ꜰ', 'g':'ɢ', 'h':'ʜ',
        'i':'ɪ', 'j':'ᴊ', 'k':'ᴋ', 'l':'ʟ',
        'm':'ᴍ', 'n':'ɴ', 'o':'ᴏ', 'p':'ᴘ',
        'q':'ǫ', 'r':'ʀ', 's':'s', 't':'ᴛ',
        'u':'ᴜ', 'v':'ᴠ', 'w':'ᴡ', 'x':'x',
        'y':'ʏ', 'z':'ᴢ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_3 (text):
    fonts = {
        'a':'α', 'b':'в', 'c':'¢', 'd':'∂',
        'e':'є', 'f':'ƒ', 'g':'g', 'h':'н',
        'i':'ι', 'j':'נ', 'k':'к', 'l':'ℓ',
        'm':'м', 'n':'η', 'o':'σ', 'p':'ρ',
        'q':'q', 'r':'я', 's':'ѕ', 't':'т',
        'u':'υ', 'v':'ν', 'w':'ω', 'x':'χ',
        'y':'у', 'z':'z'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_4 (text):
    fonts = {
        'a':'Á', 'b':'ß', 'c':'Č', 'd':'Ď',
        'e':'Ĕ', 'f':'Ŧ', 'g':'Ğ', 'h':'Ĥ',
        'i':'Ĩ', 'j':'Ĵ', 'k':'Ķ', 'l':'Ĺ',
        'm':'M', 'n':'Ń', 'o':'Ő', 'p':'P',
        'q':'Q', 'r':'Ŕ', 's':'Ś', 't':'Ť',
        'u':'Ú', 'v':'V', 'w':'Ŵ', 'x':'Ж',
        'y':'Ŷ', 'z':'Ź'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_5 (text):
    fonts = {
        'a':'𝓐', 'b':'𝔅', 'c':'𝔖', 'd':'𝔇',
        'e':'𝓔', 'f':'Ŧ', 'g':'ɠ', 'h':'𝕳',
        'i':'𝐼', 'j':'𝔍', 'k':'𝜿', 'l':'𝔏',
        'm':'𝔐', 'n':'𝜨', 'o':'𝔒', 'p':'𝔓',
        'q':'𝑄', 'r':'𝕽', 's':'𝕊', 't':'𝛵',
        'u':'𝔄', 'v':'𝝑', 'w':'𝑊', 'x':'𝔛',
        'y':'𝜸', 'z':'𝔗'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_6 (text):
    fonts = {
        'a':'aⷶ', 'b':'bⷡ', 'c':'cⷭ', 'd':'dͩ',
        'e':'eͤ', 'f':'fᷫ', 'g':'gᷚ', 'h':'hͪ',
        'i':'iͥ', 'j':'jᷯ', 'k':'kᷜ', 'l':'lᷝ',
        'm':'mͫ', 'n':'nᷡ', 'o':'oⷪ', 'p':'pᷮ',
        'q':'qᷘ',  'r':'rͬ', 's':'sᷤ', 't':'tͭ',
        'u':'uͧ', 'v':'vͮ', 'w':'wꙻ', 'x':'xͯ',
        'y':'yꙷ', 'z':'zᷦ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_7 (text):
    fonts = {
        'a':'A͜͡ꦿ', 'b':'B͜͡ꦿ', 'c':'C͜͡ꦿ', 'd':'D͜͡ꦿ',
        'e':'E͜͡ꦿ', 'f':'F͜͡ꦿ', 'g':'G͜͡ꦿ', 'h':'H͜͡ꦿ',
        'i':'I͜͡ꦿ', 'j':'J͜͡ꦿ', 'k':'K͜͡ꦿ', 'l':'L͜͡ꦿ',
        'm':'M͜͡ꦿ', 'n':'N͜͡ꦿ', 'o':'O͜͡ꦿ', 'p':'P͜͡ꦿ',
        'q':'Q͜͡ꦿ',  'r':'R͜͡ꦿ', 's':'S͜͡ꦿ', 't':'T͜͡ꦿ',
        'u':'U͜͡ꦿ', 'v':'V͜͡ꦿ','w':'W͜͡ꦿ', 'x':'X͜͡ꦿ',
        'y':'Y͜͡ꦿ', 'z':'Z͜͡ꦿ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_8 (text):
    fonts = {
        'a': '͜͡A͜͡', 'b': '͜͡B͜͡', 'c': '͜͡C͜͡', 'd': '͜͡D͜͡',
        'e': '͜͡E͜͡', 'f': '͜͡F͜͡', 'g': '͜͡G͜͡', 'h': '͜͡H͜͡',
        'i': '͜͡I͜͡', 'j': '͜͡J͜͡', 'k': '͜͡K͜͡', 'l': '͜͡L͜͡',
        'm': '͜͡M͜͡', 'n': '͜͡N͜͡', 'o': '͜͡O͜͡', 'p': '͜͡P͜͡',
        'q': '͜͡Q͜͡', 'r': '͜͡R͜͡', 's': '͜͡S͜͡', 't': '͜͡T͜͡',
        'u': '͜͡U͜͡', 'v': '͜͡V͜͡', 'w': '͜͡W͜͡', 'x': '͜͡X͜͡',
        'y': '͜͡Y͜͡', 'z': '͜͡Z͜͡'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_9 (text):
    fonts = {
        'a':'🅐', 'b':'🅑', 'c':'🅒', 'd':'🅓',
        'e':'🅔', 'f':'🅕', 'g':'🅖', 'h':'🅗',
        'i':'🅘', 'j':'🅙', 'k':'🅚', 'l':'🅛',
        'm':'🅜', 'n':'🅝', 'o':'🅞', 'p':'🅟',
        'q':'🅠',  'r':'🅡', 's':'🅢', 't':'🅣',
        'u':'🅤', 'v':'🅥','w':'🅦', 'x':'🅧',
        'y':'🅨', 'z':'🅩'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_10 (text):
    fonts = {
        'a':'ⓐ', 'b':'ⓑ', 'c':'ⓒ', 'd':'ⓓ',
        'e':'ⓔ', 'f':'ⓕ', 'g':'ⓖ', 'h':'ⓗ',
        'i':'ⓘ', 'j':'ⓙ', 'k':'ⓚ', 'l':'ⓛ',
        'm':'ⓜ', 'n':'ⓝ', 'o':'ⓞ', 'p':'ⓟ',
        'q':'ⓠ',  'r':'ⓡ', 's':'ⓢ', 't':'ⓣ',
        'u':'ⓤ', 'v':'ⓥ','w':'ⓦ', 'x':'ⓧ',
        'y':'ⓨ', 'z':'ⓩ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_11 (text):
    fonts = {
        'a':'A҈ ', 'b':'B҈ ', 'c':'C҈ ', 'd':'D҈ ',
        'e':'E҈ ', 'f':'F҈ ', 'g':'G҈ ', 'h':'H҈ ',
        'i':'I҈ ', 'j':'J҈ ', 'k':'K҈ ', 'l':'L҈ ',
        'm':'M҈ ', 'n':'N҈ ', 'o':'D҈ ', 'p':'P҈ ',
        'q':'Q҈ ', 'r':'R҈ ', 's':'S҈ ', 't':'T҈ ',
        'u':'U҈ ', 'v':'V҈ ', 'w':'W҈ ', 'x':'X҈ ',
        'y':'Y҈ ', 'z':'Z҈ '
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_12 (text):
    fonts = {
        'a':'A҉ ', 'b':'B҉ ', 'c':'C҉ ', 'd':'D҉ ',
        'e':'E҉ ', 'f':'F҉ ', 'g':'G҉ ', 'h':'H҉ ',
        'i':'I҉ ', 'j':'J҉ ', 'k':'K҉ ', 'l':'L҉ ',
        'm':'M҉ ', 'n':'N҉ ', 'o':'O҉ ', 'p':'P҉ ',
        'q':'Q҉ ',  'r':'R҉ ', 's':'S҉ ', 't':'T҉ ',
        'u':'U҉ ', 'v':'V҉ ','w':'W҉ ', 'x':'X҉ ',
        'y':'Y҉ ', 'z':'Z҉ '
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_13 (text):
    fonts = {
        'a':'ꪋ', 'b':'ଓ', 'c':'૮', 'd':'ᦔ',
        'e':'ꫀ', 'f':'ᠻ', 'g':'ꪮ', 'h':'ꫝ',
        'i':'ꪱ', 'j':'᧒', 'k':'ઝ', 'l':'ꪶ',
        'm':'ꪑ', 'n':'ꪀ', 'o':'᥆', 'p':'ƿ',
        'q':'ꪺ',  'r':'ꪚ', 's':'ઽ', 't':'ꫂ',
        'u':'ꪊ', 'v':'ꪜ','w':'ꪝ', 'x':'ꪎ',
        'y':'ꪗ', 'z':'ᤁ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_14 (text):
    fonts = {
        'a':'A⃟ ', 'b':'B⃟ ', 'c':'C⃟ ', 'd':'D⃟⃟ ',
        'e':'E⃟ ', 'f':'F⃟ ', 'g':'G⃟ ', 'h':'H⃟ ',
        'i':'I⃟ ', 'j':'J⃟ ', 'k':'K⃟ ', 'l':'L⃟ ',
        'm':'M⃟ ', 'n':'N⃟ ', 'o':'O⃟ ', 'p':'P⃟ ',
        'q':'Q⃟ ', 'r':'R⃟ ', 's':'S⃟ ', 't':'T⃟ ',
        'u':'U⃟ ', 'v':'V⃟ ', 'w':'W⃟ ', 'x':'X⃟ ',
        'y':'Y ⃟ ', 'z':'Z⃟ '
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_15 (text):
    fonts = {
        'a':'a̷', 'b':'b̷', 'c':'c̷', 'd':'d̷',
        'e':'e̷', 'f':'f̷', 'g':'g̷', 'h':'h̷',
        'i':'i̷', 'j':'j̷', 'k':'k̷', 'l':'l̷',
        'm':'m̷', 'n':'n̷', 'o':'o̷', 'p':'p̷',
        'q':'q̷', 'r':'r̷', 's':'s̷', 't':'t̷',
        'u':'u̷', 'v':'v̷', 'w':'w̷', 'x':'x̷',
        'y':'y̷', 'z':'z̷'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_16 (text):
    fonts = {
        'a':'🄰', 'b':'🄱', 'c':'🄲', 'd':'🄳',
        'e':'🄴', 'f':'🄵', 'g':'🄶', 'h':'🄷',
        'i':'🄸', 'j':'🄹', 'k':'🄺', 'l':'🄻',
        'm':'🄼', 'n':'🄽', 'o':'🄾', 'p':'🄿',
        'q':'🅀', 'r':'🅁', 's':'🅂', 't':'🅃',
        'u':'🅄', 'v':'🅅', 'w':'🅆', 'x':'🅇',
        'y':'🅈', 'z':'🅉'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_17 (text):
    fonts = {
        'a':'λ', 'b':'ß', 'c':'Ȼ', 'd':'ɖ',
        'e':'ε', 'f':'ʃ', 'g':'Ģ', 'h':'ħ',
        'i':'ί', 'j':'ĵ', 'k':'κ', 'l':'ι',
        'm':'ɱ', 'n':'ɴ', 'o':'Θ', 'p':'ρ',
        'q':'ƣ', 'r':'ર', 's':'Ș', 't':'τ',
        'u':'Ʋ', 'v':'ν', 'w':'ώ', 'x':'Χ',
        'y':'ϓ', 'z':'Հ'
    }

    word = text.lower()
    return (Changer(fonts, word))



def Font_18 (text):
    fonts = {
        'a':'ᴬ', 'b':'ᴮ', 'c':'ᶜ', 'd':'ᴰ',
        'e':'ᴱ', 'f':'ᶠ', 'g':'ᴳ', 'h':'ᴴ',
        'i':'ᴵ', 'j':'ᴶ', 'k':'ᴷ', 'l':'ᴸ',
        'm':'ᴹ', 'n':'ᴺ', 'o':'ᴼ', 'p':'ᴾ',
        'q':'ᵠ', 'r':'ᴿ', 's':'ˁ', 't':'ᵀ',
        'u':'ᵁ', 'v':'ᵛ', 'w':'ᵂ', 'x':'ˣ',
        'y':'ʸ', 'z':'ᶻ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_19 (text):
    fonts = {
        'a':'Ꭺ', 'b':'Ᏼ', 'c':'Ꮯ', 'd':'Ꭰ',
        'e':'Ꭼ', 'f':'Ғ', 'g':'Ꮐ', 'h':'Ꮋ',
        'i':'Ꮖ', 'j':'Ꭻ', 'k':'Ꮶ', 'l':'Ꮮ',
        'm':'Ꮇ', 'n':'Ν', 'o':'ϴ', 'p':'Ꮲ',
        'q':'Ϙ', 'r':'Ꭱ', 's':'Տ', 't':'Ͳ',
        'u':'Ⴎ', 'v':'Ꮩ', 'w':'Ꮤ', 'x':'Х',
        'y':'Ꮍ', 'z':'Ꮓ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_20 (text):
    fonts = {
        'a':'ꪋ', 'b':'ᙖ', 'c':'ᑕ', 'd':'ⅅ',
        'e':'ᕮ', 'f':'Բ', 'g':'ꮆ', 'h':'ℌ',
        'i':'Ⲓ', 'j':'ℐ', 'k':'Ḱ', 'l':'ℒ',
        'm':'ꪑ', 'n':'ꫜ', 'o':'۝', 'p':'ℙ',
        'q':'ℚ', 'r':'ℜ', 's':'ន', 't':'ͳ',
        'u':'ꪊ', 'v':'ꪜ', 'w':'ꪡ', 'x':'ꪎ',
        'y':'ꭹ', 'z':'Ɀ'
    }

    word = text.lower()
    return (Changer(fonts, word))



def Font_21 (text):
    fonts = {
        'a':' a꙰', 'b':' b꙰', 'c':' c꙰', 'd':' d꙰',
        'e':' e꙰', 'f':' f꙰', 'g':' g꙰', 'h':' h꙰',
        'i':' i꙰', 'j':' j꙰', 'k':' k꙰', 'l':' l꙰',
        'm':' m꙰', 'n':' n꙰', 'o':' o꙰', 'p':' p꙰',
        'q':' q꙰',  'r':' r꙰', 's':' s꙰', 't':' t꙰',
        'u':' u꙰', 'v':' v꙰', 'w':' w꙰', 'x':' x꙰',
        'y':' y꙰', 'z':' z꙰'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_22 (text):
    fonts = {
        'a':'Aᤢྀ', 'b':'Bᤢྀ', 'c':'Cᤢྀ', 'd':'Dᤢྀ',
        'e':'Eᤢྀ', 'f':'Fᤢྀ', 'g':'Gᤢྀ', 'h':'Hᤢྀ',
        'i':'Iᤢྀ', 'j':'Jᤢྀ', 'k':'Kᤢྀ', 'l':'Lᤢྀ',
        'm':'Mᤢྀ', 'n':'Nᤢྀ', 'o':'Oᤢྀ', 'p':'Pᤢྀ',
        'q':'Qᤢྀ', 'r':'Rᤢྀ', 's':'Sᤢྀ', 't':'Tᤢྀ',
        'u':'Uᤢྀ', 'v':'Vᤢྀ', 'w':'Wᤢྀ', 'x':'Xᤢྀ',
        'y':'Yᤢྀ', 'z':'Zᤢྀ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_23 (text):
    fonts = {
        'a':'🇦 ', 'b':'🇧 ', 'c':'🇨 ', 'd':'🇩 ',
        'e':'🇪 ', 'f':'🇫 ', 'g':'🇬 ', 'h':'🇭 ',
        'i':'🇮 ', 'j':'🇯 ', 'k':'🇰 ', 'l':'🇱 ',
        'm':'🇲 ', 'n':'🇳 ', 'o':'🇴 ', 'p':'🇵 ',
        'q':'🇶 ', 'r':'🇷 ', 's':'🇸 ', 't':'🇹 ',
        'u':'🇻 ', 'v':'🇺 ', 'w':'🇼 ', 'x':'🇽 ',
        'y':'🇾 ', 'z':'🇿 '
    }

    word = text.lower()
    return (Changer(fonts, word))



def Font_24 (text):
    fonts = {
        'a':'ⓐ', 'b':'ⓑ', 'c':'ⓒ', 'd':'ⓓ',
        'e':'ⓔ', 'f':'ⓕ', 'g':'ⓖ', 'h':'ⓗ',
        'i':'ⓘ', 'j':'ⓙ', 'k':'ⓚ', 'l':'ⓛ',
        'm':'ⓜ', 'n':'ⓝ', 'o':'ⓞ', 'p':'ⓟ',
        'q':'ⓠ',  'r':'ⓡ', 's':'ⓢ', 't':'ⓣ',
        'u':'ⓤ', 'v':'ⓥ','w':'ⓦ', 'x':'ⓧ',
        'y':'ⓨ', 'z':'ⓩ'
    }

    word = text.lower()
    return (Changer(fonts, word))



def Font_25 (text):
    fonts = {
        'a':'͜͡🅐͜͡', 'b':'͜͡🅑͜͡', 'c':'͜͡🅒͜͡', 'd':'͜͡🅓͜͡',
        'e':'͜͡🅔͜͡', 'f':'͜͡🅕͜͡', 'g':'͜͡🅖͜͡', 'h':'͜͡🅗͜͡',
        'i':'͜͡🅘͜͡', 'j':'͜͡🅙͜͡', 'k':'͜͡🅚͜͡', 'l':'͜͡🅛͜͡',
        'm':'͜͡🅜͜͡', 'n':'͜͡🅝͜͡', 'o':'͜͡🅞͜͡', 'p':'͜͡🅟͜͡',
        'q':'͜͡🅠͜͡',  'r':'͜͡🅡͜͡', 's':'͜͡🅢͜͡', 't':'͜͡🅣͜͡',
        'u':'͜͡🅤͜͡', 'v':'͜͡🅥͜͡','w':'͜͡🅦͜͡', 'x':'͜͡🅧͜͡',
        'y':'͜͡🅨͜͡', 'z':'͜͡🅩͜͡'
    }

    word = text.lower()
    return (Changer(fonts, word))



def Font_26 (text):
    fonts = {
        'a':'a̷̷', 'b':'b̷̷', 'c':'c̷̷', 'd':'d̷̷',
        'e':'e̷̷', 'f':'f̷̷', 'g':'g̷̷', 'h':'h̷̷',
        'i':'i̷̷', 'j':'j̷̷', 'k':'k̷̷', 'l':'l̷̷',
        'm':'m̷̷', 'n':'n̷̷', 'o':'o̷̷', 'p':'p̷̷',
        'q':'q̷̷',  'r':'r̷̷', 's':'s̷̷', 't':'t̷̷',
        'u':'u̷̷', 'v':'v̷̷','w':'w̷̷', 'x':'x̷̷',
        'y':'y̷̷', 'z':'z̷̷'
    }

    word = text.lower()
    return (Changer(fonts, word))



def Font_27 (text):
    fonts = {
        'a':'ᴀ࿆ᮀ', 'b':'ʙ࿆ᮀ', 'c':'ᴄ࿆ᮀ', 'd':'ᴅ࿆ᮀ',
        'e':'ᴇ࿆ᮀ', 'f':'ꜰ࿆ᮀ', 'g':'ɢ࿆ᮀ', 'h':'ʜ࿆ᮀ',
        'i':'ɪ࿆ᮀ', 'j':'ᴊ࿆ᮀ', 'k':'ᴋ࿆ᮀ', 'l':'ʟ࿆ᮀ',
        'm':'ᴍ࿆ᮀ', 'n':'ɴ࿆ᮀ', 'o':'ᴏ࿆ᮀ', 'p':'ᴘ࿆ᮀ',
        'q':'ǫ࿆ᮀ',  'r':'ʀ࿆ᮀ', 's':'s࿆ᮀ', 't':'ᴛ࿆ᮀ',
        'u':'ᴜ࿆ᮀ', 'v':'ᴠ࿆ᮀ','w':'ᴡ࿆ᮀ', 'x':'x࿆ᮀ',
        'y':'ʏ࿆ᮀ', 'z':'ᴢ࿆ᮀ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_28 (text):
    fonts = {
        'a':'ᥲྀᤢ', 'b':'δྀᤢ', 'c':'ᥴྀᤢ', 'd':'ɗྀᤢ',
        'e':'ᥱྀᤢ', 'f':'fྀᤢ', 'g':'gྀᤢ', 'h':'ɦྀᤢ',
        'i':'iྀᤢ', 'j':'jྀᤢ', 'k':'κྀᤢ', 'l':'ᥣྀᤢ',
        'm':'ⲙྀᤢ', 'n':'ᥒྀᤢ', 'o':'᧐ྀᤢ̷', 'p':'ρྀᤢ',
        'q':'qྀᤢ',  'r':'rྀᤢ', 's':'sྀᤢ', 't':'ᴛྀᤢ',
        'u':'ᥙྀᤢ', 'v':'᥎ྀᤢ','w':'ᥕྀᤢ', 'x':'᥊ྀᤢ',
        'y':'yྀᤢ̷', 'z':'ᤁྀᤢ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_29 (text):
    fonts = {
        'a':'ᥲོ͢', 'b':'δོ͢', 'c':'ᥴོ͢', 'd':'ɗོ͢',
        'e':'ᥱོ͢', 'f':'fོ͢', 'g':'gོ͢', 'h':'ɦོ͢',
        'i':'iོ͢', 'j':'jོ͢', 'k':'κོ͢', 'l':'ᥣོ͢',
        'm':'ⲙོ͢', 'n':'ᥒོ͢', 'o':'᧐ོ͢', 'p':'ρོ͢',
        'q':'qོ͢',  'r':'rོ͢', 's':'sོ͢', 't':'ᴛོ͢',
        'u':'ᥙོ͢', 'v':'᥎ོ͢','w':'ᥕོ͢', 'x':'᥊ོ͢',
        'y':'yོ͢', 'z':'ᤁོ͢'
    }

    word = text.lower()
    return (Changer(fonts, word))




def Font_30 (text):
    fonts = {
        'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓',
        'E': '𝓔', 'F': '𝓕', 'G': '𝓖', 'H': '𝓗',
        'I': '𝓘', 'J': '𝓙', 'K': '𝓚', 'L': '𝓛',
        'M': '𝓜', 'N': '𝓝', 'O': '𝓞', 'P': '𝓟',
        'Q': '𝓠', 'R': '𝓡', 'S': '𝓢', 'T': '𝓣',
        'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧',
        'Y': '𝓨', 'Z': '𝓩',

        'a':'𝓪', 'b':'𝓫', 'c':'𝓬', 'd':'𝓭',
        'e':'𝓮', 'f':'𝓯', 'g':'𝓰', 'h':'𝓱',
        'i':'𝓲', 'j':'𝓳', 'k':'𝓴', 'l':'𝓵',
        'm':'𝓶', 'n':'𝓷', 'o':'𝓸', 'p':'𝓹',
        'q':'𝓺',  'r':'𝓻', 's':'𝓼', 't':'𝓽',
        'u':'𝓾', 'v':'𝓿','w':'𝔀', 'x':'𝔁',
        'y':'𝔂', 'z':'𝔃'
    }

    word = text
    return (Changer(fonts, word))


def Font_31 (text):
    fonts = {
        'a':'𝖆', 'b':'𝖇', 'c':'𝖈', 'd':'𝖉',
        'e':'𝖊', 'f':'𝖋', 'g':'𝖌', 'h':'𝖍',
        'i':'𝖎', 'j':'𝖏', 'k':'𝖐', 'l':'𝖑',
        'm':'𝖒', 'n':'𝖓', 'o':'𝖔', 'p':'𝖕',
        'q':'𝖖',  'r':'𝖗', 's':'𝖘', 't':'𝖙',
        'u':'𝖚', 'v':'𝖛','w':'𝖜', 'x':'𝖝',
        'y':'𝛄', 'z':'𝖟'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Font_32 (text):
    fonts = {
        'A': '𝔸', 'B': '𝔹', 'C': 'ℂ', 'D': '𝔻',
        'E': '𝔼', 'F': '𝔽', 'G': '𝔾', 'H': 'ℍ',
        'I': '𝕀', 'J': '𝕁', 'K': '𝕂', 'L': '𝕃',
        'M': '𝕄', 'N': 'ℕ', 'O': '𝕆', 'P': 'ℙ',
        'Q': 'ℚ', 'R': 'ℝ', 'S': '𝕊', 'T': '𝕋',
        'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏',
        'Y': '𝕐', 'Z': 'ℤ',

        'a':'𝕒', 'b':'𝕓', 'c':'𝕔', 'd':'𝕕',
        'e':'𝕖', 'f':'𝕗', 'g':'𝕘', 'h':'𝕙',
        'i':'𝕚', 'j':'𝕛', 'k':'𝕜', 'l':'𝕝',
        'm':'𝕞', 'n':'𝕟', 'o':'𝕠', 'p':'𝕡',
        'q':'𝕢',  'r':'𝕣', 's':'𝕤', 't':'𝕥',
        'u':'𝕦', 'v':'𝕧','w':'𝕨', 'x':'𝕩',
        'y':'𝕪', 'z':'𝕫'
    }

    word = text
    return (Changer(fonts, word))


def Font_33 (text):
    fonts = {
        'A': '𝐴', 'B': '𝐵', 'C': '𝐶', 'D': '𝐷',
        'E': '𝐸', 'F': '𝐹', 'G': '𝐺', 'H': '𝐻',
        'I': '𝐼', 'J': '𝐽', 'K': '𝐾', 'L': '𝐿',
        'M': '𝑀', 'N': '𝑁', 'O': '𝑂', 'P': '𝑃',
        'Q': '𝑄', 'R': '𝑅', 'S': '𝑆', 'T': '𝑇',
        'U': '𝑈', 'V': '𝑉', 'W': '𝑊', 'X': '𝑋',
        'Y': '𝑌', 'Z': '𝑍',

        'a':'𝑎', 'b':'𝑏', 'c':'𝑐', 'd':'𝑑',
        'e':'𝑒', 'f':'𝑓', 'g':'𝑔', 'h':'ℎ',
        'i':'𝑖', 'j':'𝑗', 'k':'𝑘', 'l':'𝑙',
        'm':'𝑚', 'n':'𝑛', 'o':'𝑜', 'p':'𝑝',
        'q':'𝑞',  'r':'𝑟', 's':'𝑠', 't':'𝑡',
        'u':'𝑢', 'v':'𝑣','w':'𝑤', 'x':'𝑥',
        'y':'𝑦', 'z':'𝑧'
    }

    word = text
    return (Changer(fonts, word))


def Font_34 (text):
    fonts = {
        'a':'ᗣ', 'b':'ᙖ', 'c':'ᙅ', 'd':'ᗪ',
        'e':'ᙓ', 'f':'ᖴ', 'g':'ᘜ', 'h':'ᕼ',
        'i':'ᖗ', 'j':'ᒍ', 'k':'Ꮶ', 'l':'ᒐ',
        'm':'ᗰ', 'n':'ᘉ', 'o':'ᗝ', 'p':'ᗝ',
        'q':'ᘯ',  'r':'ᖇ', 's':'ᔕ', 't':'ᙢ',
        'u':'ᑌ', 'v':'ᐯ','w':'ᙡ', 'x':'ⵋ',
        'y':'Ꮍ', 'z':'ᘔ'
    }

    word = text.lower()
    return (Changer(fonts, word))


def Decoration(sym, text):
    for symvol in sym:
        done = symvol.replace(' ', text)
    return (f'<code>{done}</code>')

def Beauty (text):
    sym = {
        '༺ ༻', '★᭄ꦿ᭄ꦿ ★᭄ꦿ᭄ꦿ'
    }
    return (Decoration(sym, text))