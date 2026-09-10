import telebot

TOKEN = "توکن_ربات_اینجا"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام عزیزم، ثبت سفارش ماشین اینجاست 🌸")

bot.polling()
