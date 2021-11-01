# Напишите функцию принимающую на вход целое числом n. И возвращающую список из n элементов.
# заполненный случайными целыми числами в диапазоне от a до b.
# Примечание: для генерации случайного числа используйте import random
from random import randint


def rand_list(n, a, b):
    numbers_list = []
    while n > 0:
        numbers_list.append(randint(a, b))
        n -= 1
    return numbers_list


n = int(input('Введите количество членов ряда случайных чисел: '))
a = int(input('Введите нижнюю границу диапазона: '))
b = int(input('Введите верхнюю границу диапазона: '))

print(f'Ряд случайных {n} чисел из в диапазоне от {a} до {b}')
print(rand_list(n, a, b))
