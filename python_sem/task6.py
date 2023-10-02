# Решение №1:
# string = input("Введите слово или число: ")
# if (string == string[::-1]):
#     print("Это полиндром!")
# else:
#     print("Это не полиндром")

# Решение №2 рекурсией:
# a = input("Введите слово: ")
# def polindrome(x):
#     if len(x) <=1:
#         return True
#     elif x[0] == x[-1]:
#         return polindrome(x[1:-1])
#     return False
# print(polindrome(a))

# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с н
# Решение задачи:
# a = input("Введите список первых чисел: ").split()
# b = input("Введите список вторых чисел: ").split()
# result = []

# for i in a:
#     if i not in b:
#         result.append(i)

# print(result)

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# Решение задачи:
# a = input("Введите число: ").split()
# counter = 0

# for i in range(1, len(a)-1):
#     if a[i -1] < a[i] > a[i + 1]:
#         counter += 1

# print(counter)

# Задача:
# Решение задачи:

# from random import randint

# lst = [randint(1, 10) for i in range(10)]
# print(lst)
# count = 0
# for item in set(lst):
#     count += lst.count(item)//2

# print(count)


# Решение от GB:
# list_1 = [1, 2, 3, 2, 3]
# count = 0
# for i in range(len(list_1)):
#     for j in range(i + 1, len(list_1)):
#         if i != j and list_1[i] == list_1[j]:
#             count += 1
# print(count)



# numbers = input("Введите числа без пробела: ")
# print(numbers)
# count = 0
# for i in range(len(numbers)):
#     count += numbers[i+1:].count(numbers[i])

# print(count)