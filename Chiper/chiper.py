# Шифр Цезаря


import pyperclip

# Строка, подлежащая шифрованию/дешифрованию
massage = input("Введите сообщение, которое хотите зашифровать/дешифровать: ")

# Ключ, штфрования/дешифрования
key = int(input("Введите ключ шифрования: "))

# Установка режива работы: шифрование или дешифрование
mode = input("Введите '1' - если хотите зашифровать сообщение  или '0' - если хотите расшифровать сообщение: ")

# Вск символы, которые могут быть защифрованы
SYMBOLS = 'ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдеёжзийклмнопрстуфхцчшщэюя1234567890 !?.,@#$%^&*-+(){}[]_/`~<>'

# Переменная, хранящая защифрованную/дешифрованную форму сообщения
translated = ''

for symbol in massage:
    # Шифровать/дешифровать можно только символы, включенные в строку SYMBOLS
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Выполнить шифрование/дешифрование
        if mode == '1':
            translatedIndex = symbolIndex + key
        elif mode == '0':
            translatedIndex = symbolIndex - key

        # Обработать "завертывание", если необходимо
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Присоединить символ без шифрования/дешифрования
        translated = translated + symbol

# Вывод преобразованной строки
print(translated)
pyperclip.copy(translated)   
