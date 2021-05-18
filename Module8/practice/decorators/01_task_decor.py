# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)

def stars(f):
    def wrapper(*args):
        print('*' * (len(str(f(*args))) + 2))
        print(f'*{f(*args)}*')
        print('*' * (len(str(f(*args))) + 2))
    return wrapper


@stars
def sum(a, b):
    return a + b

sum(5, 12)
# res = stars(sum)
# print(res(5, 7))

@stars
def print_deco(n):
    return n

print_deco('Привет')
print_deco(500)
