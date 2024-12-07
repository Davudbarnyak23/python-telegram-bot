# Заняття 3

### Робота зі _стікерами_

### [&#8678; Зміст](../index.md)

---

### Повторення

В бібліотеці pyTelegramBotAPI можна мати кілька обробників message_handler з різними 
параметрами commands, і вони будуть викликати різні функції залежно від команди, яку отримують. 
Кожен обробник буде реагувати на свою команду і викликати відповідну функцію.

Приклад:

```python
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ласкаво просимо!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Як я можу допомогти?")

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "Це бот, створений для допомоги з різними завданнями.")
```

Робота з клавіатурою в pyTelegramBotAPI включає створення та додавання кнопок, 
а також обробку їх натискання. 

```python
# ...

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Ласкаво просимо! Зробіть вибір:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Кнопка 1")
def handle_button1(message):
    bot.send_message(message.chat.id, "Ви натиснули на Кнопку 1")
```

---

## Робота зі `стікерами` наліпками

Наліпки є однією з важливих функцій Telegram, вони дозволяють прикрасити повідомлення чи зробити взаємодію з ботом більш інтерактивною. 
У PyTelegramBotAPI підтримується надсилання, обробка та керування наліпками.

#### Прийом стікерів

Бот може обробляти стікери, які надсилають користувачі. 
Для цього потрібно налаштувати обробник, який реагуватиме на тип повідомлення `sticker`.

```python
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    # Отримуємо інформацію про стікер
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji
    bot.reply_to(message, f"Ви надіслали наліпку з емоджі {emoji} (ID: {sticker_id})")
```

#### Надсилання стікерів

Одним з варіантів, як можна надіслати стікер, треба знати його __file_id__.

```python
@bot.message_handler(commands=['send_custom_sticker'])
def send_custom_sticker(message):
    sticker_id = '# тут має бути ІД стікера #'
    bot.send_sticker(message.chat.id, sticker_id)
```

---

**Формати стікерів**:

- Telegram підтримує стікери у форматі `.webp` (статичні) та `.tgs` (анімаційні, створені через Lottie).
- Для надсилання власних стікерів використовуйте відповідні формати.

