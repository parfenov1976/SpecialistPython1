def deposit(money, sp, years):
    """функция принимает три числа и возвращает одно -
    итоговая сумма на счету по простому проценту.

    :param money: сумма вложенных денег в рублях -> float
    :param sp: процентная ставка в % -> float
    :param years: срок вклада в годах -> int
    :return: итоговая сумма в рублях -> float
    """
    return money * (1 + years * sp / 100)


def comp_deposit(money, cp, years):
    """функция принимает три числа и возвращает одно -
    итоговая сумма на по сложному проценту
    с капитализацией каждый месяц.

     :param money: сумма вложенных денег в рублях > float
     :param cp: процентная ставка в % -> float
     :param years: срок вклада в годах -> int
     :return: итоговая сумма в рублях > float
     """
    return money * (1 + cp / (12 * 100)) ** (12 * years)


def days_in_year(num_year):
    """Функция определения количества дней в году по номеру года

    :param num_year: номер года -> int
    :return: количество дней в году -> int
    """
    if num_year % 400 == 0 or num_year % 4 == 0 and not num_year % 100 == 0:
        return 366
    return 365


def fib(n):
    """Поиск числа Фибоначчи

    :param n: номер искомого числа в ряду -> int
    :return: n-е чило Фибоначчи  -> int
    """
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


def gen_list(size, of, to):
    from random import randint
    """Функция генерации списка случайных чисел

    :param size: размер списка -> int
    :param of:
    :param to:
    :return:
    """
    my_list = []
    for n in range(size):
        my_list.append(randint(of, to))
    return my_list


def time(secondss):
    """Преобразование секунд в формате времени чч:мм:сс

    :param secondss: количество секунд
    :return: время в формате времени чч:мм:сс
    """
    ss = secondss % 60
    mm = (secondss // 60) % 60
    hh = (secondss // 60) // 60
    return f"{hh:02}:{mm:02}:{ss:02}"
