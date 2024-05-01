import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am BrockBot, a chatbot that can answer questions about Brock, the Pokemon character.')

def new_chat_members(update: Update, context: CallbackContext) -> None:
    """Send a message when a new member joins the group."""
    for member in update.message.new_chat_members:
        if member.is_bot:
            return
        update.message.reply_text(f'Welcome to the group, {member.first_name}! I am BrockBot, a chatbot that can answer questions about Brock, the Pokemon character.')

def main() -> None:
    """Start the bot."""
    updater = Updater("TOKEN", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_chat_members))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
