import telebot
from config import config
from keystore_client import KeyStore
from typing import Dict

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)
store = KeyStore()

# Store user states
user_states: Dict[int, Dict] = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Available commands:\n"
                         "/store - Store a new key-value pair\n"
                         "/edit - Edit an existing key-value pair\n"
                         "/list - Show all your stored keys and values\n"
                         "/find - Search for a specific key")

@bot.message_handler(commands=['store'])
def initiate_store(message):
    chat_id = message.chat.id
    user_states[chat_id] = {'action': 'store', 'step': 'waiting_key'}
    bot.reply_to(message, "Please enter the key you want to store:")

@bot.message_handler(commands=['edit'])
def initiate_edit(message):
    chat_id = message.chat.id
    user_states[chat_id] = {'action': 'edit', 'step': 'waiting_key'}
    bot.reply_to(message, "Please enter the key you want to edit:")

@bot.message_handler(commands=['list'])
def list_keys(message):
    chat_id = message.chat.id
    pairs = store.get_all_pairs(chat_id)
    
    if not pairs:
        bot.reply_to(message, "You don't have any stored key-value pairs yet.")
        return
    
    # Format the key-value pairs
    response = "Your stored key-value pairs:\n\n"
    for key, value in pairs.items():
        response += f"🔑 Key: {key}\n📝 Value: {value}\n➖➖➖➖➖➖\n"
    
    bot.reply_to(message, response)

@bot.message_handler(commands=['find'])
def initiate_find(message):
    chat_id = message.chat.id
    user_states[chat_id] = {'action': 'find', 'step': 'waiting_key'}
    bot.reply_to(message, "Please enter the key you want to find:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    
    # If user hasn't started a store/edit/find action
    if chat_id not in user_states:
        bot.reply_to(message, "Please use:\n"
                            "/store - Store a new key-value pair\n"
                            "/edit - Edit an existing key-value pair\n"
                            "/list - Show all your stored keys and values\n"
                            "/find - Search for a specific key")
        return

    state = user_states[chat_id]
    
    if state['step'] == 'waiting_key':
        key = message.text.strip()
        
        if state['action'] == 'find':
            # Handle find action
            value = store.get_value(chat_id, key)
            if value is not None:
                bot.reply_to(message, f"Found key-value pair:\n🔑 Key: {key}\n📝 Value: {value}")
            else:
                bot.reply_to(message, f"❌ Key '{key}' not found!")
            del user_states[chat_id]
            return
        
        if state['action'] == 'store':
            # Check if key exists for store action
            if store.key_exists(chat_id, key):
                bot.reply_to(message, f"❌ Key '{key}' already exists! Use /edit to modify it.")
                del user_states[chat_id]
                return
        else:  # edit action
            # Check if key doesn't exist for edit action
            if not store.key_exists(chat_id, key):
                bot.reply_to(message, f"❌ Key '{key}' doesn't exist! Use /store to create it.")
                del user_states[chat_id]
                return
        
        # Store the key and wait for value
        state['key'] = key
        state['step'] = 'waiting_value'
        bot.reply_to(message, f"Now please enter the value for key '{key}':")
        
    elif state['step'] == 'waiting_value':
        value = message.text.strip()
        key = state['key']
        
        if state['action'] == 'store':
            store.add_key_value(chat_id, key, value)
            bot.reply_to(message, f"✅ Key-value pair stored successfully!\nKey: {key}\nValue: {value}")
        else:  # edit action
            store.update_key_value(chat_id, key, value)
            bot.reply_to(message, f"✅ Key-value pair updated successfully!\nKey: {key}\nValue: {value}")
        
        # Clear user state
        del user_states[chat_id]

if __name__ == "__main__":
    bot.polling()