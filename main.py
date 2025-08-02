from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Play Movie Tycoon", web_app=WebAppInfo(url="https://your-webapp-url.vercel.app"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to Movie Tycoon!", reply_markup=reply_markup)

app = ApplicationBuilder().token("7052220530:AAHEap-IF4xlX9Jb_qSRPpLyCiKa7SbYlEM").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
