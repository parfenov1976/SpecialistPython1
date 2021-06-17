# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci(n):
    """Compute the Fibonacci number

    :param n: the number of the element in numeric sequence of Fibonacci numbers -> int
    :return: Fibonacci number -> int
    """
    a = b = 1
    i = 2
    while i < n:
        i += 1
        a, b = b, a + b
    return b


n = int(input("Введите номе числа Фибоначчи n: "))
print(fibonacci(n))
