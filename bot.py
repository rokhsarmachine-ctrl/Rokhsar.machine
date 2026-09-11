import os
import telebot
from telebot import types

TOKEN ="8390893863:AAEZFhkYG0l22pWGNr3rounwkUChtxneOPc"
bot = telebot.TeleBot(TOKEN)

# آیدی تلگرام مدیر (تو)
ADMIN_ID = 7122529232

# -------------------------
# منوی اصلی
# -------------------------
def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("معرفی ماشین CNC")
    return menu

# -------------------------
# منوی معرفی CNC
# -------------------------
def cnc_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("تراش CNC", "فرز CNC")
    menu.add("بازگشت")
    return menu

# -------------------------
# شروع ربات
# -------------------------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
         سلام! به ربات معرفی ماشین  CNC خوش اومدی رخسار ماشین 🌸",
        reply_markup=main_menu()
    )

# -------------------------
# ارسال پیام کاربران به مدیر
# -------------------------
@bot.message_handler(content_types=['text', 'photo', 'voice', 'document'])
def forward_to_admin(message):

    # متن
    if message.content_type == 'text':
        bot.send_message(
            ADMIN_ID,
            f"پیام جدید از @{message.from_user.username}:\n\n{message.text}"
        )

    # عکس
    elif message.content_type == 'photo':
        bot.send_message(ADMIN_ID, f"یک عکس جدید از @{message.from_user.username}:")
        bot.send_photo(ADMIN_ID, message.photo[-1].file_id)

    # ویس
    elif message.content_type == 'voice':
        bot.send_message(ADMIN_ID, f"یک ویس جدید از @{message.from_user.username}:")
        bot.send_voice(ADMIN_ID, message.voice.file_id)

    # فایل
    elif message.content_type == 'document':
        bot.send_message(ADMIN_ID, f"یک فایل جدید از @{message.from_user.username}:")
        bot.send_document(ADMIN_ID, message.document.file_id)

    # بعد از ارسال پیام به مدیر، پیام کاربر هم هندل می‌شود
    menu_handler(message)

# -------------------------
# هندل پیام‌ها (منوها)
# -------------------------
def menu_handler(message):

    # --- منوی اصلی ---
    if message.text == "معرفی ماشین CNC":
        bot.send_message(
            message.chat.id,
            "کدوم بخش رو می‌خوای ببینی؟",
            reply_markup=cnc_menu()
        )

    # --- تراش CNC ---
    elif message.text == "تراش CNC":
        bot.send_message(
            message.chat.id,
            "🔧 معرفی تراش CNC\n\n"
            "برای ساخت قطعات گرد، شفت‌ها، بوش‌ها و قطعات دقیق استفاده می‌شود.\n"
            "مزایا:\n"
            "- دقت بالا\n"
            "- سرعت تولید زیاد\n"
            "- مناسب برای برنج، آلومینیوم، فولاد\n"
        )

    # --- فرز CNC ---
    elif message.text == "فرز CNC":
        bot.send_message(
            message.chat.id,
            "🛠 معرفی فرز CNC\n\n"
            "برای ساخت قطعات تخت، شیارها، سوراخ‌کاری و مدل‌سازی سه‌بعدی استفاده می‌شود.\n"
            "مزایا:\n"
            "- قابلیت ساخت قطعات پیچیده\n"
            "- مناسب برای قالب‌سازی\n"
            "- دقت بالا در محورهای X,Y,Z\n"
        )

    # --- بازگشت ---
    elif message.text == "بازگشت":
        bot.send_message(
            message.chat.id,
            "به منوی اصلی برگشتی 🌸",
            reply_markup=main_menu()
        )

# -------------------------
# اجرای ربات
# -------------------------
bot.polling()
