import logging
from telegram import Update
from telegram.ext import ApplicationBuilder,  CommandHandler, ContextTypes
from utils import get_random_joke, get_random_meme


logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your friendly bot. I like share jokes and memes with my friends and you can be one of them!\n"
    'Use the following commands:\n'
    '/joke - Get a random joke\n'
    '/meme - Get a random meme')

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    joke_text = get_random_joke()
    await update.message.reply_text(joke_text)

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    meme_url = get_random_meme()
    if meme_url:
        await update.message.reply_photo(photo=meme_url, caption="Here's a meme for you!")
    else:
        await update.message.reply_text("Sorry, I couldn't find a meme for you. Try again!")


def main() -> None:
    BOT_TOKEN = "8017288006:AAFqSfhpwO8HJ5BM1yAEEHOIwXCue2UTMwQ"

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CommandHandler("meme", meme))

    application.run_polling()

if __name__ == '__main__':
    main()