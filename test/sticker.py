import telebot
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

token = '7318286492:AAG0setDCJyhHVxrYcIH_yt0KEjVBjIq448'
bot = telebot.TeleBot(token)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite'
app.config['SECRET_KEY'] = 'sdhjp677'
db = SQLAlchemy(app)

class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(),nullable=False)

with app.app_context():
    db.create_all


@app.route('/')
def index():
    mes = Base.query.all()
    return render_template('index.html', mes=mes)

@bot.message_handler(content_types=['sticker'])
def handler_sticker(message):
    id = message.sticker.file_id
    em = message.sticker.emoji
    text = f'id_sticker = ({id}). emoji = ({em})'
    bot.reply_to(message, text)


@bot.message_handler(commands=['f'])
def handler_f(message):
    current_path_app = os.path.abspath(__file__)
    current_path = os.path.dirname(current_path_app)
    my_file = os.path.join(current_path, 'sticker', 'dog.webm')

    with open(my_file, 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)



sticker_list = ['CAACAgIAAxkBAAICIGdUJu8Ip5uhPj2HWXXwaP9Oj93sAAJqGAACdU0hSePFqEQNyXxvNgQ',
                'CAACAgIAAxkBAAICPmdUKdC6cRhgzgPu-FO5nqm5LUNRAAI-KgACDSrZSPVwvES1L1ybNgQ',
                'CAACAgIAAxkBAAICIGdUJu8Ip5uhPj2HWXXwaP9Oj93sAAJqGAACdU0hSePFqEQNyXxvNgQ',]

@bot.message_handler(content_types=['text'])
def is_text(message):

    if message.text == 'g':
        bot.send_sticker(message.chat.id, sticker_list[0])
        return True
    elif message.text == 'j':
        bot.send_sticker(message.chat.id, sticker_list[1])
        return True

    bot.send_message(message.chat.id, 'sticker')


if __name__ == '__main__':
    #bot.infinity_polling()
    app.run()