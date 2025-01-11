import telebot

token = '7318286492:AAG0setDCJyhHVxrYcIH_yt0KEjVBjIq448'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def is_text(message):
    bot.send_message(message.chat.id, message.text + 'start')


if __name__ == '__main__':
    bot.polling()

