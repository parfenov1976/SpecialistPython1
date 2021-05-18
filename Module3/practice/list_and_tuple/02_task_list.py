# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

'''
i = 0
for element in fruits:
    i += 1
    print(i, element)
'''

for i, element in enumerate(fruits):
    print(i, element)
