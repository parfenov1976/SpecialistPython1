# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    # return str(number) == str(number)[::-1]
    rev_n = 0
    copy_n = number
    while copy_n:
        rev_n = 10 * rev_n + copy_n % 10
        copy_n = copy_n // 10
    return number == rev_n


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))

# if palindrome(4567654):
#     print("Число палиндром")
