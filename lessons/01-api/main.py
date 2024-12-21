import telebot


token = '7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def say_number(message):
    if '1' == message.text:
        request = 'Один'
    elif '2' == message.text :
        request = 'Два'
    elif message.text == '3':
        request = 'Три'
    elif message.text == '4':
        request = 'Чотири'
    elif message.text == '5':
        request = 'Пять'
    else:
        request = 'Відповідь не знайдена'

    bot.send_message(message.chat.id, request)


# Перевіряємо чи файл запускається безпосередньо, а не імпортується як модуль в інший скрипт
if __name__ == '__main__':
    bot.polling()
