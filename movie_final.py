import telegram.ext
import requests
import json

from telegram.ext import Filters,commandhandler

from telegram.ext import MessageHandler

from bson import json_util


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



def CleanData(data):
    ordered_data = {
    'Title': data['Title'],
    'Year': data['Year'],
    'Director': data['Director'],
    'Actors': data['Actors'],
    'Plot': data['Plot']
    }
    message = ""
    for key, value in ordered_data.items():
        message += f'{key}: {value}\n'
    return message





def search_movie(title):
    try:
        url = f"http://www.omdbapi.com/?i=tt3896198&apikey=a52d3312&t={title}"
        response = requests.get(url)
        movie_data = response.json()
        formatted_data = CleanData(movie_data)
        return formatted_data+"\u2764\ufe0f"+"\u2764\ufe0f"+"\u2764\ufe0f"
    except:
        
        return "PLEASE ENTER A VALID MOVIE TITLTE\U0001F643"


def Avatar(update,context):
    chatid = update.effective_chat.id
    bot = telegram.Bot("6169546617:AAE-4qKGjnYXNejerwAy8avAtfNGWTgiV-0")

    msg = update.message.text
    msg = msg[1:]

    result  = search_movie(msg)


    bot.send_message(chat_id=chatid, text=result)
   
    

dispatcher.add_handler(telegram.ext.CommandHandler("start",start))
dispatcher.add_handler(telegram.ext.CommandHandler("help",help))
#dispatcher.add_handler(telegram.ext.CommandHandler(,Avatar))
dispatcher.add_handler(MessageHandler(Filters.command, Avatar))

updater.start_polling()
updater.idle()
