import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
QUEUE_FILE_PATH = os.getenv("QUEUE_FILE_PATH", "queue.json")