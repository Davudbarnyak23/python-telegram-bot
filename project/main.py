import config as c
from SQliteManager import SQLNote
import telebot
import time
import threading
import sqlite3

bot = telebot.TeleBot(c.BOT_TOKEN)


def bot_stars(message):
    print(message)
    with get_bd_cursor() as cur:
        cur.execute("SELECT chat_id FROM users WHERE chat_id='%d'" % message.chat.id)
        row = cur.fetchone()

        if not row:
            cur.execute(
                f"INSERT INTO users (chat_id, name) VALUES ('{message.chat.id}', '{message.from_user.username}')")
            bot.send_message(message.chat.id, f'користувач [{message.chat.id}] , save')
        else:
            bot.send_message(message.chat.id, '++++')

def bot_add_title(message):
    pass

# === SQLITE =====
# db = sqlite3.connect('notebook.db')
# cur = db.cursor()
#
# cur.execute('''CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     chat_id INTEGER NOT NULL ,
#     name TEXT DEFAULT 'Unknown',
#     deleted INTEGER DEFAULT 0
#     )''')
# db.commit()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS notes (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER NOT NULL ,
#     title TEXT NOT NULL,
#     content TEXT DEFAULT '',
#     notification DATETIME DEFAULT CURRENT_TIMESTAMP,
#     is_send INTEGER DEFAULT 0,
#     deleted INTEGER DEFAULT 0
#     )''')
# db.commit()

# === FUNCTIONS =====

def get_bd_cursor():
    return SQLNote(c.DB_NAME)

def send_text_message():
     while True:
         bot.send_message(USER_ID, 'text')
         time.sleep(20)

# start - new
# add - add
# edit - refactor
# delete - delete
# all - notes
# help - help
# end - all new

@bot.message_handler(commands=['start', 'add', 'edit', 'delete', 'help', 'end'])# === MESSAGE-HANDLERS =====
def bot_commands(message):
    if '/start' == message.text:
        bot_stars('ok')
    elif '/add' == message.text:
        bot.send_message(message.chat.id, 'note:')
        bot.register_next_step_handler(message, bot_add_title)

@bot.message_handler(commands=['start'])
def bot_stars(message):
    print(message)
    with get_bd_cursor() as cur:
        cur.execute("SELECT chat_id FROM users WHERE chat_id='%d'" % message.chat.id)
        row = cur.fetchone()

        if not row:
            cur.execute(f"INSERT INTO users (chat_id, name) VALUES ('{message.chat.id}', '{message.from_user.username}')")
            bot.send_message(message.chat.id, f'користувач [{message.chat.id}] , save')
        else:
            bot.send_message(message.chat.id, '++++')


@bot.message_handler(content_types=['text'])
def text_message(message):
    bot.send_message(message.chat.id, 'Ok')

#
if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    bot.infinity_polling()

