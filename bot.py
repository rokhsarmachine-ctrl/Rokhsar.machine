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
        "تولیدکننده انواع ماشین‌آلات CNC\n\n"
        "لطفاً از منوی زیر انتخاب کنید:",
        reply_markup=main_menu()
    )

# ============================================================
# 🛠 ثبت سفارش دستگاه CNC
# ============================================================
@bot.message_handler(func=lambda m: m.text == "🛠 ثبت سفارش دستگاه CNC")
def cnc_order(message):
    bot.send_message(message.chat.id, "لطفاً نام خود را وارد کنید:")
    bot.register_next_step_handler(message, cnc_get_name)

def cnc_get_name(message):
    name = message.text
    bot.send_message(message.chat.id, "شماره تماس را وارد کنید:")
    bot.register_next_step_handler(message, cnc_get_phone, name)

def cnc_get_phone(message, name):
    phone = message.text
    bot.send_message(message.chat.id, "نوع دستگاه و توضیحات سفارش را وارد کنید:")
    bot.register_next_step_handler(message, cnc_finish, name, phone)

def cnc_finish(message, name, phone):
    details = message.text

    bot.send_message(
        ADMIN_ID,
        f"📩 سفارش دستگاه CNC\n"
        f"👤 نام: {name}\n"
        f"📞 تماس: {phone}\n"
        f"📝 توضیحات: {details}"
    )

    bot.send_message(
        message.chat.id,
        "✔️ سفارش شما با موفقیت ثبت شد.\n"
        "به زودی با شما تماس گرفته می‌شود.",
        reply_markup=main_menu()
    )

# ============================================================
# 🧩 ثبت سفارش طراحی و ساخت قطعه
# ============================================================
@bot.message_handler(func=lambda m: m.text == "🧩 ثبت سفارش طراحی و ساخت قطعه")
def part_order(message):
    bot.send_message(message.chat.id, "لطفاً نام خود را وارد کنید:")
    bot.register_next_step_handler(message, part_get_name)

def part_get_name(message):
    name = message.text
    bot.send_message(message.chat.id, "شماره تماس را وارد کنید:")
    bot.register_next_step_handler(message, part_get_phone, name)

def part_get_phone(message, name):
    phone = message.text
    bot.send_message(message.chat.id, "توضیحات قطعه یا فایل/عکس را ارسال کنید:")
    bot.register_next_step_handler(message, part_finish, name, phone)

def part_finish(message, name, phone):
    details = message.text

    bot.send_message(
        ADMIN_ID,
        f"📩 سفارش طراحی و ساخت قطعه\n"
        f"👤 نام: {name}\n"
        f"📞 تماس: {phone}\n"
        f"📝 توضیحات: {details}"
    )

    bot.send_message(
        message.chat.id,
        "✔️ سفارش شما ثبت شد.\n"
        "به زودی با شما تماس گرفته می‌شود.",
        reply_markup=main_menu()
    )

# ============================================================
# ⚙️ معرفی انواع دستگاه‌های تولیدی
# ============================================================
@bot.message_handler(func=lambda m: m.text == "⚙️ معرفی انواع دستگاه‌های تولیدی")
def devices(message):
    bot.send_message(
        message.chat.id,
        "🔧 **معرفی کامل انواع دستگاه‌های CNC تولیدی رخسار ماشین** 🔧\n\n"

        "🔹 **CNC تراش**\n"
        "مناسب ساخت قطعات گرد، شفت‌ها، بوش‌ها، پولی‌ها و رزوه‌زنی داخلی و خارجی.\n"
        "✔️ دقت بالا\n✔️ ابزارگیری اتومات\n✔️ مناسب فولاد، آلومینیوم، برنج\n\n"

        "🔹 **CNC فرز تخت**\n"
        "برای شیارزنی، سوراخ‌کاری، براده‌برداری، سطح‌تراشی و ساخت قالب‌ها.\n"
        "✔️ دقت بالا در محورهای X,Y,Z\n✔️ مناسب قطعات پیچیده\n✔️ قابل استفاده روی فلز، چوب، پلاستیک\n\n"

        "🔹 **CNC منبت**\n"
        "مخصوص حکاکی و طراحی روی چوب و MDF.\n"
        "✔️ اجرای طرح‌های ظریف\n✔️ قابلیت طرح سه‌بعدی\n✔️ مناسب دکوراسیون و کابینت‌سازی\n\n"

        "🔹 **CNC خراطی**\n"
        "برای تولید قطعات گرد چوبی مثل پایه میز، نرده و قطعات تزئینی.\n"
        "✔️ سرعت بالا\n✔️ دقت در قطر و فرم\n✔️ مناسب تولید انبوه\n\n"

        "🔹 **CNC سنگ‌بری**\n"
        "برای برش، حکاکی و سوراخ‌کاری سنگ‌های ساختمانی و تزئینی.\n"
        "✔️ قدرت بالا\n✔️ مناسب سنگ‌های سخت مثل گرانیت\n✔️ حکاکی دقیق\n\n"

        "🔹 **CNC سفارشی**\n"
        "طراحی اختصاصی بر اساس نیاز کارخانه‌ها و خطوط تولید.\n"
        "✔️ قابلیت افزودن سنسور، سروو، پنوماتیک\n✔️ مناسب پروژه‌های صنعتی خاص\n"
    )

# ============================================================
# 📞 تماس با ما
# ============================================================
@bot.message_handler(func=lambda m: m.text == "📞 تماس با ما")
def contact(message):
    bot.send_message(
        message.chat.id,
        "📞 شماره تماس: 09150447201\n"
        "📍 آدرس: گروه تولیدی رخسار ماشین"
    )

# ============================================================
# ℹ️ درباره ما
# ============================================================
@bot.message_handler(func=lambda m: m.text == "ℹ️ درباره ما")
def about(message):
    bot.send_message(
        message.chat.id,
        "گروه تولیدی رخسار ماشین متخصص طراحی و ساخت انواع ماشین‌آلات CNC صنعتی.\n"
        " ساخت دستگاه‌های تراش، فرز، منبت، خراطی و سفارشی."
    )

# -------------------------
# اجرای ربات
# -------------------------
bot.polling()
