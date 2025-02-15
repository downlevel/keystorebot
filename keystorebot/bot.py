import telebot
from config import TELEGRAM_BOT_TOKEN
from keystore_client import KeyStore

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
store = KeyStore()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a key and I'll store it for you.")

@bot.message_handler(func=lambda message: True)
def store_key(message):
    key = message.text.strip()
    chat_id = message.chat.id
    store.add_key(chat_id, key)
    bot.reply_to(message, f"✅ Key '{key}' stored successfully!")

if __name__ == "__main__":
    bot.polling()
