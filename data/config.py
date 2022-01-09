#from environs import Env

# environs kutubxonasidan foydalanish
#env = Env()
#env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
#BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
#ADMINS = env.list("ADMINS")  # adminlar ro'yxati
#IP = env.str("ip")  # Xosting ip manzili
#CHANNELS = ['@nima_nega_qanday']


import os

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = ['1254604313']
CHANNELS = ['@nima_nega_qanday']
