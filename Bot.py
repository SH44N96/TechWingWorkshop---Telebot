
# Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import HoroscopeSign
import WebScrapper

# Variables
token = '1079456424:AAHVV8BSa30x4gN0FOK7V2PJR6qSZ9osa98'
msg = 'These are the 2 commands available: \n - /setDate ddmm: To Save your Horoscope Sign \n - /horoscope: To Get your Daily Horoscope'
updater = Updater(token = token, use_context = True)
dispatcher = updater.dispatcher

# Functions
def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'Welcome to our Horoscope Bot! \n\n' + msg)

def error(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'Please enter a valid command. \n\n' +msg)

def set_date(update, context):
    ddmm = update.message.text[9:]
    date = int(ddmm[:2])
    month = int(ddmm[2:])

    global sign
    sign = HoroscopeSign.get_sign(date, month)
    context.bot.send_message(chat_id = update.effective_chat.id, text= 'Your sign is ' + sign.upper())

def get_daily(update, context):
    description = WebScrapper.get_description(sign)
    context.bot.send_message(chat_id = update.effective_chat.id, text = description)

# Main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

error_handler = MessageHandler(Filters.text, error)
dispatcher.add_handler(error_handler)

date_handler = CommandHandler('setDate', set_date)
dispatcher.add_handler(date_handler)

horoscope_handler = CommandHandler('horoscope', get_daily)
dispatcher.add_handler(horoscope_handler)

updater.start_polling()
print('Your bot is now online!')
