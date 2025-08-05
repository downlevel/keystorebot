import json
import os
from pyqueue_client import PyQueue
from config import config

class KeyStore:
    def __init__(self):
        self.queue = PyQueue(
            server_url=config.PYQUEUE_SERVER_URL,
            queue_type=config.PYQUEUE_QUEUE_TYPE,
            queue_name=config.PYQUEUE_QUEUE_NAME
        )

    def add_key_value(self, chat_id, key, value):

        # Load data from queue
        messages = self.queue.get_messages()

        # If key already exists, return
        for message in messages:
            if message["message_body"]["chat_id"] == chat_id and message["message_body"]["key"] == key:
                return 0

        # Add to queue for processing
        self.queue.add_message(message={"chat_id": chat_id, "key": key, "value": value}, item_id=None)
        return 1
    
    def get_keys(self, chat_id):
        messages = self.queue.get_messages()
        keys = []
        for message in messages:
            if message["message_body"]["chat_id"] == chat_id:
                keys.append(message["message_body"]["key"])
        return keys

    def key_exists(self, chat_id, key):
        messages = self.queue.get_messages()
        for message in messages:
            if message["message_body"]["chat_id"] == chat_id and message["message_body"]["key"] == key:
                return True
        return False

    def get_all_pairs(self, chat_id):
        messages = self.queue.get_messages()
        pairs = {}
        for message in messages:
            if message["message_body"]["chat_id"] == chat_id:
                pairs[message["message_body"]["key"]] = message["message_body"]["value"]
        return pairs

    def update_key_value(self, chat_id, key, value):
        messages = self.queue.get_messages()
        for message in messages:
            if message["message_body"]["chat_id"] == chat_id and message["message_body"]["key"] == key:
                message["message_body"]["value"] = value
                self.queue.update_message(message["Id"], message["message_body"])
                return 1
        return 0

    def get_value(self, chat_id, key):
        messages = self.queue.get_messages()
        for message in messages:
            if message["message_body"]["chat_id"] == chat_id and message["message_body"]["key"] == key:
                return message["message_body"]["value"]
        return None