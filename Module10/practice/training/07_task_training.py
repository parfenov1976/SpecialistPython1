# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.
from random import randint

number = ''
while len(str(number)) < 20000:
    number += str(randint(0, 10))
with open('data.txt', 'w', encoding='UTF-8') as f:
    f.write(number)
