# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов

import random

random.seed(20)


def rnd_numbers_lst(n, at, to):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(at, to))
    return numbers


# задача 1
lst = rnd_numbers_lst(10, -50, 50)
print(lst)
new_lst = []

for el in lst:
    if el <= 10:
        new_lst.append(el)
print(len(new_lst))

# задача 2
print(sum(list(filter(lambda n: n > 0, lst))))

# задача 3
even_list = list(filter(lambda n: n % 2 == 0, lst))
print(sum(even_list) / len(even_list))
