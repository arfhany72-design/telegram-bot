import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN =BOT_TOKEN = "8898982004:AAEgIPs4M_jaEUSZy1rmAqio7KCxvGJUmZA"

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.text:
        return
    reply_text = f"🤖 البوت استلم: {update.message.text}"
    await update.message.reply_text(reply_text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), reply_message)
    application.add_handler(message_handler)
    print("🔥 البوت شغال!")
    application.run_polling()
