import math
#определение этажа по номеру квартиры
flat_namber = int(input("Введите номер квартиры: "))

#1-ый способ - работает без math
print ("Номер этажа", (flat_namber-1)//12+1)

#2-ой способ - с округлением вверх math.ceil()
print ("Номер этажа", math.ceil(flat_namber/12))