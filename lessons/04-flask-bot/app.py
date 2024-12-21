import telebot
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import threading

token = '7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM'
bot = telebot.TeleBot(token)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bot.sqlite"
app.config['SECRET_KEY'] = '00011110000111'
db = SQLAlchemy(app)


# --- MODELS ----------------------------------------------------
class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=True)


# with app.app_context():
#     db.create_all()


# --- ROUTE ----------------------------------------------------
@app.route('/')
def index():
    mes = Base.query.all()
    return render_template('index.html', mes=mes)


# ------ MESSAGE ---------------------------------------------------
@bot.message_handler(content_types=['text'])
def is_text(message):
    with app.app_context():
        b = Base(text=message.text)
        db.session.add(b)
        db.session.commit()

    bot.send_message(message.chat.id, 'OK!')


def run_bot():
    print('run bot::')
    bot.polling()


def run_flask():
    print('run flask::')
    app.run()


if __name__ == '__main__':
    f_thread = threading.Thread(target=run_flask)
    b_thread = threading.Thread(target=run_bot)

    f_thread.start()
    b_thread.start()

    f_thread.join()
    b_thread.join()