import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

energy = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id
    energy[user] = 100
    await update.message.reply_text("⚔️ RPG iniciado! Sua energia: 100")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id
    e = energy.get(user, 100)
    await update.message.reply_text(f"🔋 Sua energia: {e}")

async def hunt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id
    e = energy.get(user, 100)

    if e <= 0:
        await update.message.reply_text("Sem energia! Aguarde regenerar ⏳")
        return

    energy[user] = e - 10
    await update.message.reply_text("🐺 Você caçou um monstro! -10 energia")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("hunt", hunt))

    app.run_polling()

if __name__ == "__main__":
    main()
