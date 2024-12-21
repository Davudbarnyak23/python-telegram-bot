import telebot
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import threading
token = '7318286492:AAG0setDCJyhHVxrYcIH_yt0KEjVBjIq448'
bot = telebot.TeleBot(token)
filename = "bot_message.txt"
file_text = 'bot_text.txt'
file_number = 'bot_number.txt'

def f1(v):
    try:
        int(v)
        return True
    except ValueError:
        return False


@bot.message_handler(content_types=['text'])
def is_text(message):
    if not f1(message.text):
        filename = 'bot_text.txt'
    else:
        filename = 'bot_number.txt'

    with open(filename, 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'save file')


if __name__ == '__main__':
    bot.polling()
