import telebot
TOKEN = "8390893863:AAEZFhkYG0l22pWGNr3rounwkUChtxneOPc"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام عزیزم، ثبت سفارش ماشین سی ان سی اینجاست 🌸")


ADMIN_ID = 7122529232
bot.polling()
