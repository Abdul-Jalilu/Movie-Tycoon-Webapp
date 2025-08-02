from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Play Movie Tycoon", web_app=WebAppInfo(url="movie-tycoon-webapp.vercel.app"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎉 Welcome to Movie Tycoon!\n\nClick the button below to launch the game and start building your movie empire.",
        reply_markup=reply_markup
    )

# WebAppData handler
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data  # This is the string sent from the web app
    await update.message.reply_text(f"🎬 Your movie result: {data}")

# Bot setup
app = ApplicationBuilder().token("7052220530:AAHEap-IF4xlX9Jb_qSRPpLyCiKa7SbYlEM").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
app.run_polling()

