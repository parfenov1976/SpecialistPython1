# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here
a = int (input("a: "))
b = int (input("b: "))
c = int (input("c: "))

if a == b or a == c or b == c:
    print("YES")
else:
    print("NO")
