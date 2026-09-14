import os
import telebot
from telebot import types

TOKEN = "8390893863:AAEZFhkYG0l22pWGNr3rounwkUChtxneOPc"
ADMIN_ID = 7122529232   # آیدی عددی مدیر ربات را اینجا بگذار
bot = telebot.TeleBot(TOKEN)

# -------------------------
# منوی اصلی
# -------------------------
def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("ثبت سفارش دستگاه", "ثبت سفارش طراحی ماشین‌آلات")
    menu.add("معرفی دستگاه‌های تولیدی")
    menu.add("درباره ما", "شماره تماس")
    return menu

# -------------------------
# منوی معرفی دستگاه‌ها
# -------------------------
def device_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("CNC فرز تخت", "CNC تراش")
    menu.add("دستگاه منبت", "دستگاه خراطی")
    menu.add("بازگشت")
    return menu

# -------------------------
# شروع ربات
# -------------------------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "سلام! به ربات گروه تولیدی رخسار ماشین خوش اومدی 🌸\n"
        "لطفاً از منوی زیر انتخاب کن:",
        reply_markup=main_menu()
    )

# -------------------------
# هندل پیام‌ها
# -------------------------
@bot.message_handler(func=lambda m: True)
def handler(message):

    # --- ثبت سفارش دستگاه ---
    if message.text == "ثبت سفارش دستگاه":
        msg = bot.send_message(
            message.chat.id,
            "لطفاً نوع دستگاه مورد نیاز، مشخصات و شماره تماس خود را ارسال کنید.\n"
            "اگر عکس هم داری، ارسال کن تا مدیر بررسی کند."
        )
        bot.register_next_step_handler(msg, save_order)

    # --- ثبت سفارش طراحی ماشین‌آلات ---
    elif message.text == "ثبت سفارش طراحی ماشین‌آلات":
        msg = bot.send_message(
            message.chat.id,
            "لطفاً توضیحات کامل پروژه طراحی، جنس، ابعاد و شماره تماس را ارسال کن.\n"
            "در صورت نیاز عکس هم ارسال کن."
        )
        bot.register_next_step_handler(msg, save_design)

    # --- معرفی دستگاه‌ها ---
    elif message.text == "معرفی دستگاه‌های تولیدی":
        bot.send_message(
            message.chat.id,
            "کدوم دستگاه رو می‌خوای ببینی؟",
            reply_markup=device_menu()
        )

    # --- CNC فرز تخت ---
    elif message.text == "CNC فرز تخت":
        bot.send_message(
            message.chat.id,
            "🛠 **CNC فرز تخت**\n"
            "مناسب برای برش، حکاکی، قالب‌سازی و تولید قطعات دقیق.\n"
            "کاربرد در چوب، آلومینیوم، کامپوزیت و فلزات سبک."
        )

    # --- CNC تراش ---
    elif message.text == "CNC تراش":
        bot.send_message(
            message.chat.id,
            "🔧 **CNC تراش**\n"
            "مناسب برای تولید قطعات گرد، شفت‌ها، بوش‌ها و قطعات دقیق صنعتی."
        )

    # --- دستگاه منبت ---
    elif message.text == "دستگاه منبت":
        bot.send_message(
            message.chat.id,
            "🪵 **دستگاه منبت CNC**\n"
            "برای تولید طرح‌های سه‌بعدی روی چوب، مبل‌سازی، دکوراسیون و هنرهای چوبی."
        )

    # --- دستگاه خراطی ---
    elif message.text == "دستگاه خراطی":
        bot.send_message(
            message.chat.id,
            "🪚 **دستگاه خراطی CNC**\n"
            "مناسب برای تولید پایه‌میز، نرده، قطعات گرد چوبی و طرح‌های خاص."
        )

    # --- درباره ما ---
    elif message.text == "درباره ما":
        bot.send_message(
            message.chat.id,
            "🏭 **گروه تولیدی رخسار ماشین**\n"
            "تولیدکننده انواع دستگاه‌های CNC، طراحی ماشین‌آلات صنعتی، ساخت سفارشی تجهیزات.\n"
            "با بیش از ۱۵ سال تجربه در صنعت ماشین‌سازی."
        )

    # --- شماره تماس ---
    elif message.text == "شماره تماس":
        bot.send_message(
            message.chat.id,
            "📞 شماره تماس پشتیبانی:\n**09150447201**"
        )

    # --- بازگشت ---
    elif message.text == "بازگشت":
        bot.send_message(
            message.chat.id,
            "به منوی اصلی برگشتی 🌸",
            reply_markup=main_menu()
        )

    else:
        bot.send_message(
            message.chat.id,
            "لطفاً از منوی زیر انتخاب کن:",
            reply_markup=main_menu()
        )

# -------------------------
# ذخیره سفارش دستگاه
# -------------------------
def save_order(message):
    if message.photo:
        file_id = message.photo[-1].file_id
        bot.send_photo(ADMIN_ID, file_id, caption=f"سفارش دستگاه:\n{message.caption}")
    else:
        bot.send_message(ADMIN_ID, f"سفارش دستگاه:\n{message.text}")

    bot.send_message(message.chat.id, "سفارش شما ثبت شد و برای مدیر ارسال گردید 🌸")

# -------------------------
# ذخیره سفارش طراحی
# -------------------------
def save_design(message):
    if message.photo:
        file_id = message.photo[-1].file_id
        bot.send_photo(ADMIN_ID, file_id, caption=f"سفارش طراحی:\n{message.caption}")
    else:
        bot.send_message(ADMIN_ID, f"سفارش طراحی:\n{message.text}")

    bot.send_message(message.chat.id, "سفارش طراحی شما ثبت شد و برای مدیر ارسال شد 🌸")

# -------------------------
# اجرای ربات
# -------------------------
bot.polling()
