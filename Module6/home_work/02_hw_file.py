# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    summ = 0
    non_number = []
    for line in f:
        try:
            summ += int(line.rstrip())
        except ValueError:
            non_number.append(line.rstrip())
    if len(non_number) > 0:
        print(f"Имеются не числовые значения: {', '.join(non_number)}, данные значения исключены.")

    print(f"Сумма всех чисел равна {summ}")
