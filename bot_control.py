import telebot
import os
import platform
from plyer import vibrator, battery, gps

TOKEN = '8229088402:AAFAsQV-fQlzaZYdXSevS1XvOdbfn-p164s'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    help_msg = """
🤖 **Android Remote System v1.0**
Daftar Perintah Awal:
/cek - Cek Status HP (Baterai & Info)
/getar - Tes Getar HP
/lokasi - Ambil GPS (Lat, Long)
/file - List file di folder aplikasi
/say [teks] - Buat HP bicara (TTS)
    """
    bot.reply_to(message, help_msg, parse_mode='Markdown')

# FITUR 1: Cek Baterai & Info
@bot.message_handler(commands=['cek'])
def cek_status(message):
    level = battery.status['percentage']
    is_charging = battery.status['is_charging']
    info = f"🔋 Baterai: {level}%\n⚡ Charging: {is_charging}\n📱 Model: {platform.machine()}"
    bot.reply_to(message, info)

# FITUR 2: Getar
@bot.message_handler(commands=['getar'])
def tes_getar(message):
    try:
        vibrator.vibrate(2)
        bot.reply_to(message, "📳 HP Bergetar selama 2 detik!")
    except:
        bot.reply_to(message, "Gagal akses vibrator!")

# FITUR 3: List File
@bot.message_handler(commands=['file'])
def list_file(message):
    files = os.listdir('.')
    bot.reply_to(message, "📂 Daftar File:\n" + "\n".join(files))

def start_bot():
    bot.polling(none_stop=True)
