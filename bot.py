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
    menu.add("ثبت سفارش دستگاه", "ثبت سفارش طراحی و ساخت ماشین‌آلات")
    menu.add("ثبت سفارش طراحی قطعه", "ثبت سفارش طراحی و ساخت قطعه")
    menu.add("معرفی دستگاه‌های تولیدی")
    menu.add("درباره ما", "شماره تماس")
    return menu

# -------------------------
# منوی معرفی دستگاه‌ها
# -------------------------
def device_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("CNC فرز تخت", "CNC تراش")
    menu.add("CNC تخت", "دستگاه منبت", "دستگاه خراطی")
    menu.add("بازگشت")
    return menu

# -------------------------
# شروع ربات
# -------------------------
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "سلام! به ربات گروه تولیدی رخسار ماشین خوش آمدید 🫡\n"
        "لطفاً از منوی زیر انتخاب کنید:",
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
            "لطفاً نوع دستگاه، توضیحات کامل و شماره تماس را ارسال کنید.\n"
            "در صورت نیاز عکس هم ارسال کنید."
        )
        bot.register_next_step_handler(msg, save_order_device)

    # --- ثبت سفارش طراحی و ساخت ماشین‌آلات ---
    elif message.text == "ثبت سفارش طراحی و ساخت ماشین‌آلات":
        msg = bot.send_message(
            message.chat.id,
            "لطفاً توضیحات پروژه، ابعاد، جنس، نیازهای فنی و شماره تماس را ارسال کنید.\n"
            "در صورت نیاز عکس هم ارسال کنید."
        )
        bot.register_next_step_handler(msg, save_design_machine)

    # --- ثبت سفارش طراحی قطعه ---
    elif message.text == "ثبت سفارش طراحی قطعه":
        msg = bot.send_message(
            message.chat.id,
            "لطفاً مشخصات قطعه، ابعاد، جنس و شماره تماس را ارسال کنید.\n"
            "اگر عکس یا نقشه دارید، ارسال کنید."
        )
        bot.register_next_step_handler(msg, save_design_part)

    # --- ثبت سفارش طراحی و ساخت قطعه ---
    elif message.text == "ثبت سفارش طراحی و ساخت قطعه":
        msg = bot.send_message(
            message.chat.id,
            "لطفاً توضیحات کامل ساخت قطعه، جنس، ابعاد و شماره تماس را ارسال کنید.\n"
            "در صورت نیاز عکس هم ارسال کنید."
        )
        bot.register_next_step_handler(msg, save_build_part)

    # --- معرفی دستگاه‌ها ---
    elif message.text == "معرفی دستگاه‌های تولیدی":
        bot.send_message(
            message.chat.id,
            "کدام دستگاه را می‌خواهید ببینید؟",
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

    # --- CNC تخت ---
    elif message.text == "CNC تخت":
        bot.send_message(
            message.chat.id,
            "⚙️ **CNC تخت**\n"
            "مناسب برای برش و حکاکی صفحات بزرگ چوب، MDF و کامپوزیت."
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
            "تولیدکننده انواع دستگاه‌های CNC، طراحی ماشین‌آلات صنعتی و ساخت سفارشی تجهیزات.\n"
            "بزودی."
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
            "به منوی اصلی برگشتید 😊",
            reply_markup=main_menu()
        )

    else:
        bot.send_message(
            message.chat.id,
            "لطفاً از منوی زیر انتخاب کنید:",
            reply_markup=main_menu()
        )

# -------------------------
# ذخیره سفارش‌ها
# -------------------------

def forward_to_admin(prefix, message):
    if message.photo:
        file_id = message.photo[-1].file_id
        bot.send_photo(ADMIN_ID, file_id, caption=f"{prefix}\n{message.caption}")
    else:
        bot.send_message(ADMIN_ID, f"{prefix}\n{message.text}")

    bot.send_message(message.chat.id, "سفارش شما ثبت شد و برای مدیر ارسال گردید 🌹")

def save_order_device(message):
    forward_to_admin("سفارش دستگاه:", message)

def save_design_machine(message):
    forward_to_admin("سفارش طراحی و ساخت ماشین‌آلات:", message)

def save_design_part(message):
    forward_to_admin("سفارش طراحی قطعه:", message)

def save_build_part(message):
    forward_to_admin("سفارش طراحی و ساخت قطعه:", message)

# -------------------------
# اجرای ربات
# -------------------------
bot.polling()
