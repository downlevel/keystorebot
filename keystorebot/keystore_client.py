import json
import os
from pynotiq_client import PyNotiQ

class KeyStore:
    def __init__(self, storage_file="storage.json"):
        self.storage_file = storage_file
        self.queue = PyNotiQ()

    def add_key(self, chat_id, key):
        data = self.load_data()
        data[str(chat_id)] = key  # Store as string to ensure JSON compatibility
        self.save_data(data)

        # Add to queue for processing
        self.queue.add_message({"chat_id": chat_id, "key": key})

    def load_data(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                return json.load(f)
        return {}

    def save_data(self, data):
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

