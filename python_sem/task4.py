# Задача №25:
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# Решение задачи №25:
# str = 'a a a b c a a d c d d'
# a = str.split()
# b = dict().fromkeys(a, 0)
# for i in a:
#     if b[i] == 0:
#         print(i, end = " ")
#     else:
#         print(f"{i}_{b[i]}", end = " ")
#     b[i] += 1

# Решение задачи №25 вариант 2:
# stroka = input("Введите строку: ").split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1


# Задача №27:
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
# Решение задачи №27:
# text = input("Введите текст: ").split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))

