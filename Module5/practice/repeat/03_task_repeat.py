# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    return str(number) == str(number)[::-1]


a = 10
b = 10000
c = 0
for n in range(b - a):
    if palindrome(n):
        c += 1
print(c)
