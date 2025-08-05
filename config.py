import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    QUEUE_FILE_PATH = os.getenv("QUEUE_FILE_PATH", "queue.json")

    # PyQueue Configuration
    PYQUEUE_SERVER_URL = os.getenv("PYQUEUE_SERVER_URL")
    PYQUEUE_QUEUE_TYPE = os.getenv("PYQUEUE_QUEUE_TYPE", "local")
    PYQUEUE_QUEUE_NAME = os.getenv("PYQUEUE_QUEUE_NAME")

config = Config()