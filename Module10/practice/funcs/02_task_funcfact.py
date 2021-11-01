# Напишите функцию нахождения факториала числа n
# Примеры нахождения факториала:
# 5! = 1*2*3*4*5
# 7! = 1*2*3*4*5*6*7

def factorial(n):
    """
    Рекурсивная функция
    :param n: int
    :return: int
    """
    if n > 1:
        return n * factorial(n - 1)
    return 1

def fact(n):
    """
    Прямая итерация
    :param n: int
    :return: int
    """
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

n = int(input('Введите чило: '))
print(f'N!= {factorial(n)}')
print(f'N!= {fact(n)}')
