import telebot
from telebot import types

# -------------------------
# تنظیمات اصلی
# -------------------------
TOKEN = "8390893863:AAEZFhkYG0l22pWGNr3rounwkUChtxneOPc"
ADMIN_ID = 7122529232
bot = telebot.TeleBot(TOKEN)

# -------------------------
# منوی اصلی
# -------------------------
def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("🛠 ثبت سفارش دستگاه CNC", "🧩 ثبت سفارش طراحی و ساخت قطعه")
    menu.add("⚙️ معرفی انواع دستگاه‌های تولیدی")
    menu.add("📞 تماس با ما", "ℹ️ درباره ما")
    return menu

# -------------------------
# شروع ربات
# -------------------------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 خوش آمدید به ربات گروه تولیدی رخسار ماشین\n"
        "تولیدکننده ماشین‌آلات CNC (تراش، فرز، منبت، خراطی)\n\n"
        "لطفاً از منوی زیر انتخاب کنید:",
        reply_markup=main_menu()
    )

# -------------------------
# هندل پیام‌ها
# -------------------------
@bot.message_handler(func=lambda m: True)
def menu_handler(message):

    # --- ثبت سفارش دستگاه CNC ---
    if message.text == "🛠 ثبت سفارش دستگاه CNC":
        bot.send_message(
            message.chat.id,
            "لطفاً نوع دستگاه مورد نظر (تراش، فرز، منبت، خراطی) و مشخصات فنی را وارد کنید."
        )
        bot.send_message(ADMIN_ID, f"📩 سفارش دستگاه CNC از کاربر: {message.from_user.id}")

    # --- ثبت سفارش طراحی و ساخت قطعه ---
    elif message.text == "🧩 ثبت سفارش طراحی و ساخت قطعه":
        bot.send_message(
            message.chat.id,
            "لطفاً توضیحات قطعه، نقشه یا فایل سه‌بعدی خود را ارسال کنید.\n"
            "📎 می‌توانید فایل CAD یا تصویر قطعه را هم بفرستید."
        )
        bot.send_message(ADMIN_ID, f"📩 سفارش طراحی قطعه از کاربر: {message.from_user.id}")

    # --- معرفی انواع دستگاه‌های تولیدی ---
    elif message.text == "⚙️ معرفی انواع دستگاه‌های تولیدی":
        bot.send_message(
            message.chat.id,
            "✅ دستگاه‌های تولیدی رخسار ماشین:\n\n"
            "🔹 CNC تراش: ساخت قطعات گرد و رزوه‌دار\n"
            "🔹 CNC فرز تخت: شیارزنی و سوراخ‌کاری دقیق\n"
            "🔹 CNC منبت: حکاکی و طراحی روی چوب و MDF\n"
            "🔹 CNC خراطی: تولید قطعات گرد چوبی\n"
            "🔹 CNC سنگ‌بری: برش و حکاکی سنگ\n"
            "🔹 CNC سفارشی: طراحی اختصاصی برای خطوط تولید\n"
        )

    # --- تماس با ما ---
    elif message.text == "📞 تماس با ما":
        bot.send_message(
            message.chat.id,
            "📞 شماره تماس: 09150447201\n"
            "📍 آدرس: قزوین، گروه تولیدی رخسار ماشین"
        )

    # --- درباره ما ---
    elif message.text == "ℹ️ درباره ما":
        bot.send_message(
            message.chat.id,
            "🔧 گروه تولیدی رخسار ماشین با تجربه در طراحی و ساخت ماشین‌آلات CNC، "
            "آماده ارائه خدمات تخصصی در زمینه تراشکاری، فرزکاری و ساخت دستگاه‌های صنعتی است."
        )

    else:
        bot.send_message(
            message.chat.id,
            "لطفاً از منوی زیر انتخاب کنید:",
            reply_markup=main_menu()
        )

# -------------------------
# اجرای ربات
# -------------------------
bot.polling()
