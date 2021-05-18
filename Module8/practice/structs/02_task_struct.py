# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

random.seed(20)


def rnd_numbers_lst(n, at, to):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(at, to))
    return numbers


lst = rnd_numbers_lst(10, 1, 10)

# 1 - вариант - плохой
# for el in lst[:]:
#     if lst.count(el) > 1:
#         lst.remove(el)
# print(lst)

# 2 - вариант - тоже не очень
# d = {}
# for num in lst:
#     if num in d:
#         d[num] +=1
#     else:
#         d[num] = 1
# print(d)

# лучший вариант
uniq_list = list(set(lst))
print(uniq_list)

# uniq_list = []
# for el in lst:
#     if el not in uniq_list:
#         uniq_list.append(el)

# задача 2
# 1- вариант
# only_one_list = []
# for el in lst:
#     if lst.count(el) == 1:
#         only_one_list.append(el)

# 2 вариант - генератор списка
only_one_list = [el for el in lst if lst.count(el) == 1]
print(only_one_list)
