# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci(n):
    """Compute the Fibonacci number

    :param n: the number of the element in numeric sequence of Fibonacci numbers -> int
    :return: Fibonacci number -> int
    """
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Введите номе числа Фибоначчи n: "))
print(fibonacci(n))
