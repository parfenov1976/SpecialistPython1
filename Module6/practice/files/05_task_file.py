# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально,
# а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def keys_correction(k):
    """Функция корректировки списка ключей. Работает при условии,
    что в имени столбца его наименование начинается со слова с заглавной буквы
    и в качестве разделителя между словами наименования использован пробел

    :param k: список ключей из отдельных слов
    :return: список ключей с объединением наменований столбцов
    """
    final_keys = []
    for i in range(len(k)):
        tmp = k[i]
        if k[i].capitalize() != k[i]:
            final_keys.pop()
            tmp = k[i - 1] + ' ' + k[i]
        final_keys.append(tmp)
    return final_keys


# Открытие и чтение файлов с исходными данными
with open("data/workers.txt", "r", encoding="utf-8") as workers:
    workers = workers.readlines()

with open("data/hours_of.txt", "r", encoding="utf-8") as hours:
    hours = hours.readlines()

# создание списка ключей
keys_h = keys_correction(hours[0].split())
keys_w = keys_correction(workers[0].split())

# создание таблиц в виде списка словарей
w_table = []
for line in workers[1:]:
    w_table.append(dict(zip(keys_w, line.split())))

h_table = []
for line in hours[1:]:
    h_table.append(dict(zip(keys_h, line.split())))

# создание объединенной таблицы в виде списка словарей
for line in w_table:
    for el in h_table:
        if line.get(keys_w[0]) == el.get(keys_h[0]) and line.get(keys_w[1]) == el.get(keys_h[1]):
            line.update(el)

keys = list(w_table[0].keys())  # извленчение списка ключей

# Расчет размеров выплат
for line in w_table:
    c = line.get(keys[2])
    if int(line.get(keys[4])) < int(line.get(keys[5])):
        c = str(int(c) + int(int(line.get(keys[2])) / int(line.get(keys[4])) * 2 * (
                    int(line.get(keys[5])) - int(line.get(keys[4])))))
    elif int(line.get(keys[4])) > int(line.get(keys[5])):
        c = str(int(int(line.get(keys[2])) / int(line.get(keys[4])) * int(line.get(keys[5]))))
    line.update({'К оплате': c})

keys = list(w_table[0].keys())  # извленчение нового списка ключей

# Вывод таблицы выплат
print(f'{keys[0]:<10}{keys[1]:<10}{keys[2]:<10}{keys[3]:<14}{keys[4]:<12}{keys[5]:<17}{keys[6]:<10}')
print('=' * 81)
for line in w_table:
    print(f'{line.get(keys[0]):<10}{line.get(keys[1]):<10}{line.get(keys[2]):<10}{line.get(keys[3]):<14}'
          f'{line.get(keys[4]):^12}{line.get(keys[5]):^17}{line.get(keys[6]):<10}')
