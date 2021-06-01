# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def operation_type(text):
    """Extract type of operation. Return tuple with sign of operation and its index in the string

    :param text: string with fractions type like n x/y + m o/p
    :return:
        op_type: type of operation -> str
        op_poz: index of operation sign -> int
    """

    op_type = ''
    op_poz = 0
    if text.find(' / ') > 0:
        op_poz = text.find(' / ') + 1
        op_type = text[op_poz]
    elif text.find(' * ') > 0:
        op_poz = text.find(' * ') + 1
        op_type = text[op_poz]
    elif text.find(' - ') > 0:
        op_poz = text.find(' - ') + 1
        op_type = text[op_poz]
    elif text.find(' + ') > 0:
        op_poz = text.find(' + ') + 1
        op_type = text[op_poz]
    return op_type, op_poz


def mixed_to_improper_fraction(mixed):
    """Mixed fraction to improper conversion

    :param: string with mixed fraction like 'n x/y' in string
    :return: improper fraction in tuple whit int (numerator, denominator)
    """

    mixed = mixed.replace('/', ' ')
    mixed = mixed.split()
    mixed = list(map(int, mixed))
    if len(mixed) == 1:
        return mixed[0], 1  # integer to improper fraction conversion
    elif len(mixed) == 2:
        return tuple(mixed)
    imp_fr = (abs(mixed[0]) * mixed[2] + mixed[1]) * (-1 if mixed[0] < 0 else 1), mixed[2]
    return imp_fr


def get_answer(f1, f2, oprn):
    """Сalculation with two fractions

    :param f1: first fraction
    :param f2: second fraction
    :param oprn: type of operation
    :return: improper fraction
    """

    if oprn[0] == '+':
        return f1[0] * f2[1] + f1[1] * f2[0], f1[1] * f2[1]
    elif oprn[0] == '-':
        return f1[0] * f2[1] - f1[1] * f2[0], f1[1] * f2[1]
    elif oprn[0] == '*':
        return f1[0] * f2[0], f1[1] * f2[1]
    elif oprn[0] == '/':
        return f1[0] * f2[1], f1[1] * f2[0]


def improper_to_mixed_fraction(f):
    """Improper fraction to mixed conversion

    :param f: fraction in format (numerator, denominator)
    :return: fraction in format (integer part, numerator, denominator)
    """
    integer_part = f[0] // f[1]
    denominator = f[1]
    numerator = f[0] - integer_part * denominator
    if numerator == 0:
        return integer_part, 0, 0
    if denominator % numerator == 0:
        return integer_part, 1, int(denominator / numerator)
    i = 2
    while i <= int(numerator ** 0.5):
        if numerator % i == 0 and denominator % (numerator / i) == 0:
            return integer_part, i, int(denominator / (numerator / i))
        elif numerator % i == 0 and denominator % i == 0:
            return integer_part, int(numerator / i), int(denominator / i)
        else:
            i += 1
    return integer_part, numerator, denominator


expression = input("Введите выражение с дробями в формате n x/y: ")
op = operation_type(expression)
try:
    a, b = expression.split(' ' + op[0] + ' ')
    # split expression by operation sign in two strings with fraction in each

    a = mixed_to_improper_fraction(a)
    b = mixed_to_improper_fraction(b)
    c = get_answer(a, b, op)
    c = improper_to_mixed_fraction(c)

    if c[0] == 0 and c[1] == 0:
        print('0')
    print(f"{c[0] if c[0] != 0 else ''} {'' if c[1] == 0 else c[1]}"
          f"{'' if c[1] == 0 else '/'}{'' if c[1] == 0 else c[2]}".strip())
except (ZeroDivisionError, ValueError):
    print("Введены не корректные данные")
    quit()
