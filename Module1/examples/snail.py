# Время подъема улитки до вершины шеста
def solution(h, a, b):
    """
    Подсчет количества дней для подъема улитки по шесту
    :param h: Высота шеста
    :param a: Высота, на которую поднимается улитка за день
    :param b: Высота, на которую улитка спускается за ночь
    :return:
    """
    d = (h - b - 1) // (a - b) + 1
    return d


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert solution(h=10, a=3, b=2) == 8
    assert solution(h=20, a=7, b=3) == 5
    assert solution(h=10, a=10, b=0) == 1
    print("All test done!!!")
