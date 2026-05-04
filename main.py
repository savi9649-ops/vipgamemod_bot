from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "PUT_YOUR_TOKEN_HERE"8545448390:AAHQvaaAIKUFjqeguLhfPnpNdeyeGpoV3PA

accounts = ["acc1:pass1", "acc2:pass2"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Welcome to VIP Game Bot!")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(accounts) == 0:
        await update.message.reply_text("❌ Out of stock")
        return

    acc = accounts.pop(0)
    await update.message.reply_text(f"🎁 Account: {acc}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))

app.run_polling()
