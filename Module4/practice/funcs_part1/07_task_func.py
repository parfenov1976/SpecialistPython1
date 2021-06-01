# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def time(secondss):
    ss = secondss % 60
    mm = (secondss // 60) % 60
    hh = (secondss // 60) // 60
    return f"{hh:02}:{mm:02}:{ss:02}"


seconds = int(input("Введите количество секунд: "))
print(time(seconds))
