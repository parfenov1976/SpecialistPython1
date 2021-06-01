# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def can_triangle(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p2, *p3)
    c = distance(*p1, *p3)
    return a + b > c and a + c > b and b + c > a


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def triangle_perimeter(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p2, *p3)
    c = distance(*p1, *p3)
    return a + b + c


def triangle_area(p1, p2, p3):
    a = distance(*p1, *p2)
    b = distance(*p2, *p3)
    c = distance(*p1, *p3)
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


pa = 4, 6
pb = 2, -6
pc = -2, 12

if not can_triangle(pa, pb, pc):
    print("Не треугольник")
else:
    print(f"Периметр треугольника = {triangle_perimeter(pa, pb, pc)}")
    print(f"Площадь треугольника = {triangle_area(pa, pb, pc)}")

# Не забудьте протестировать вашу функцию
