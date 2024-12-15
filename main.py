import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, Application, MessageHandler, filters, CallbackQueryHandler
from dotenv import load_dotenv
import os


logging.basicConfig(format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"), level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
load_dotenv()
token = os.getenv("token")
morse_code = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",
    "/": "_.._.",
    "@": ".__._.",
    " ": "",
    "": "  "
}


async def start_morse_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("Cypher", callback_data="cypher"),
        InlineKeyboardButton("Decypher", callback_data="decypher")

    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_html("cypher or decypher? \n hit <a>/cancel</a> if you wanna withdraw",
                                    reply_markup=reply_markup)


async def morse_code_state(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    context.user_data["status"] = query.data
    await query.edit_message_text("Please enter you message:")


async def decryption(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    state = context.user_data["status"]
    if state == "cypher":
        #  Cyphering the word
        user = update.effective_message.text.lower()
        final_word = []
        test_list = [i for i in user]
        try:
            for i in test_list:
                final_word.append(morse_code[i])
            await update.message.reply_text(" ".join(final_word))
        except KeyError:
            await update.message.reply_text("Please send a valid text")
    elif state == "decypher":
        # deciphering the word
        translated_word = []
        user = update.effective_message.text.lower()
        reversed_morse_dic = {value: key for key, value in morse_code.items()}
        morse_word = user.split(" ")
        try:
            for i in morse_word:
                translated_word.append(reversed_morse_dic[i])
            deciphered_word = "".join(translated_word)
            await update.message.reply_text(deciphered_word)
        except KeyError:
            await update.message.reply_text("Please check your code again")
    else:
        await update.message.reply_html("Please <a>/restart</a> to start again")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start_morse_code(update, context)


def main() -> None:
    application = Application.builder().token(token=token).build()
    application.add_handler(CommandHandler(["start", "restart"], start_morse_code))
    application.add_handler(CallbackQueryHandler(morse_code_state))
    application.add_handler(MessageHandler(filters.TEXT and ~filters.COMMAND, decryption))
    application.add_handler(CommandHandler("cancel", cancel))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
