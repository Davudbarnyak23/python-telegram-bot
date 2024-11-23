import telebot

token = '7318286492:AAG0setDCJyhHVxrYcIH_yt0KEjVBjIq448'
bot = telebot.TeleBot(token)

#codes program
@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - text message'
    bot.send_message(message.chat.id, msg)


if __name__ == '__main__':
    bot.polling()