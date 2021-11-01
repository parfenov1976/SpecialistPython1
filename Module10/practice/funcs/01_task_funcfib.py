# Напишите функцию нахождения n-ого числа Фибоначчи
# Пример ряда чисел Фибоначчи: 0 1 1 2 3 5 8 13 ...
# (сумма элемента равна сумме двух предыдущих)

def fib(n):
    """
    Решение в лоб
    :param n:
    :return:
    """
    a = b = 1
    i = 2
    while i < n:
        i += 1
        a, b = b, a + b
    return b


def fibonacci(n):
    """
    Рекурсивная функция
    :param n:
    :return:
    """
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Введите номе числа Фибоначчи n: "))
print(fib(n))
print(fibonacci(n))
