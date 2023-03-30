import telegram.ext
import pymongo
from telegram.ext import Filters

from telegram.ext import MessageHandler

from bson import json_util
client = pymongo.MongoClient("mongodb+srv://telemongo666:2jdkNeP5bpQmFseP@mydb.wfmwrmy.mongodb.net/Profile?retryWrites=true&w=majority")

db = client.Profile
collection = db.images

#Token = "6169546617:AAE-4qKGjnYXNejerwAy8avAtfNGWTgiV-0"
updater = telegram.ext.Updater("6169546617:AAE-4qKGjnYXNejerwAy8avAtfNGWTgiV-0",use_context=True)
dispatcher = updater.dispatcher



def start(update,context):
    update.message.reply_text("Hello! welcome ")


def help(update,context):
    update.message.reply_text(
        """
        /start -> Welcome to the Bot
/help -> want more help ?
/content -> Shows All the available profiles
/<profile_id> -> displays the details ofthe profile

        """
        )






def Avatar(update,context):
    chatid = update.effective_chat.id
    bot = telegram.Bot("6169546617:AAE-4qKGjnYXNejerwAy8avAtfNGWTgiV-0")
    img = db["images"]
    filter = { "Name": "Avatar" }

    document = img.find_one(filter)
    formated = ""
    formated += f"Movie Name : {document['Name']}\n"
    formated += f"Movie Trailer : {document['Link']}\n"
    
    bot.send_message(chat_id=chatid, text=formated)
   
    
    
dispatcher.add_handler(telegram.ext.CommandHandler("start",start))
dispatcher.add_handler(telegram.ext.CommandHandler("help",help))
dispatcher.add_handler(telegram.ext.CommandHandler("Avatar",Avatar))

updater.start_polling()
updater.idle()
