# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]

# TODO: your code here
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}

# 1-ый вариант
# my_dict = {}
# for i in range(len(keys)):
#     my_dict[keys[i]] = values[i]
# print(my_dict)

# 2-й вариант
# my_dict = {}
# for key, value in zip(keys, values):
#     my_dict[key] = value
# print(my_dict)

# 3-й вариант - предпочтительный
my_dict = dict(zip(keys, values))
print(my_dict)
