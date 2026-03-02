import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Shop Queue Bot is running.")

# Queue command (test)
async def queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Queue feature coming next.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("queue", queue))

    app.run_polling()

if __name__ == "__main__":
    main()