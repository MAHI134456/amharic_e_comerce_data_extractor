import os, csv
from telethon import TelegramClient
from config.settings import API_ID, API_HASH, CHANNELS, HISTORY_LIMIT, MEDIA_DIR
from utils.logger import setup_logger

logger = setup_logger("fetch_history_csv")
os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)

client = TelegramClient("session_history", API_ID, API_HASH)

CSV_FILE = "data/telegram_messages.csv"

# Initialize CSV file with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["channel", "message_id", "sender_id", "timestamp", "text", "media_paths"])

async def fetch():
    await client.start()
    for channel in CHANNELS:
        logger.info(f"Fetching from @{channel}")
        async for msg in client.iter_messages(channel, limit=HISTORY_LIMIT):
            text = msg.text or ""
            media_paths = []

            if msg.photo or msg.document:
                try:
                    media_path = await msg.download_media(file=os.path.join(MEDIA_DIR, channel))
                    media_paths.append(media_path)
                    logger.info(f"Downloaded media to {media_path}")
                except Exception as e:
                    logger.warning(f"Failed to download media: {e}")

            with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    channel,
                    msg.id,
                    msg.sender_id,
                    msg.date.isoformat(),
                    text.replace("\n", " ").strip(),
                    ";".join(media_paths)
                ])
        logger.info(f"✅ Done with @{channel}")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(fetch())
