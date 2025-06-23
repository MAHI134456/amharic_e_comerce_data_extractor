import os, csv
from telethon import TelegramClient, events
from config.settings import API_ID, API_HASH, CHANNELS, MEDIA_DIR
from utils.logger import setup_logger

# Initialize logger and folders
logger = setup_logger("listen_realtime")
os.makedirs("data", exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

# Configure CSV file for real-time data
CSV_FILE = "data/raw_media/telegram_live.csv"
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["channel", "message_id", "sender_id", "timestamp", "text", "media_paths"])

# Initialize Telegram client
client = TelegramClient("session_realtime", API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    msg = event.message
    channel = msg.chat.username
    text = msg.text or ""
    media_paths = []

    # Download media if present
    if msg.photo or msg.document:
        try:
            path = await msg.download_media(file=os.path.join(MEDIA_DIR, channel))
            if path:
                media_paths.append(path)
                logger.info(f"📥 Media saved: {path}")
        except Exception as e:
            logger.error(f"❌ Media download failed: {e}")

    # Append the record to CSV
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
    logger.info(f"✅ New message captured: {msg.id} from @{channel}")

def main():
    logger.info("🔔 Starting real-time listener...")
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
