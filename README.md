# telegram_bot
The code is a Python script that uses the python-telegram-bot library to create a Telegram bot that listens for new messages in a group and triggers an event when a new member joins.

Here's a breakdown of the code:

Import necessary modules:
**code**
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
logging is used for logging messages and errors.
Update is a class that represents an update from Telegram.
Updater is a class that initializes the bot and starts the polling loop.
CommandHandler is a class that handles commands issued to the bot.
CallbackContext is a class that provides context for callback functions.


**Enable logging:**
Full Screen
Copy code
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)
This sets up logging to print messages in a human-readable format.

**Define the start function:**

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am BrockBot, a chatbot that can answer questions about Brock, the Pokemon character.')
This function is called when the user issues the /start command. It sends a message to the user introducing the bot.

**Define the new_chat_members function:
**
def new_chat_members(update: Update, context: CallbackContext) -> None:
    """Send a message when a new member joins the group."""
    for member in update.message.new_chat_members:
        if member.is_bot:
            return
        update.message.reply_text(f'Welcome to the group, {member.first_name}! I am BrockBot, a chatbot that can answer questions about Brock, the Pokemon character.')
This function is called when a new member joins the group. It checks if the new member is a bot and ignores it if it is. Otherwise, it sends a message to the new member introducing the bot.

**Define the main function:
**
def main() -> None:
    """Start the bot."""
    updater = Updater("TOKEN", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_chat_members))

    updater.start_polling()

    updater.idle()
updater = Updater("TOKEN", use_context=True) initializes the bot with your Telegram bot token.
dispatcher = updater.dispatcher creates a dispatcher object that handles incoming updates.
dispatcher.add_handler(CommandHandler("start", start)) adds a command handler for the /start command.
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_chat_members)) adds a message handler for new chat members.
updater.start_polling() starts the polling loop that listens for incoming updates.
updater.idle() keeps the bot running until it is stopped manually.
