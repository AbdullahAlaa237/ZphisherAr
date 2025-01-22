import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, CallbackContext

# جلب التوكن من المتغيرات البيئية
TOKEN = os.getenv("7911314048:AAH4bf8lorhh5xoktK93hn-58TIUBZzuD74")

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("تشغيل Zphisher", callback_data='start_zphisher')],
        [InlineKeyboardButton("إيقاف Zphisher", callback_data='stop_zphisher')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("مرحبًا! استخدم الأزرار للتحكم في Zphisher.", reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == "start_zphisher":
        query.edit_message_text(text="جاري تشغيل Zphisher...")
        os.system("bash zphisher/zphisher.sh")  # تشغيل Zphisher
    elif query.data == "stop_zphisher":
        query.edit_message_text(text="تم إيقاف Zphisher.")
        os.system("pkill -f zphisher.sh")  # إيقاف Zphisher

def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
