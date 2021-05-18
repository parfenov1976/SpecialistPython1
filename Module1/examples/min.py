#минимальное из двух чисел
a = int (input("a: "))
b = int (input("b: "))
print ("Min=", int(((a+b)-abs(a-b))/2))