# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here


n = str(input("Введите количество коров n: "))
if n == "0":
    print("На лугу нет коров")
elif 11 <= int(n)%100 <= 14 or n[-1]=="0" or 5 <= int(n[-1]) <= 9:
    print("На лугу пасутся", n, "коров")
elif n[-1] == "1":
    print("На лугу пасется",n , "корова")
else:
    print("На лугу пасутся",n , "коровы")

"""    
#правильное решение
n = int(input("Введите количество коров n: "))
if n == "0":
    print("На лугу нет коров")
elif 11 <= n % 100 <= 14 or n % 10 == 0 or 5 <= n % 10 <= 9:
    print("На лугу пасутся", n, "коров")
elif n[-1] == "1":
    print("На лугу пасется",n , "корова")
else:
    print("На лугу пасутся",n , "коровы")
"""
