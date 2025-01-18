import config
import telebot
import time
import threading
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

# === SQLITE =====
db = sqlite3.connect('notebook.db')
cur = db.cursor()

# cur.execute('''CREATE TABLE user (
#     id INTEGER PRIMARY KEY,
#     chat_id INTEGER NOT NULL ,
#     name TEXT DEFAULT 'Unknown',
#     email TEXT DEFAULT '',
#     role INTEGER DEFAULT 0,
#     deleted INTEGER DEFAULT 0
#     )''')
# db.commit()



# === FUNCTIONS =====
USER_ID = '1461689080'


def send_text_message():
     while True:
         bot.send_message(USER_ID, 'text')
         time.sleep(20)


# === MESSAGE-HANDLERS =====
@bot.message_handler(commands=['start'])
def bot_stars(message):

    # TODO: KONTENT.....
    cur.execute('SELECT chat_id FROM user')
    row = cur.fetchone()
    if not row:
        cur.execute(f"INSERT INTO user(chat_id, name) VALUES ({message.chat_id}, {message.name})")
        db.commit()

    #db.commit()

    #cur.execute(f"INSERT INTO user(chat_id, name) VALUES ({message.chat_id}, {message.name})")
    #db.commit()
    bot.send_message(message.chat.id, f'користувач [{message.chat_id}] , save')


@bot.message_handler(content_types=['text'])
def text_message(message):
    bot.send_message(message.chat.id, 'Ok')


if __name__ == '__main__':
    thread = threading.Thread(target=send_text_message)
    thread.start()
    bot.infinity_polling()

