import asyncio
import time
from telethon import TelegramClient, events
from flask import Flask
import threading
import os

api_id = 33412623
api_hash = '9376d25b1911642531cd3210c8b44b27'

WELCOME_MESSAGE = """أهلا بـك صديـقي ⚡️ 🫱

رجاء اكتب مشكلتك او طلبك بختصار حتى اتمكن من الرد عليك بسرعة 🥷

قد اتاخر عليك بالرد بسبب ضغط الرسائل الكبير ⏰🚫"""

client = TelegramClient('my_session', api_id, api_hash)
last_reply_times = {}

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and not event.out:
        sender = await event.get_sender()
        # لو الحساب اللي باعت بوت، متعملش حاجة واخرج
        if sender and sender.bot:
            return
            
        user_id = event.sender_id
        current_time = time.time()
        if user_id in last_reply_times:
            if current_time - last_reply_times[user_id] < 240:
                return
        last_reply_times[user_id] = current_time
        await event.reply(WELCOME_MESSAGE)

async def main():
    await client.start()
    print("Userbot is running!")
    await client.run_until_disconnected()

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(main())
