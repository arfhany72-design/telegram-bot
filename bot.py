import asyncio
from telethon import TelegramClient, events

api_id = 33412623
api_hash = '9376d25b1911642531cd3210c8b44b27'

WELCOME_MESSAGE = """أهلا بـك صديـقي ⚡️ 🫱

رجاء اكتب مشكلتك او طلبك بختصار حتى اتمكن من الرد عليك بسرعة 🥷

قد اتاخر عليك بالرد بسبب ضغط الرسائل الكبير ⏰🚫"""

client = TelegramClient('my_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and not event.out:
        await event.reply(WELCOME_MESSAGE)

async def main():
    await client.start()
    print("Userbot is running!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
