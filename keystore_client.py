import json
import os
from pynotiq_client import PyNotiQ

class KeyStore:
    def __init__(self):
        self.queue = PyNotiQ()

    def add_key_value(self, chat_id, key, value):

        # Load data from queue
        messages = self.queue.get_messages()

        # If key already exists, return
        for message in messages:
            if message["MessageBody"]["chat_id"] == chat_id and message["MessageBody"]["key"] == key:
                return 0

        # Add to queue for processing
        self.queue.add_message(None, {"chat_id": chat_id, "key": key, "value": value})
        return 1
    
    def get_keys(self, chat_id):
        messages = self.queue.get_messages()
        keys = []
        for message in messages:
            if message["MessageBody"]["chat_id"] == chat_id:
                keys.append(message["MessageBody"]["key"])
        return keys

    def key_exists(self, chat_id, key):
        messages = self.queue.get_messages()
        for message in messages:
            if message["MessageBody"]["chat_id"] == chat_id and message["MessageBody"]["key"] == key:
                return True
        return False

    def get_all_pairs(self, chat_id):
        messages = self.queue.get_messages()
        pairs = {}
        for message in messages:
            if message["MessageBody"]["chat_id"] == chat_id:
                pairs[message["MessageBody"]["key"]] = message["MessageBody"]["value"]
        return pairs

    def update_key_value(self, chat_id, key, value):
        messages = self.queue.get_messages()
        for message in messages:
            if message["MessageBody"]["chat_id"] == chat_id and message["MessageBody"]["key"] == key:
                message["MessageBody"]["value"] = value
                self.queue.update_message(message["Id"], message["MessageBody"])
                return 1
        return 0