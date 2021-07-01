# Даны два уравнения прямых вида у=kx+b и виде строки. Проверить, пересекаются ли данные прямые?
# Примеры уравнений: "y = 2x + 4"  "y = -12x -12"

# Проверьте входные данные на корректность

def extract_param(string):
    i = 0
    param_ = ['', '']
    for el in string:
        if el == '-' or el.isdigit():
            param_[i] += str(el)
        elif el == 'x':
            i += 1
    param_ = list(map(int, param_))
    return param_


def check_data(string, param_):
    new_string = f'y={param_[0]}x' + ('+' if param_[1] >= 0 else '') + f'{param_[1]}'
    return string.replace(' ', '') == new_string


while True:
    # Ввод исходных данных
    print('Введите урнавления прямых в виде: y = kx + b')
    straight_1 = input('Введите уравнение 1-ой прямой: ')
    straight_2 = input('Введите уравнение 2-ой прямой: ')
    try:
        # Извлечение параметров прямых
        straight_1_param = extract_param(straight_1)
        straight_2_param = extract_param(straight_2)
        # проверка корректности исходных данных
        if not check_data(straight_1, straight_1_param) and not check_data(straight_2, straight_2_param):
            raise ValueError
        break
    except ValueError:
        print("Введены некорректные данные, прошу повторить ввод.")

if straight_1_param[0] == straight_2_param[0] and straight_1_param[1] != straight_2_param[1]:
    print('Прямые не пересекаются')
elif straight_1_param[0] == straight_2_param[0] and straight_1_param[1] == straight_2_param[1]:
    print('Прямые совпадают')
else:
    print('Прямые пересекаются')
