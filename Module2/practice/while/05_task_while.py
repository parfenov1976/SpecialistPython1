# Вывод символов по диагоналям
# Даны сторона квадрата. Вывести его диагонали символами #.
# Формат входных данных: На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных: Требуется вывести диагонали символами # (см. примеры)
# Примеры:
# a = 6
#    #
 #  #
  ##
  ##
 #  #
#    #

# a = 3
# #
 #
# #


# TODO: your code here
a = int(input("a: "))
b = a
while b//2>0:
    print(" "*((a-b)//2)+"#"+" "*(b-2)+"#")
    b -= 2
if a%2 != 0:
    print(" "*(a//2)+"#")
b += 2    
while b//2 <= a//2:
    print(" "*((a-b)//2)+"#"+" "*(b-2)+"#")
    b += 2
