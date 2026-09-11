import telebot
import os
TOKEN = "8390893863:AAEZFhkYG0l22pWGNr3rounwkUChtxneOPc"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام عزیزم، ثبت سفارش ماشین سی ان سی اینجاست 🌸")


ADMIN_ID = 7122529232  # اینجا آیدی عددی خودت را بگذار

@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    text = f"پیام جدید از @{message.from_user.username}:\n\n{message.text}"
    bot.send_message(ADMIN_ID, text)
bot.polling()
