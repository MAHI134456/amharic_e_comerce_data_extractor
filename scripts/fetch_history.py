import os, csv
from telethon import TelegramClient
from configparser import ConfigParser

# Replace these with your actual Telegram credentials
api_id = 29625537
api_hash = "6d1102ce84353f3bf6377acb5390358f"

client = TelegramClient('session_name', api_id, api_hash)

channels = [
    "ethio_brand_collection",
    "Leyueqa", "sinayelj", "Shewabrand",
    "helloomarketethiopia", "modernshoppingcenter", "qnashcom"
]

csv_file = "data/raw_media/telegram_messages.csv"
os.makedirs(os.path.dirname(csv_file), exist_ok=True)

# Write headers if file does not exist
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["channel", "message_id", "sender_id", "timestamp", "text"])

async def fetch_history():
    await client.start()
    for username in channels:
        try:
            async for message in client.iter_messages(username, limit=500):  # You can increase limit
                if message.text:
                    with open(csv_file, "a", newline='', encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow([
                            username,
                            message.id,
                            message.sender_id,
                            message.date.isoformat(),
                            message.text.replace('\n', ' ')
                        ])
            print(f"✅ Done fetching from @{username}")
        except Exception as e:
            print(f"❌ Failed to fetch from @{username}: {e}")

with client:
    client.loop.run_until_complete(fetch_history())
