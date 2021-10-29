import re

"""
Часть-1:
Ниже находятся строки с различными символами, но одинаковой длины.
Попробуйте написать шаблон, который будет соответствовать первым
трем строкам, но не соответствовать последней.
"""

re_list1 = ['cats.', '8967.', '?=+!.', 'abcd1']
pattern1 = r'\.'
print(list(filter(lambda string: re.findall(pattern1, string), re_list1)))

"""
Часть-2:
Ниже находится несколько строчек, где мы хотим сопоставить только первые три строки, 
последние три строки мы сопоставлять не хотим. 
Обратите внимание, как при использовании метасимвола точки 
мы не сможем избежать совпадения с последними тремя строками.
Соответствовать	can	
Соответствовать	man	
Соответствовать	fan	
Пропустить		dan
Пропустить		ran	
Пропустить		pan
"""

re_list2 = ['can', 'man', 'fan', 'dan', 'ran', 'pan']
pattern2 = r'c|m|f'
print(list(filter(lambda string: re.findall(pattern2, string), re_list2)))

"""
Часть-3:
Для строк ниже напишите выражение, которое будет соответствовать как полной дате, так и только годам.
    Дано        Захватить 1	Захватить 2
Date Jan 1987	Jan 1987	1987
Date May 1969 	May 1969	1969
Date Aug 2011	Aug 2011	2011

"""
re_list3 = ['Date Jan 1987', 'Date May 1969', 'Date Aug 2011']
pattern31 = r'Date '
pattern32 = r'\d{4}'
print(list(map(lambda string: re.sub(pattern31, '', string), re_list3)))
print([re.search(pattern32, string).group() for string in re_list3])

"""
Задание-1 “Простые регулярки”
Данo произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
Найдите:
1.	первое слово из строки
2.	первые два символа каждого слова
3.	все слова начинающиеся на гласную букву
4.	все слова начинающиеся на согласную букву
5.	все уникальные(без дубликатов) знаки препинания
"""
string_task1 = 'Данo произвольное предложение. Анна любит, Алексея. Слова разделены пробелами. Предложение содержит знаки препинания.'
pattern_11 = r'^\w*'
print(re.findall(pattern_11, string_task1))
pattern_12 = r'\b\w{2}'
print(re.findall(pattern_12, string_task1))
pattern_13 = r'\b[аоэеиыуёюя]\w*'
print(re.findall(pattern_13, string_task1, flags=re.I))
pattern_14 = r'\b[бвгджзйклмнпрстфхцчшщ]\w*'
print(re.findall(pattern_14, string_task1, flags=re.I))
pattern_15 = r'[^\w ]'
print(set(re.findall(pattern_15, string_task1)))

"""
Задание-2
Дан текст в котором упоминаются IP-адреса. Найдите все упоминаемые IP.
Пример текста:  
"""
text = """
Все публичные серверы и сайты в сети Интернет используют "белые" IP-адреса (например, сайт google.com — 172.217.22.14, 
DNS-сервер Google — 8.8.8.8, сайт yandex.ru — 213.180.204.11, DNS-сервер Яндекс.DNS — 77.88.8.8). 
Все публичные IP-адреса в сети Интернет уникальны и не могут повторяться.
Точно известно, что все IP-адреса в тексте являются корректными, т.е. не будут встречаться адреса вида 900.400.18.56
"""
pattern_2 = r'\d+3?\.\d+3?\.\d+3?\.\d+3?'
print(re.findall(pattern_2, text))

"""
Задание-3
Проверить, является ли заданная строка доменным именем для протоколов http или https, с необязательным слешем в конце.
Специальные символы не используются.
Примеры:
"""
adress1 = 'http://example.com/'  # Да
adress2 = 'example.com'  # Нет
adress3 = 'https://кремль.рф'  # Да

pattern_3 = r'(http|https)://\w+\.\w+'
print(re.match(pattern_3, adress1) is not None)
print(re.match(pattern_3, adress2) is not None)
print(re.match(pattern_3, adress3) is not None)

"""
Задание-4
Дан текст: "World War II began on Sep 1939 and ended on Sep 1945. Victory Day has been celebrated since 1945."
Найдите и выведите все года, которым предшествует месяц.
"""
text4 = "World War II began on Sep 1939 and ended on Sep 1945. Victory Day has been celebrated since 1945."

pattern_4 = r'\b\w{3} \d{4}?'
print(re.findall(pattern_4, text4))
