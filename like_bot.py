from flask import Flask, request
from telegram import Bot,ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import config

app = Flask(__name__)
TOKEN = "8195691401:AAFz4-PPftn6ONSO0VbE75IbpgeYAGae9ic"
bot = Bot(token=TOKEN)
#create like bot 
@app.route('/like', methods=["POST"])
def like_bot():
    data = request.get_json()
    chat_id = data["message"]["from"]["id"]
    if data['message']['text'] == '/start':
        return "Tugmani tanlang"

    button = [["👍", "👎"],
              ["Clear"]]
    markup = ReplyKeyboardMarkup(button, one_time_keyboard=True)
    bot.send_message(chat_id=chat_id,text = "Buttondan tanlang!!!", reply_markup=markup)

    like = 0
    dislike = 0
    if '👍' in data["message"]["text"]:
        like += 1
    elif '👎' in data["message"]["text"]:
        dislike += 1
    





if __name__ == '__main__':
    app.run(debug=True)