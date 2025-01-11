# Заняття 9

### Робота з базою даних SQLite3

### [&#8678; Зміст](../index.md)

---

[SQLite3](https://docs.python.org/3.10/library/sqlite3.html) — це вбудована реляційна база даних, яка зберігає дані у файл, 
що робить її ідеальною для невеликих додатків та прототипів.

Модуль `sqlite3` входить до стандартної бібліотеки Python, 
тому немає потреби встановлювати додаткові пакети.

Для роботи з базою даних може знадобитися редактор, можна скористатися DBeaver.    
__[DBeaver Community](https://dbeaver.io/download/)__ — це безкоштовний універсальний інструмент для баз даних із відкритим кодом для розробників і адміністраторів баз даних.

#### Підключення до бази даних:

  - Спочатку потрібно імпортувати модуль `sqlite3` і створити з'єднання з базою даних.
    ```python
    import sqlite3

    # Підключення до бази даних
    db = sqlite3.connect('example.db')  # Якщо файл бази даних не існує, він буде створений
    ```

#### Створення курсору:

  - Курсор використовується для виконання SQL-запитів.
    ```python
    cursor = db.cursor()
    ```

#### Створення таблиці:

  - Для створення таблиці використовуйте метод `execute()` курсора.
    ```python
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    ''')
    ```

#### Вставка даних:

  - Дані можна вставити за допомогою SQL-запиту `INSERT INTO`.
    ```python
    cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
    ''', ('John Doe', 28))

    # Фіксуємо зміни
    db.commit()
    ```

#### Запит даних:

  - Для отримання даних з таблиці використовуйте запит `SELECT`.
    ```python
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    ```

#### Оновлення даних:

  - Для оновлення записів в таблиці використовуйте запит `UPDATE`.
    ```python
    cursor.execute('''
    UPDATE users SET age = ? WHERE name = ?
    ''', (29, 'John Doe'))
    db.commit()
    ```

#### Видалення даних:

  - Для видалення записів з таблиці використовуйте запит `DELETE`.
    ```python
    cursor.execute('''
    DELETE FROM users WHERE name = ?
    ''', ('John Doe',))
    db.commit()
    ```

#### Закриття з'єднання:

  - Після завершення роботи з базою даних, не забудьте закрити з'єднання.
    ```python
    db.close()
    ```

#### Обробка винятків:

  - Для обробки помилок використовуйте блоки `try` і `except`.
    ```python
    try:
        # Ваш код для роботи з базою даних
    except sqlite3.Error as e:
        print(f"Помилка: {e}")
    finally:
        if conn:
            db.close()
    ```

---

[Документація SQLite](https://www.sqlite.org/lang.html)

[SQL](https://sqlzoo.net/wiki/SQL_Tutorial)