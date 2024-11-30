from pyexpat.errors import messages

import telebot
from telebot import types
token = '7318286492:AAG0setDCJyhHVxrYcIH_yt0KEjVBjIq448'
bot = telebot.TeleBot(token)

#codes program
@bot.message_handler(commands=['open'])
def handler_open(message):
    bot.send_message(message.chat.id, 'open')


@bot.message_handler(commands=['close'])
def handler_close(message):
    bot.send_message(message.chat.id, 'close')


@bot.message_handler(commands=['start', 'stop', 'speed'])
def handler_run_car(message):
    car = 'Stop'

    if message.text == '/start':
        car = 'start'
    elif message.text == '/stop':
        car = 'stop'
    elif message.text == '/speed':
        car = 'stap'

    bot.send_message(message.chat.id, car)


@bot.message_handler(commands=['p'])
def handler_pizza(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='paperoni')
    btn2 = types.KeyboardButton(text='classic')
    keyboard.add(btn1, btn2)

    bot.send_message(message.chat.id, 'вибиріть піцу', reply_markup=keyboard)
    bot.register_next_step_handler(message, pizza_order)


@bot.message_handler(commands=['d'])
def handler_drinks(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='pepsi')
    btn2 = types.KeyboardButton(text='fanta')
    btn3 = types.KeyboardButton(text='cola')
    keyboard.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, 'вибиріть напій', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'pepsi')
def drinks_pepsi(message):
    bot.send_message(message.chat.id, '+ ' + message.text)

@bot.message_handler(func=lambda message: message.text == 'fanta')
def drinks_fanta(message):
    bot.send_message(message.chat.id, '+ ' + message.text)

@bot.message_handler(func=lambda message: message.text == 'cola')
def drinks_cola(message):
    bot.send_message(message.chat.id, '+ ' + message.text)


@bot.message_handler(commands=['ik'])
def inline_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('k1', callback_data='b1')
    b2 = types.InlineKeyboardButton('k2', callback_data='b2')
    keyboard.add (b1, b2)

    bot.send_message(message.chat.id, ' 1 or 2', reply_markup=keyboard)


@bot.callback_query_handler()
def f_b1(cl):
    if cl.data == 'b1':
        bot.send_message(cl.message.chat.id, 'text 1')
    elif cl.data == 'b2':
        bot.send_message(cl.message.chat.id, 'text 2')


@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - text message'
    bot.send_message(message.chat.id, msg)


def pizza_order(message):
    if message.text == 'paperoni':
        pass
    elif message.text == 'classic':
        pass

    bot.send_message(message.chat.id, f'ваше замовлення піци ({message.text}) прийнято! ')


if __name__ == '__main__':
    bot.infinity_polling()
