from gc import callbacks

import config as c
from SQliteManager import SQLNote
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import threading
import sqlite3
import re
from datetime import datetime as dt

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


def bot_add_note(message):
    bot.send_message(message.chat.id, 'input note: ')
    bot.register_next_step_handler(message, bot_add_title)


def bot_add_title(message):
    with get_bd_cursor() as cur:
        cur.execute(f'SELECT id FROM users WHERE chat_id={int(message.chat.id)}')
        row = cur.fetchone()

        if row:
            cur.execute('INSERT INTO notes (user_id, title) VALUES (?, ?)', (row[0], message.text))
            bot.send_message(message.chat.id, 'note save')
        else:
            bot.send_message(message.chat.id, ':(')


def all_notes(message):
    with get_bd_cursor() as cur:
        cur.execute(f'SELECT id FROM users WHERE chat_id={int(message.chat.id)}')
        row = cur.fetchone()

        if row:
            cur.execute(f'SELECT id, title, notification FROM notes WHERE deleted=0 AND user_id={row[0]}')
            rows = cur.fetchall()

            notes = ''
            for r in rows:
                notes += f'/edit_{r[0]}: {r[1]}. [{r[2]}]\n'

            if  notes:
                bot.send_message(message.chat.id, 'notes:\n' + notes)
            else:
                bot.send_message(message.chat.id, 'no :(')
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

def edit_note(message, note_id):

    keyboard = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('regit note', callback_data="title_" + note_id)
    b2 = InlineKeyboardButton('опис', callback_data="content_" + note_id)
    b3 = InlineKeyboardButton('reg time', callback_data="notification_" + note_id)
    b4 = InlineKeyboardButton('delete', callback_data="delete_" + note_id)
    keyboard.add(b1, b2, b3)
    keyboard.add(b4)

    bot.send_message(message.chat.id, '?', reply_markup=keyboard)

def delete_note(call, note_id):
    with get_bd_cursor() as cur:
        cur.execute(f'UPDATE notes SET deleted=1 WHERE id={int(note_id)}')

        if cur.rowcount > 0:
            bot.send_message(call.message.chat.id, 'delete note')
        else:
            bot.send_message(call.message.chat.id, 'error')

def get_bd_cursor():
    return SQLNote(c.DB_NAME)

def send_text_message():
    while True:
        notes_id_list = []
        with get_bd_cursor() as cur:
            cur.execute('''
                SELECT users.chat_id, notes.title, notes.content, notes.notification, notes.id
                FROM notes 
                INNER JOIN users ON notes.user_id = users.id
                WHERE notes.is_send = 0 AND notes.deleted = 0 AND notes.notification < datetime('now')
            ''')
            rows = cur.fetchall()
            print(rows)

            for r in rows:
                notes_id_list.append(r[4])
                message = 'нагадування!\n' + r[3] + '\n' + r[1] + '\n' + r[2]
                bot.send_message(r[0], message)
                time.sleep(1)

            id_str = ', '.join(['?'] * len(notes_id_list))
            cur.execute(f'UPDATE notes SET is_send = 1 WHERE id IN ({id_str})', notes_id_list)

        time.sleep(60)


# =============================================================================================


@bot.message_handler(commands=['start', 'add', 'help', 'end', 'all'])# === MESSAGE-HANDLERS =====
def bot_commands(message):
    if '/start' == message.text:
        bot_stars(message)
    elif '/add' == message.text:
        bot_add_note(message)
    elif '/all' == message.text:
        all_notes(message)

@bot.callback_query_handler(func=lambda call: True)
def handler_note_acrion(call):
    callback_data = call.data.split('_')
    if 2 == len(callback_data):
        if callback_data[0] == 'delete':
            delete_note(call, callback_data[1])
        elif callback_data[0] == 'title':
            title_note(call, callback_data[1])
        elif callback_data[0] == 'content':
            content_note(call, callback_data[1])
        elif callback_data[0] == 'notification':
            notification_note(call, callback_data[1])

def title_note(call, note_id):
    if hasattr(call.message, 'message_id'):
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.send_message(call.message.chat.id, 'r note')
    bot.register_next_step_handler_by_chat_id(call.message.chat.id, save_title_note, note_id)

def save_title_note(message, note_id):
    with get_bd_cursor() as cur:
        cur.execute(f'UPDATE notes SET title= ? WHERE id=?', (message.text, note_id))

        if cur.rowcount > 0:
            bot.send_message(message.chat.id, 'new note')
        else:
            bot.send_message(message.chat.id, 'error')

def content_note(call, note_id):
    pass


def notification_note(call, note_id):
    if hasattr(call.message, 'message_id'):
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    m = """new time:
    *день.місяць.рік години:хвилини*
    """
    # bot.send_message(call.message.chat.id, m, parse_mode='Markdoun' )
    bot.send_message(call.message.chat.id, m)
    bot.register_next_step_handler_by_chat_id(call.message.chat.id, save_notification_note, note_id)

def save_notification_note(message, note_id):

    try:
        original_date = dt.strptime(message.text, '%d.%m.%Y %H:%M')
        notification = original_date.strftime("%Y-%m-%d %H:%M:00")

        with get_bd_cursor() as cur:
            cur.execute(f'UPDATE notes SET is_send = 0, notification=? WHERE id=?', (notification, note_id))

            if cur.rowcount > 0:
                bot.send_message(message.chat.id, 'edit time note')
            else:
                bot.send_message(message.chat.id, 'error')
    except Exception:
        bot.send_message(message.chat.id, 'error :<')

@bot.message_handler(regexp=r'^\/edit_\d+$')
def handler_edit_id(message):
    match = re.match(r'^\/edit_(\d+)$', message.text)

    if match:
        edit_note(message,match.group(1))
        #bot.send_message(message.chat.id, match.group(1))


@bot.message_handler(content_types=['text'])
def text_message(message):
    bot.send_message(message.chat.id, 'Ok')

#
if __name__ == '__main__':
    thread = threading.Thread(target=send_text_message)
    thread.start()
    bot.infinity_polling()

