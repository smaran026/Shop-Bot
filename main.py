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

buyers_per_week = 7
current_index = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Citadel rotation bot active.")

async def week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buyers = []
    for i in range(buyers_per_week):
        buyers.append(members[(current_index + i) % len(members)])

    text = "This week buyers:\n"
    for b in buyers:
        text += f"- {b}\n"

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("week", week))

app.run_polling()
