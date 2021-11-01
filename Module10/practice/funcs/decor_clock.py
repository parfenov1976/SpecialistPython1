def clock(func):
    def clocked(*args, **kwargs):
        import time
        t0 = time.time()

        result = func(*args, **kwargs)  # вызов декорированной функции

        elapsed = time.time() - t0
        name = func.__name__
        arg_1st = []
        if args:
            arg_1st.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_1st.append(', '.join(pairs))
        arg_str = ', '.join(arg_1st)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def fac(n):
    def factorial(n):
        """
        Рекурсивная функция
        :param n: int
        :return: int
        """
        if n > 1:
            return n * factorial(n - 1)
        return 1

    return factorial(n)


@clock
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
print(f'N!= {fac(n)}')
print(f'N!= {fact(n)}')


@clock
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


@clock
def fibcci(n):
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
    return fibonacci(n)


n = int(input("Введите номе числа Фибоначчи n: "))
print(fib(n))
print(fibcci(n))
