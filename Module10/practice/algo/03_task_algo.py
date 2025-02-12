# "Кинотеатр"
# X мальчиков и Y девочек пошли в кинотеатр и купили билеты на подряд идущие места в одном ряду.
# Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом с каждым мальчиком
# сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку, в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи. Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку “Нет решения”.
b = int(input('Введите количество мальчиков: '))
g = int(input('Введите количество девочек: '))
c = b + g
raw = ''
while g > 0 and b > 0:
    if b == g and g > 0 and b > 0:
        raw += 'BG'
        b -= 1
        g -= 1
    elif b > g and b > 1:
        raw += 'BGB'
        b -= 2
        g -= 1
    elif b < g and g > 1:
        raw += 'GBG'
        b -= 1
        g -= 2
if len(raw) == c:
    print(raw)
else:
    print('Задача не имеет решения')
