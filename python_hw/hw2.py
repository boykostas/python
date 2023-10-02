# Урок 2. Циклы (for, while)
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# Решение задачи №10:
# n = int(input('Введите количество монет: '))
# orel = reshka = 0
# for i in range(n):
#     x = int(input('Ввидите 1 (Орел) или 0 (Решка): '))
#     if x == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(f'Переверните {orel} монет с орла на решку, их меньше всего!')
# elif orel == reshka:
#     print(f'Количество орлов и решек одинаково, по {orel} штук')
# else:
#     print((f'Переверните {reshka} монет с решки на орла, их меньше всего!'))


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Решение задачи №12:
# x = abs(int(input('Введите первое натуральное число x: ')))
# y = abs(int(input('Введите второе натуральное число y: ')))
# S = x + y
# P = x * y
# print(f"Подсказка: сумма загаданных чисел: {S}")
# print(f"Подсказка: произведение загаданных чисел: {P}")
# x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# print(f"Первое число: {x1}, второе число: {y1}")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Решение задачи №14:
# n = int(input("Введите число N: "))
# i =0
# while 2 ** i <=n:
#     print (2 ** i)
#     i += 1