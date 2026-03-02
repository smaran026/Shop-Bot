import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

members = [
"Руслан",
"Dimario",
"madness",
"Эд",
"CITADEL - VIP",
"Татьяна Русакова",
"Умар Раисов",
"Nikolay Kopnin",
"Jonce",
"Vladimir",
"Если честно...",
"Idris Mayar",
"Горыныч",
"@AK1200083",
"DeletE Маккейн",
"Smaran Shetty",
"Максим",
"Антон Суханов",
"Александр",
"Юрий",
"AIFFAI",
"Владимир",
"Эдгар Левин"
]

current_index = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Shop Queue Bot is running.")

async def queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Current Queue:\n\n"
    for i, m in enumerate(members):
        if i == current_index:
            text += f"{i+1}. {m} ← NEXT\n"
        else:
            text += f"{i+1}. {m}\n"
    await update.message.reply_text(text)

async def next_buyer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_index
    current_index = (current_index + 1) % len(members)
    await update.message.reply_text(f"Next buyer: {members[current_index]}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("queue", queue))
app.add_handler(CommandHandler("next", next_buyer))

app.run_polling()
