# Напишите функцию декоратор, которая округляет значение декорируемой функции до двух знаков после  запятой.
# Если округление невозможно, например там строка, или не требуется(целое число) то оставляем результат без изменений.
# Примечание: используйте встроенную функцию round()

def round_deco(func):
    def wrapper(*arg):
        print(type(func(*arg)))
        if type(func(*arg)) is not float:
            return func(*arg)
        else:
            return round(func(*arg), 2)
    return wrapper


@round_deco
def a_b(a, b):
    return a / b


@round_deco
def print_deco(n):
    return n


print(a_b(1, 3))  # в результате вычисления получено float
print(a_b(3, 1))  # в результате вычисления получено float
print(print_deco(3))  # здесь имеем int
print(print_deco('Строка'))  # здесь имеем str
