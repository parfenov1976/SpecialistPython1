# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

def leap_year_check(year):
    return year % 400 == 0 or year % 4 == 0 and not year % 100 == 0


days = [0, 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одинадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
        'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
        'двадцать девятое', 'тридцатое', 'тридцать первое']
months = [0, 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']

data = input("Введите дату в формате dd.mm.yyyy: ")
data = data.split('.')

# проверка корректности даты
if (int(data[0]) == 29 and int(data[1]) == 2 and not leap_year_check(int(data[2]))) \
        or (int(data[0]) > 29 and int(data[1]) == 2) \
        or (int(data[0]) > 30 and (int(data[1]) == 4 or int(data[1]) == 6 or int(data[1]) == 9 or int(data[1]) == 11)) \
        or int(data[0]) > 31 or int(data[1]) > 12:
    print("Некорректная дата")
else:
    print(days[int(data[0])], months[int(data[1])], data[2], 'года.')
