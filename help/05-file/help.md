# Заняття 5

### Робота з файлами

### [&#8678; Зміст](../index.md)

---

#### Основні операції з файлами
Python надає зручний та простий інтерфейс для роботи з файлами. 
Основні операції включають відкриття, читання, запис та закриття файлів. 
Для цього використовуються вбудовані функції модуля `io`.

```python
try:
    file = open("hello.txt", mode="w")
    file.write("Hello, World!")
finally:
    file.close()
```

### Відкриття файлу

Файл можна відкрити за допомогою функції `open()`, яка повертає файловий об'єкт. 
Можна вказати режим відкриття файлу:

- `'r'` - читання (за замовчуванням)
- `'w'` - запис (створює новий файл або перезаписує існуючий)
- `'a'` - додавання (додає вміст до кінця файлу)
- `'b'` - бінарний режим
- `'t'` - текстовий режим (за замовчуванням)
- `'+'` - читання та запис

```python
# Відкриття файлу для читання
file = open('example.txt', 'r')
```

### Читання з файлу

Існують різні методи для читання з файлу:
- `read()` - читає весь вміст файлу
- `readline()` - читає один рядок файлу
- `readlines()` - читає всі рядки файлу і повертає їх як список

```python
# Читання всього вмісту файлу
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Читання рядка за рядком
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
```

### Запис у файл
Запис до файлу можна здійснити за допомогою методу `write()` або `writelines()`.

```python
# Запис тексту до файлу
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')

# Додавання тексту до файлу
with open('example.txt', 'a') as file:
    file.write('Additional line.\n')
```

### Закриття файлу

Файл потрібно закривати після роботи з ним, щоб звільнити ресурси. 
Це можна зробити за допомогою методу `close()`. 
Однак, кращою практикою є використання менеджера контексту `with`, 
який автоматично закриває файл.

```python
file = open('example.txt', 'r')
content = file.read()
file.close()

# Використання менеджера контексту
with open('example.txt', 'r') as file:
    content = file.read()
```

### Робота з бінарними файлами

Для роботи з бінарними файлами використовуйте режим `'b'`.

```python
# Запис бінарних даних
with open('example.bin', 'wb') as file:
    file.write(b'\xDE\xAD\xBE\xEF')

# Читання бінарних даних
with open('example.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)
```

#### Документація

- [Документація Python: Робота з файлами](https://docs.python.org/3/library/io.html)

