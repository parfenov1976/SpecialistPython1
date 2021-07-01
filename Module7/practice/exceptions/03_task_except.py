# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.


def str_to_tuple(d_string):
    return tuple(map(int, d_string.split()))


def check_data(d_tuple):
    if len(d_tuple) != 5:
        print('Количество введенных чисел меньше или больше 5')
        return False
    for el in d_tuple:
        if el > 0:
            return True
    print('Нет положительных чисел')
    return False


def min_pos(d_tuple):
    m_p = d_tuple[0]
    for el in d_tuple:
        if 0 < el < m_p:
            m_p = el
    return m_p


while True:
    # digit_str = "2 12 -45 7 10"
    digit_str = input('Введите пять целых чисел через пробел: ')
    try:
        digit_tuple = str_to_tuple(digit_str)
        if not check_data(digit_tuple):
            raise UserWarning
        break
    except UserWarning:
        print("Введены некорректные данные, прошу повторить ввод.")
    except ValueError:
        print("Обнаружены не числовые данные")
        print("Введены некорректные данные, прошу повторить ввод.")

print('Минимальное положительное число равно:', min_pos(digit_tuple))
