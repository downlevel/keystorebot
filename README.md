# keystorebot
A simple Telegram Bot that store a key and chat ID on a json file

## Key Functionalities
✅ Users send a key via Telegram → The bot saves it in a queue using pynotiq_client <br/>
✅ Stores chat ID + key → Other apps can process it later.

## Workflow

✅ Replies to /start <br/>
✅ Stores user-sent messages as keys <br/>
✅ Adds it to the pynotiq_client queue for processing