import os
import telebot

TOKEN = os.getenv("8390893863:AAEZFhkYG0l22pWGNr3rounwkUChtxneOPc")
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 7122529232  # اینجا آیدی عددی خودت را بگذار

@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    text = f"پیام جدید از @{message.from_user.username}:\n\n{message.text}"
    bot.send_message(ADMIN_ID, text)
