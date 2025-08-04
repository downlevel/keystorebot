import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    QUEUE_FILE_PATH = os.getenv("QUEUE_FILE_PATH", "queue.json")

    # PyNotiQ Configuration
    PYNOTIQ_SERVER_URL = os.getenv("PYNOTIQ_SERVER_URL")
    PYNOTIQ_QUEUE_TYPE = os.getenv("PYNOTIQ_QUEUE_TYPE", "local")
    PYNOTIQ_QUEUE_NAME = os.getenv("PYNOTIQ_QUEUE_NAME")
    
config = Config()