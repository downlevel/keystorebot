import json
import os
from pynotiq_client import PyNotiQ

class KeyStore:
    def __init__(self):
        self.queue = PyNotiQ()

    def add_key(self, chat_id, key):

        # Load data from queue
        messages = self.queue.get_messages()

        # If key already exists, return
        for message in messages:
            if message["chat_id"] == chat_id and message["key"] == key:
                return 0

        # Add to queue for processing
        self.queue.add_message({"chat_id": chat_id, "key": key})
        return 1