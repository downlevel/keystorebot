# keystorebot
A simple Telegram Bot that store a key and chat ID on a json file

## Key Functionalities
✅ Users send a key via Telegram → The bot saves it in storage.json. <br/>
✅ Stores chat ID + key → Other apps can process it later. <br/>
✅ Uses pynotiq_client → Adds messages to the queue for further processing.

## Workflow

Replies to /start <br/>
Stores user-sent messages as keys <br/>
Saves the chat ID + key in storage.json <br/>
Adds it to the pynotiq_client queue for processing <br/>
