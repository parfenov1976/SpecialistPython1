# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

# def my_sum(*args):
#     s = 0
#     for arg in args:
#         s += arg
#     return s

def average(*args):
    return sum(args)/len(args)


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
