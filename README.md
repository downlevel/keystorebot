# KeyStoreBot 🤖

A simple yet powerful Telegram bot that allows users to securely store, edit, list, and retrieve key-value pairs associated with their Telegram chat ID. The bot uses a queue system (via `pyqueue_client`) to persist user data in a JSON file, making it easy for other applications to process or consume the stored information.

## Features ✨

- 🚀 **Start the bot** and get instructions with `/start`
- 💾 **Store** a new key-value pair with `/store`
- ✏️ **Edit** an existing key-value pair with `/edit`
- 📋 **List** all your stored keys and values with `/list`
- 🔍 **Find** a specific key with `/find`
- 🔒 All data is associated with your Telegram chat ID for privacy
- 📊 Uses queue-based storage for easy integration with other systems

## How It Works 🔧

1. Users interact with the bot via Telegram commands
2. The bot saves key-value pairs (along with the user's chat ID) in a queue using `pyqueue_client`
3. Data is persisted in a JSON file for reliability
4. Other applications can process the queue for further actions

## Example Usage 📝

### Starting the bot
```
User: /start
Bot: Welcome! Available commands:
     /store - Store a new key-value pair
     /edit - Edit an existing key-value pair
     /list - Show all your stored keys and values
     /find - Search for a specific key
```

### Storing a new key-value pair
```
User: /store
Bot: Please enter the key you want to store:
User: api_key
Bot: Now please enter the value for key 'api_key':
User: sk-1234567890abcdef
Bot: ✅ Key-value pair stored successfully!
     Key: api_key
     Value: sk-1234567890abcdef
```

### Listing all stored data
```
User: /list
Bot: Your stored key-value pairs:

     🔑 Key: api_key
     📝 Value: sk-1234567890abcdef
     ➖➖➖➖➖➖
     
     🔑 Key: database_url
     📝 Value: postgresql://localhost:5432/mydb
     ➖➖➖➖➖➖
```

### Finding a specific key
```
User: /find
Bot: Please enter the key you want to find:
User: api_key
Bot: Found key-value pair:
     🔑 Key: api_key
     📝 Value: sk-1234567890abcdef
```

### Editing an existing key
```
User: /edit
Bot: Please enter the key you want to edit:
User: api_key
Bot: Now please enter the value for key 'api_key':
User: sk-new1234567890abcdef
Bot: ✅ Key-value pair updated successfully!
     Key: api_key
     Value: sk-new1234567890abcdef
```

## Requirements 📋

- Python 3.7+
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))

## Setup & Installation 🚀

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd keystorebot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   QUEUE_FILE_PATH=queue.json
   ```

4. **Run the bot:**
   ```bash
   python main.py
   ```

## Project Structure 📁

```
keystorebot/
├── main.py              # Entry point
├── bot.py               # Telegram bot logic and handlers
├── keystore_client.py   # KeyStore class for data management
├── config.py            # Configuration and environment variables
├── requirements.txt     # Python dependencies
├── queue.json          # Data storage file (created automatically)
├── .env                # Environment variables (create this)
└── README.md           # This file
```

## Architecture 🏗️

The bot follows a simple but effective architecture:

- **Bot Layer** (`bot.py`): Handles Telegram interactions and user states
- **Storage Layer** (`keystore_client.py`): Manages key-value operations
- **Queue System**: Uses `pyqueue_client` for reliable data persistence
- **Configuration** (`config.py`): Centralized settings management

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.