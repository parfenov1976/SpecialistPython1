# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci(n):
    """Compute the Fibonacci number

    :param n: the number of the element in numeric sequence of Fibonacci numbers -> int
    :return: Fibonacci number -> int
    """
    if n in (1, 2):
        return 1
    f = [1, 1]
    i = 2
    while i < n:
        i += 1
        fs = f[1]
        f[1] = f[0] + f[1]
        f[0] = fs
    return f[1]


n = int(input("Введите номе числа Фибоначчи n: "))
print(fibonacci(n))
