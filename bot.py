import asyncio
import time
from telethon import TelegramClient, events

api_id = 33412623
api_hash = '9376d25b1911642531cd3210c8b44b27'

WELCOME_MESSAGE = """أهلا بـك صديـقي ⚡️ 🫱

رجاء اكتب مشكلتك او طلبك بختصار حتى اتمكن من الرد عليك بسرعة 🥷

قد اتاخر عليك بالرد بسبب ضغط الرسائل الكبير ⏰🚫"""

client = TelegramClient('my_session', api_id, api_hash)

# متغير عشان نحفظ وقت آخر رد لكل شخص
last_reply_times = {}

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # نتأكد إن الرسالة في الخاص ومش من البوت نفسه
    if event.is_private and not event.out:
        user_id = event.sender_id
        current_time = time.time()
        
        # نشوف لو الشخص ده استلم رد قبل كده
        if user_id in last_reply_times:
            # لو عدت 4 دقايق (240 ثانية)، نرد تاني
            if current_time - last_reply_times[user_id] < 240:
                return # لو لسه مكملش 4 دقايق، ميردش
        
        # نسجل وقت الرد الحالي
        last_reply_times[user_id] = current_time
        
        # نبعت الرد
        await event.reply(WELCOME_MESSAGE)

async def main():
    await client.start()
    print("Userbot is running!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
