from flask import Flask, request
from telegram import Bot
import config

app = Flask(__name__)
TOKEN = "6404865942:AAGB1ZoHP8q2AET6zT5E6ex1yAYMU3GeoXs"
bot = Bot(token=TOKEN)

@app.route('/', methods=["POST"])
def main():
    data = request.get_json()
    chat_id = data['message']['from']['id']
    text = data['message']['text']
    first_name = data['message']['from']['first_name']
    if text == '/start':
        bot.send_message(chat_id=chat_id, text= f"Hello {first_name}")
    else:
        bot.send_message(chat_id=chat_id, text= text)
    print(data)


    return data

if __name__ == '__main__':
    app.run(debug=True)