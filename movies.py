import telegram.ext
import pymongo
from telegram.ext import Filters

from telegram.ext import MessageHandler

from bson import json_util
client = pymongo.MongoClient("mongodb+srv://telemongo666:2jdkNeP5bpQmFseP@mydb.wfmwrmy.mongodb.net/Profile?retryWrites=true&w=majority")

db = client.Profile
collection = db.images

updater = telegram.ext.Updater("<API_TOKEN_HERE>",use_context=True)
dispatcher = updater.dispatcher



def start(update,context):
    update.message.reply_text("Hello! welcome to Movies BOT")


def help(update,context):
    update.message.reply_text(
        """
        /start -> Welcome to the Bot
/help -> want more help ?
/content -> Shows All the available profiles
/<profile_id> -> displays the details ofthe profile

        """
        )
def Movie(update,context):
    chatid = update.effective_chat.id
    bot = telegram.Bot("<API_TOKEN_HERE>")
    img = db["images"]
    filter = { "Name": update.message.text[1:].title()}

    document = img.find_one(filter)
    formated = ""
    formated += f"Movie Name : {document['Name']}\n"
    formated += f"Movie Trailer : {document['Link']}\n"
    
    bot.send_message(chat_id=chatid, text=formated)
   
    
    
dispatcher.add_handler(telegram.ext.CommandHandler("start",start))
dispatcher.add_handler(telegram.ext.CommandHandler("help",help))
dispatcher.add_handler(MessageHandler(Filters.command, Movie))

updater.start_polling()
updater.idle()
